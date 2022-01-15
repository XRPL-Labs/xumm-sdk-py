import os
import json
import time
from testing_config import BaseTestConfig
from tests.fixtures import xumm_api as test_fixtures
from unittest.mock import Mock, patch

import asyncio

class TestPayloadSubscribe(BaseTestConfig):

    def test_payload_subscribe(cls):
        asyncio.run(cls._test_payload_subscribe())

    @patch('xumm.client.requests.get')
    async def _test_payload_subscribe(cls, mock_get):
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

        cls.assertEqual(subscription_socket.websocket.sock.getstatus(), 101)
        cls.assertEqual(await subscription_socket.resolved(), test_fixtures.subscription_updates()['rejected'])
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))

    def test_payload_create_subscribe(cls):
        asyncio.run(cls._test_payload_create_subscribe())

    @patch('xumm.client.requests.get')
    @patch('xumm.client.requests.post')
    async def _test_payload_create_subscribe(cls, mock_post, mock_get):
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

        # cls.assertEqual(subscription_socket.websocket.sock.getstatus(), 101)
        # cls.assertEqual(await subscription_socket.resolved(), test_fixtures.subscription_updates()['rejected'])
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))

