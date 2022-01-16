import os
import json
import time
from testing_config import BaseTestConfig
from tests.fixtures import (
    xumm_api as test_fixtures,
    xumm_ws,
)
from unittest.mock import Mock, patch

import asyncio

import pytest
@pytest.mark.skip(reason="Using Prod Cert")
class TestPayloadSubscribe(BaseTestConfig):

    # def setUp(cls):
    #     print('SET UP TEST')
    #     asyncio.run(xumm_ws.start())

    # def tearDown(cls):
    #     print('TEAR DOWN TEST')

    def test_payload_subscribe_inner(cls):
        asyncio.run(cls._test_payload_subscribe_inner())

    @patch('xumm.client.requests.get')
    async def _test_payload_subscribe_inner(cls, mock_get):
        print('should susbscribe & resolve using inner resolve method @ callback')
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['payload']['get']
        def callback_func(event):
            if 'signed' in event['data']:
                return event['resolve'](event['data']) # FIX

        subscription_socket = await cls.ws_sdk.subscribe(
            cls.sdk,
            '0ef943e9-18ae-4fa2-952a-6f55dce363f0',
            callback_func,
        )

        # expect(subscriptionSocket).toMatchObject({
        #     payload: jsonFixtures.payload.get,
        #     resolve: expect.any(Function),
        #     resolved: expect.any(Promise),
        #     websocket: expect.any(MockedWebSocket)
        # })

        cls.assertEqual(subscription_socket.websocket.sock.getstatus(), 101)
        cls.assertEqual(await subscription_socket.resolved(), test_fixtures.subscription_updates()['rejected'])
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))
    
    def test_payload_subscribe_return(cls):
        asyncio.run(cls._test_payload_subscribe_return())

    @patch('xumm.client.requests.get')
    async def _test_payload_subscribe_return(cls, mock_get):
        print('should susbscribe & resolve using return @ callback')
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['payload']['get']
        def callback_func(event):
            if 'signed' in event['data']:
                return event['resolve'](event['data']) # FIX

        subscription_socket = await cls.ws_sdk.subscribe(
            cls.sdk,
            '0ef943e9-18ae-4fa2-952a-6f55dce363f0',
            callback_func,
        )

        # expect(subscriptionSocket).toMatchObject({
        #     payload: jsonFixtures.payload.get,
        #     resolve: expect.any(Function),
        #     resolved: expect.any(Promise),
        #     websocket: expect.any(MockedWebSocket)
        # })

        cls.assertEqual(subscription_socket.websocket.sock.getstatus(), 101)

        received_messages = 0
        # subscription_socket.websocket.onmessage = () => receivedWsMessages++

        time.sleep(1)

        # setTimeout(() => {
        #     subscriptionSocket.resolve({dummyObject: true})
        #     expect(receivedWsMessages).toEqual(3)
        # }, 500)

        subscription_socket.resolve({'dummyObject': True})
        cls.assertEqual(len(received_messages), 3)
        # expect(received_messages).toEqual(3)

        cls.assertEqual(await subscription_socket.resolved(), {'dummyObject': True})
        # expect(await subscriptionSocket.resolved).toMatchObject({dummyObject: true})
        
        # TODO: Unknown
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))

    def test_payload_create_subscribe_inner(cls):
        asyncio.run(cls._test_payload_create_subscribe_inner())

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

        subscription_socket = await cls.ws_sdk.subscribe(
            cls.sdk,
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

    def test_payload_create_subscribe_return(cls):
        asyncio.run(cls._test_payload_create_subscribe_return())

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

        subscription_socket = await cls.ws_sdk.subscribe(
            cls.sdk,
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

