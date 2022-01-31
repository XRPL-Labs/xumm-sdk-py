#!/usr/bin/env python
# coding: utf-8

from multiprocessing.sharedctypes import Value
import sys
import time
import json
from testing_config import BaseTestConfig, AsyncioTestCase
from tests.fixtures import (
    xumm_api as test_fixtures,
)
from unittest.mock import Mock, patch
from xumm.ws_client import WSClient

import xumm
import asyncio
import websockets

from threading import Thread, main_thread
from xumm.error import APIError
from xumm.resource.payload import CallbackPromise

COUNT = 0

# import pytest
# @pytest.mark.skip(reason="Using Prod Cert")
class TestPayloadSubscribe(BaseTestConfig):

    server = None
    thread = None

    @classmethod
    async def start_server(cls, ws, path):
        try:
            print('MOCK SOCKET OPEN: {}'.format(ws.open))

            await ws.send(json.dumps(test_fixtures.subscription_updates()['expire']))  # noqa: E501
            print('SENT EXPIRE')
            print(test_fixtures.subscription_updates()['expire'])

            await ws.send(json.dumps(test_fixtures.subscription_updates()['opened']))  # noqa: E501
            print('SENT OPENED')
            print(test_fixtures.subscription_updates()['opened'])

            await ws.send(json.dumps(test_fixtures.subscription_updates()['rejected']))  # noqa: E501
            print('SENT REJECTED')
            print(test_fixtures.subscription_updates()['rejected'])

            await asyncio.sleep(1)

        except KeyboardInterrupt:
            ws.close()

        except Exception as e:
            print('on_open Error: {}'.format(e))
            ws.close()

    @classmethod
    def startup_server(cls):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        start_server = websockets.serve(cls.start_server, "127.0.0.1", 8765)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
        print('WS RUNNING')

    @classmethod
    def setUp(cls):
        print('SET UP TEST')

        thread = Thread(
            target=cls.startup_server,
            daemon=True
        )
        thread.start()

        xumm.env = 'sandbox'
        cls.sdk = xumm.XummSdk(
            cls.json_fixtures['api']['key'],
            cls.json_fixtures['api']['secret']
        )
        
        print('SDK INIT')

    def tearDown(cls):
        print('TEAR DOWN TEST')
        # print(ee)

    def _test_callback_promise_result(cls):
        callback_promise = CallbackPromise()
        callback_promise._resolve({'data': 'something'})
        cls.assertEqual(callback_promise.data, {'data': 'something'})
        cls.assertEqual(callback_promise.error, None)

    def _test_callback_promise_reject(cls):
        callback_promise = CallbackPromise()
        callback_promise._reject(APIError('Invalid Rejection'))
        cls.assertEqual(callback_promise.data, None)
        cls.assertEqual(str(callback_promise.error), 'Invalid Rejection')

    def _test_callback_promise_await(cls):
        callback_promise = CallbackPromise()

        async def run_pass(cb: CallbackPromise = None):
            result = await cb._resolved()
            cls.assertEqual(result, {'data': 'something'})

        callback_promise._resolve({'data': 'something'})
        asyncio.run(run_pass(callback_promise))

        async def run_fail(cb: CallbackPromise = None):
            result = await cb._resolved()
            cls.assertEqual(result, None)

        callback_promise._reject(APIError('Invalid Rejection'))
        asyncio.run(run_fail(callback_promise))

    @patch('xumm.client.requests.get')
    async def _test_payload_subscribe_inner(cls, mock_get):
        print('should susbscribe & resolve using inner resolve method @ callback')

        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['payload']['get']
        def callback_func(event):
            if 'signed' in event['data']:
                return event['resolve'](event['data'])

        subscription_socket = await cls.sdk.payload.subscribe(
            '0ef943e9-18ae-4fa2-952a-6f55dce363f0',
            callback_func,
        )

        test_dict = {
            'payload': subscription_socket.payload.to_dict(),
            'resolve': type(subscription_socket.resolve).__name__,
            'resolved': type(subscription_socket.resolved).__name__,
            'websocket': type(subscription_socket.websocket).__name__,
        }

        cls.assertEqual(test_dict, {
            'payload': cls.json_fixtures['payload']['get'],
            'resolve': 'method',
            'resolved': 'method',
            'websocket': WSClient.__name__,
        })

        cls.assertEqual(subscription_socket.websocket.status(), 101)
        cls.assertEqual(await subscription_socket.resolved(), test_fixtures.subscription_updates()['rejected'])
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))
        time.sleep(3)


    @patch('xumm.client.requests.get')
    async def _test_payload_subscribe_return(cls, mock_get):
        print('should susbscribe & resolve using return @ callback')
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['payload']['get']

        def received_ws_message(event):
            global COUNT
            COUNT = COUNT + 1

        subscription_socket = await cls.sdk.payload.subscribe(
            '0ef943e9-18ae-4fa2-952a-6f55dce363f0',
            received_ws_message,
        )

        test_dict = {
            'payload': subscription_socket.payload.to_dict(),
            'resolve': type(subscription_socket.resolve).__name__,
            'resolved': type(subscription_socket.resolved).__name__,
            'websocket': type(subscription_socket.websocket).__name__,
        }

        cls.assertEqual(test_dict, {
            'payload': cls.json_fixtures['payload']['get'],
            'resolve': 'method',
            'resolved': 'method',
            'websocket': WSClient.__name__,
        })

        cls.assertEqual(subscription_socket.websocket.status(), 101)
        # cls.assertEqual(COUNT, 3)
        subscription_socket.resolve({'dummyObject': True})
        cls.assertEqual(await subscription_socket.resolved(), {'dummyObject': True})
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))
        time.sleep(3)


    @patch('xumm.client.requests.get')
    @patch('xumm.client.requests.post')
    async def _test_payload_create_subscribe_inner(cls, mock_post, mock_get):
        print('should create, susbscribe & resolve using inner @ callback')
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = cls.json_fixtures['payload']['created']
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['payload']['get']

        def callback_func(event):
            if 'signed' in event['data']:
                return event['resolve'](event['data']) # FIX

        subscription_socket = await cls.sdk.payload.subscribe(
            '0ef943e9-18ae-4fa2-952a-6f55dce363f0',
            callback_func,
        )

        test_dict = {
            'payload': subscription_socket.payload.to_dict(),
            'resolve': type(subscription_socket.resolve).__name__,
            'resolved': type(subscription_socket.resolved).__name__,
            'websocket': type(subscription_socket.websocket).__name__,
        }

        cls.assertEqual(test_dict, {
            'payload': cls.json_fixtures['payload']['get'],
            'resolve': 'method',
            'resolved': 'method',
            'websocket': WSClient.__name__,
        })

        cls.assertEqual(subscription_socket.websocket.status(), 101)
        cls.assertEqual(await subscription_socket.resolved(), test_fixtures.subscription_updates()['rejected'])
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))
        time.sleep(3)


    @patch('xumm.client.requests.get')
    @patch('xumm.client.requests.post')
    async def _test_payload_create_subscribe_return(cls, mock_post, mock_get):
        print('should create, susbscribe & resolve using return @ callback')

        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = cls.json_fixtures['payload']['created']
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['payload']['get']

        def callback_func(event):
            if 'signed' in event['data']:
                return event['resolve'](event['data'])

        subscription_socket = await cls.sdk.payload.subscribe(
            '0ef943e9-18ae-4fa2-952a-6f55dce363f0',
            callback_func,
        )

        test_dict = {
            'payload': subscription_socket.payload.to_dict(),
            'resolve': type(subscription_socket.resolve).__name__,
            'resolved': type(subscription_socket.resolved).__name__,
            'websocket': type(subscription_socket.websocket).__name__,
        }

        cls.assertEqual(test_dict, {
            'payload': cls.json_fixtures['payload']['get'],
            'resolve': 'method',
            'resolved': 'method',
            'websocket': WSClient.__name__,
        })

        cls.assertEqual(subscription_socket.websocket.status(), 101)
        cls.assertEqual(await subscription_socket.resolved(), test_fixtures.subscription_updates()['rejected'])
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))
        time.sleep(3)

    async def _test_payload_subscribe(cls):

        await asyncio.sleep(3)

        await cls._test_payload_subscribe_inner()

        await cls._test_payload_subscribe_return()

        await cls._test_payload_create_subscribe_inner()

        await cls._test_payload_create_subscribe_return()

        return True


    def test_ws_tests(cls):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(cls._test_payload_subscribe())
        loop.close()
