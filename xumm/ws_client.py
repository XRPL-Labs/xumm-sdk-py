#!/usr/bin/env python
# coding: utf-8

import logging
import time
import json
import sys
from multiprocessing import Queue
from threading import Thread, Event, Timer
from typing import Dict, Any

from websocket import (
    enableTrace,
    WebSocketApp
)

class WSClient(Thread):
    """
    Higher level of APIs are provided.
    The interface is like JavaScript WebSocket object.
    """
    def __init__(cls, server=None, timeout=None, log_level=None, *args, **kwargs):
        """
        Args:
            server: rippled node url.
            timeout: connection timeout seconds
            log_level: loggin level
            on_open: callable object which is called at opening websocket.
            on_reconnect: callable object which is called at reconnecting
            on_error: callable object which is called when we get error.
            on_close: callable object which is called when closed the connection.
            on_response: callback object which is called when we recieve message
        """

        # assing any callback method
        available_callbacks = [
            'on_open',
            'on_reconnect',
            'on_close','on_error',
            'on_response'
       ]

        for key,value in kwargs.items():
            if(key in available_callbacks):
                setattr(cls, key, value)

        cls.socket: WebSocketApp = None
        cls.server = server or 'wss://xumm.app/sign'
        cls.responseEvents = dict()
        cls.q = Queue()

        # ledger status
        cls._ledgerVersion = None
        cls._fee_base = None
        cls._fee_ref = None

        # Connection Handling Attributes
        cls.connected = Event()
        cls.disconnect_called = Event()
        cls.reconnect_required = Event()
        cls.reconnect_interval = 10
        cls.paused = Event()

        # Setup Timer attributes
        # Tracks API Connection & Responses
        cls.ping_timer = None
        cls.ping_interval = 10

        # Tracks Websocket Connection
        cls.connection_timer = None
        cls.connection_timeout = timeout if timeout else 30
        cls.response_timeout = timeout if timeout else 30

        # Tracks responses from send_ping()
        cls.pong_timer = None
        cls.pong_received = False
        cls.pong_timeout = 30

        # Logging stuff
        cls.log = logging.getLogger(cls.__module__)
        logging.basicConfig(stream=sys.stdout, format="[%(filename)s:%(lineno)s - %(funcName)10s() : %(message)s")
        if log_level == logging.DEBUG:
            enableTrace(True)
        cls.log.setLevel(level=log_level if log_level else logging.ERROR)

        # Call init of Thread and pass remaining args and kwargs
        Thread.__init__(cls)
        cls.daemon = False

    def connect(cls, nowait = True):
        """
        Simulate cls.start(), run the main thread
        :return:
        """
        cls.start()

        if not nowait:
            return cls.connected.wait()

    def disconnect(cls):
        """
        Disconnects from the websocket connection and joins the Thread.
        :return:
        """
        cls.log.debug("Disconnecting from API..")
        cls.reconnect_required.clear()
        cls.disconnect_called.set()
        if cls.socket:
            cls.socket.close()

        # stop timers
        cls._stop_timers()

        cls.join(timeout=1)

    def status(cls) -> int:
        """
        Get socket status.
        :return:
        """
        if cls.socket.sock:
            return cls.socket.sock.getstatus()

    def reconnect(cls):
        """
        Issues a reconnection by setting the reconnect_required event.
        :return:
        """
        # Reconnect attempt at cls.reconnect_interval
        cls.log.debug("Initiation reconnect sequence..")
        cls.connected.clear()
        cls.reconnect_required.set()
        if cls.socket:
            cls.socket.close()

    def _connect(cls):
        """
        Creates a websocket connection.
        :return:
        """
        cls.log.debug("Initializing Connection..")
        cls.socket = WebSocketApp(
            cls.server,
            on_open=cls._on_open,
            on_message=cls._on_message,
            on_error=cls._on_error,
            on_close=cls._on_close
        )

        cls.log.debug("Starting Connection..")
        cls.socket.run_forever()

        while cls.reconnect_required.is_set():
            if not cls.disconnect_called.is_set():
                cls.log.info("Attempting to connect again in %s seconds."
                              % cls.reconnect_interval)
                cls.state = "unavailable"
                time.sleep(cls.reconnect_interval)

                # We need to set this flag since closing the socket will
                # set it to False
                cls.socket.keep_running = True
                cls.socket.run_forever()

    def run(cls):
        """
        Main method of Thread.
        :return:
        """
        cls.log.debug("Starting up..")
        cls._connect()

    def _on_message(cls, ws, message):
        """
        Handles and passes received data to the appropriate handlers.
        :return:
        """

        # ignore income messages if we are disconnecting
        if cls.disconnect_called.is_set():
            return

        raw, received_at = message, time.time()
        cls.log.debug("Received new message %s at %s", raw, received_at)

        data: Dict[str, Any] = None

        try:
            data = json.loads(raw)
        except json.JSONDecodeError as e:
            cls.log.info("Unknown Response.")
            return

        if isinstance(data, dict):
            # This is a valid message
            cls._data_handler(data, received_at)

        # We've received data, reset timers
        cls._start_timers()

    def _on_close(cls, *args):
        cls.log.info("Connection closed")
        cls.connected.clear()
        cls._stop_timers()

        cls._callback('on_close')

    def _on_open(cls, ws):
        cls.log.info("Connection opened")
        cls.connected.set()
        cls.send_ping()
        cls._start_timers()
        if cls.reconnect_required.is_set():
            cls.log.info("Connection reconnected.")

        cls._callback('on_open', cls)

    def _on_error(cls, ws, error):
        cls.log.info("Connection Error - %s", error)

        # ignore errors if we are disconnecting
        if cls.disconnect_called.is_set():
            return

        cls.reconnect_required.set()
        cls.connected.clear()

        cls._callback('on_error', error)

    def _stop_timers(cls):
        """
        Stops ping, pong and connection timers.
        :return:
        """
        if cls.ping_timer:
            cls.ping_timer.cancel()

        if cls.connection_timer:
            cls.connection_timer.cancel()

        if cls.pong_timer:
            cls.pong_timer.cancel()
        cls.log.debug("Timers stopped.")

    def _start_timers(cls):
        """
        Resets and starts timers for API data and connection.
        :return:
        """
        cls._stop_timers()

        # Sends a ping at ping_interval to see if API still responding
        cls.ping_timer = Timer(cls.ping_interval, cls.send_ping)
        cls.ping_timer.start()

        # Automatically reconnect if we did not receive data
        cls.connection_timer = Timer(
            cls.connection_timeout,
            cls._connection_timed_out
        )
        cls.connection_timer.start()

    def send_ping(cls):
        """
        Sends a ping message to the API and starts pong timers.
        :return:
        """
        cls.log.debug("Sending ping to API..")
        cls.socket.send(json.dumps(dict(command='ping', id='ping')))
        cls.pong_timer = Timer(cls.pong_timeout, cls._check_pong)
        cls.pong_timer.start()

    def _check_pong(cls):
        """
        Checks if a Pong message was received.
       :return:
        """
        cls.pong_timer.cancel()
        if cls.pong_received:
            cls.log.debug("Pong received in time.")
            cls.pong_received = False
        else:
            # reconnect
            cls.log.debug("Pong not received in time."
                           "Issuing reconnect..")
            cls.reconnect()

    def _connection_timed_out(cls):
        """
        Issues a reconnection if the connection timed out.
       :return:
        """
        cls.log.debug("Timeout, Issuing reconnect..")
        cls.reconnect()

    def _pause(cls):
        """
        Pauses the connection.
        :return:
        """
        cls.log.debug("Setting paused() Flag!")
        cls.paused.set()

    def _unpause(cls):
        """
        Unpauses the connection.
        Send a message up to client that he should re-subscribe to all
        channels.
        :return:
        """
        cls.log.debug("Clearing paused() Flag!")
        cls.paused.clear()

    def _data_handler(cls, data, ts):
        """
        Distributes system messages to the appropriate handler.
        System messages include everything that arrives as a dict,
        :param data:
        :param ts:
        :return:
        """
        cls._callback('on_response', data)

    def _callback(cls, callback, *args):
        """Emit a callback in a thread
        :param callback:
        :param *args:
        :return:
        """
        if callback:
            try:
                _callback = getattr(cls, callback, None)
                if _callback is not None and callable(_callback):
                    t = Thread(target=_callback, args=args)
                    t.setDaemon(True)
                    t.start()
            except Exception as e:
                cls.log.error("error from callback {}: {}".format(_callback, e))