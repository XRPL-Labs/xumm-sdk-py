import os
import json
import time
from testing_config import BaseTestConfig
from tests.fixtures import (
    xumm_api as test_fixtures,
)
from tests.fixtures.xumm_ws import main as ws_main
from unittest.mock import Mock, patch
from xumm.ws_client import WSClient
from typing import Callable

import xumm
import asyncio

import pytest
@pytest.mark.skip(reason="Using Prod Cert")
class TestPayloadSubscribe(BaseTestConfig):

    @classmethod
    def setUp(cls):
        print('SET UP TEST')
        xumm.api_key = cls.json_fixtures['api']['key']
        xumm.api_secret = cls.json_fixtures['api']['secret']
        cls.sdk = xumm.XummSdk()
        # asyncio.run(ws_main())

    def tearDown(cls):
        print('TEAR DOWN TEST')

    # @pytest.mark.skip(reason="Using Prod Cert")
    def test_payload_subscribe_inner(cls):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(cls._test_payload_subscribe_inner())

    @patch('xumm.client.requests.get')
    async def _test_payload_subscribe_inner(cls, mock_get):
        print('should susbscribe & resolve using inner resolve method @ callback')
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['payload']['get']
        async def callback_func(event):
            if 'signed' in event['data']:
                return event['resolve'](event['data']) # FIX

        cls.sdk.payload.mock = True
        subscription_socket = await cls.sdk.payload.subscribe(
            '0ef943e9-18ae-4fa2-952a-6f55dce363f0',
            callback_func,
        )

        # print(subscription_socket.resolve)

        test_dict = {
            # 'payload': subscription_socket.payload.to_dict(),
            # 'resolve': subscription_socket.resolve,
            # 'resolved': subscription_socket.resolved,
            'websocket': type(subscription_socket.websocket).__name__,
        }

        # print(type(subscription_socket.resolved).__name__)
        # print(Callable.__name__)

        cls.assertEqual(test_dict, {
            # 'payload': cls.json_fixtures['payload']['get'],
            # 'resolve': isinstance(subscription_socket.resolve, Callable),
            # 'resolved': isinstance(subscription_socket.resolved, Callable),
            'websocket': WSClient.__name__,
        })

        print(await subscription_socket.resolved())

        # cls.assertEqual(subscription_socket.websocket.status(), 101)
        # cls.assertEqual(await subscription_socket.resolved(), test_fixtures.subscription_updates()['rejected'])
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))
    
    # @pytest.mark.skip(reason="Using Prod Cert")
    def test_payload_subscribe_return(cls):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(cls._test_payload_subscribe_return())

    @patch('xumm.client.requests.get')
    async def _test_payload_subscribe_return(cls, mock_get):
        print('should susbscribe & resolve using return @ callback')
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['payload']['get']
        def callback_func(event):
            if 'signed' in event['data']:
                return event['resolve'](event['data']) # FIX

        subscription_socket = await cls.sdk.payload.subscribe(
            '0ef943e9-18ae-4fa2-952a-6f55dce363f0',
            callback_func,
        )

        # expect(subscriptionSocket).toMatchObject({
        #     payload: jsonFixtures.payload.get,
        #     resolve: expect.any(Function),
        #     resolved: expect.any(Promise),
        #     websocket: expect.any(MockedWebSocket)
        # })

        # cls.assertEqual(subscription_socket.websocket.sock.getstatus(), 101)

        received_messages = 0
        # subscription_socket.websocket.onmessage = () => receivedWsMessages++

        # time.sleep(1)

        # setTimeout(() => {
        #     subscriptionSocket.resolve({dummyObject: true})
        #     expect(receivedWsMessages).toEqual(3)
        # }, 500)

        # subscription_socket.resolve({'dummyObject': True})
        # cls.assertEqual(len(received_messages), 3)
        # expect(received_messages).toEqual(3)

        # cls.assertEqual(await subscription_socket.resolved(), {'dummyObject': True})
        # expect(await subscriptionSocket.resolved).toMatchObject({dummyObject: true})
        
        # TODO: Unknown
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))

    # @pytest.mark.skip(reason="Using Prod Cert")
    def test_payload_create_subscribe_inner(cls):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(cls._test_payload_create_subscribe_inner())

    @patch('xumm.client.requests.get')
    @patch('xumm.client.requests.post')
    async def _test_payload_create_subscribe_inner(cls, mock_post, mock_get):
        print('should create, susbscribe & resolve using return @ callback')
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

        # expect(subscriptionSocket).toMatchObject({
        #     payload: jsonFixtures.payload.get,
        #     resolve: expect.any(Function),
        #     resolved: expect.any(Promise),
        #     websocket: expect.any(MockedWebSocket)
        # })

        # cls.assertEqual(subscription_socket.websocket.sock.getstatus(), 101)
        # cls.assertEqual(await subscription_socket.resolved(), test_fixtures.subscription_updates()['rejected'])
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))

    # @pytest.mark.skip(reason="Using Prod Cert")
    def test_payload_create_subscribe_return(cls):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(cls._test_payload_create_subscribe_return())

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
                return event['resolve'](event['data']) # FIX

        subscription_socket = await cls.sdk.payload.subscribe(
            '0ef943e9-18ae-4fa2-952a-6f55dce363f0',
            callback_func,
        )

        # expect(subscriptionSocket).toMatchObject({
        #     payload: jsonFixtures.payload.get,
        #     resolve: expect.any(Function),
        #     resolved: expect.any(Promise),
        #     websocket: expect.any(MockedWebSocket)
        # })

        # cls.assertEqual(subscription_socket.websocket.sock.getstatus(), 101)
        # cls.assertEqual(await subscription_socket.resolved(), test_fixtures.subscription_updates()['rejected'])
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))

