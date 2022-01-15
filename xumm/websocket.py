import asyncio
import json
import time
import websockets
from random import random
from uuid import uuid4
import logging

logger = logging.getLogger(__name__)




class WebsocketConnect:

    # def __init__(cls, uri, payload, consumer):
    #     asyncio.run(cls.connect(uri, payload, consumer))

    async def connect(cls, uri, payload, consumer):
        # websocket = await websockets.connect(uri, ssl=True)
        websocket = await websockets.connect(uri)
        await websocket.send(json.dumps(payload))
        while True:
            if not websocket.open:
                try:
                    print('Websocket is NOT connected. Reconnecting...')
                    websocket = await websockets.connect(uri)
                    await websocket.send(json.dumps(payload))
                except:
                    print('Unable to reconnect, trying again.')
            try:
                async for message in websocket:
                    if message is not None:
                        consumer(json.loads(message))

                print('NOTHING FOUND')
            except:
                print('Error receiving message from websocket.')


class ConnectWebsocket:
    MAX_RECONNECTS = 5
    MAX_RECONNECT_SECONDS = 60

    def __init__(cls, loop, uuid, callback):
        cls._loop = loop
        cls._callback = callback
        cls._reconnect_num = 0
        cls._ws_details = {
            'uuid': uuid,
            'tester': True,
        }
        cls._connect_id = None
        cls._last_ping = None
        cls._socket = None
        # cls._topics = []
        asyncio.ensure_future(cls.run_forever(), loop=cls._loop)

    # @property
    # def topics(cls):
    #     return cls._topics

    async def _run(cls, event: asyncio.Event):
        keep_alive = True
        cls._last_ping = time.time()  # record last ping
        # cls._ws_details = None
        # logger.debug(cls._ws_details)

        # async with websockets.connect(cls.get_ws_endpoint(), ssl=cls.get_ws_encryption()) as socket:
        async with websockets.connect(cls.get_ws_endpoint()) as socket:
            cls._socket = socket
            cls._reconnect_num = 0

            print('EVENT SET: {}'.format(event.is_set()))
            if not event.is_set():
                print('PING: 1')
                await cls.send_ping()
                event.set()

            while keep_alive:
                # print('TIME TIME: {}'.format(time.time()))
                # print('LAST PING: {}'.format(cls._last_ping))
                # print('WS PING TIMEOUT: {}'.format(cls.get_ws_pingtimeout()))
                # print(time.time() - cls._last_ping)
                # print(cls.get_ws_pingtimeout())
                # if time.time() - cls._last_ping > cls.get_ws_pingtimeout():
                #     print('PING: 2')
                #     await cls.send_ping()
                try:
                    _msg = await asyncio.wait_for(cls._socket.recv(), timeout=cls.get_ws_pingtimeout())
                except asyncio.TimeoutError:
                    print('TimeoutError')
                    await cls.send_ping()
                except asyncio.CancelledError:
                    print('CancelledError')
                    await cls._socket.ping()
                else:
                    try:
                        msg = json.loads(_msg)
                    except ValueError:
                        logger.warning(_msg)
                    else:
                        await cls._callback({})

    def get_ws_endpoint(cls):
        if not cls._ws_details['uuid']:
            raise Exception("Websocket details Error: uuid")

        if cls._ws_details['tester']:
            return 'ws://localhost:8765'
        
        return 'wss://xumm.app/sign/' + cls._uuid

    def get_ws_encryption(cls):
        if not cls._ws_details:
            raise Exception("Websocket details Error")
        return cls._ws_details['instanceServers'][0]['encrypt']

    def get_ws_pingtimeout(cls):
        # if not cls._ws_details:
        #     raise Exception("Websocket details Error")
        # _timeout = int(cls._ws_details['instanceServers'][0]['pingTimeout'] / 1000) - 2
        _timeout = 30000 / 1000
        return _timeout

    async def run_forever(cls):
        while True:
            await cls._reconnect()

    async def _reconnect(cls):
        print('Websocket start connect/reconnect')

        cls._reconnect_num += 1
        reconnect_wait = cls._get_reconnect_wait(cls._reconnect_num)
        # print(f'asyncio sleep reconnect_wait={reconnect_wait} s reconnect_num={cls._reconnect_num}')
        await asyncio.sleep(reconnect_wait)
        print(f'asyncio sleep ok')
        event = asyncio.Event()

        tasks = {
            asyncio.ensure_future(cls._recover_req_msg(event), loop=cls._loop): cls._recover_req_msg,
            asyncio.ensure_future(cls._run(event), loop=cls._loop): cls._run
        }

        while set(tasks.keys()):
            finished, pending = await asyncio.wait(tasks.keys(), return_when=asyncio.FIRST_EXCEPTION)
            exception_occur = False
            for task in finished:
                if task.exception():
                    exception_occur = True
                    # logger.warning("{} got an exception {}".format(task, task.exception()))
                    for pt in pending:
                        # logger.warning(f'pending {pt}')
                        try:
                            pt.cancel()
                        except asyncio.CancelledError:
                            logger.exception('CancelledError ')
                        logger.warning('cancel ok.')

            if exception_occur:
                break

        logger.warning('_reconnect over.')

    async def _recover_req_msg(cls, event):
        # print(f'recover topic event {cls.topics} waiting')
        await event.wait()
        event.set()
        # print(f'recover topic event {cls.topics} done.')
        # for topic in cls.topics:
        print('RESPONSE MESSAGE')
        # print(await event.data)
        # await cls.send_message({
        #     'type': 'subscribe',
        #     # 'topic': topic,
        #     'response': True
        # })
        # print(f'{topic} OK')

    def _get_reconnect_wait(cls, attempts):
        expo = 2 ** attempts
        return round(random() * min(cls.MAX_RECONNECT_SECONDS, expo - 1) + 1)

    async def send_ping(cls):
        msg = {
            'id': str(int(time.time() * 1000)),
            'type': 'ping'
        }
        await cls._socket.send(json.dumps(msg))
        cls._last_ping = time.time()

    async def send_message(cls, msg, retry_count=0):
        print('SENDING MSG: {}'.format(msg))
        if not cls._socket:
            if retry_count < cls.MAX_RECONNECTS:
                await asyncio.sleep(1)
                await cls.send_message(msg, retry_count + 1)
        else:
            msg['id'] = str(int(time.time() * 1000))
            await cls._socket.send(json.dumps(msg))

