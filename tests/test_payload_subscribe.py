#!/usr/bin/env python
# coding: utf-8

import time
import json
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

from threading import Thread


# import pytest
# @pytest.mark.skip(reason="Using Prod Cert")
class TestPayloadSubscribe(BaseTestConfig):

    @classmethod
    def setUp(cls):
        print('SET UP TEST')
        xumm.env = 'sandbox'
        cls.sdk = xumm.XummSdk(
            cls.json_fixtures['api']['key'],
            cls.json_fixtures['api']['secret']
        )

    def tearDown(cls):
        print('TEAR DOWN TEST')

    @patch('xumm.client.requests.get')
    async def _test_payload_subscribe_inner(cls, mock_get):
        print('should susbscribe & resolve using inner resolve method @ callback')
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

        # cls.assertEqual(subscription_socket.websocket.status(), 101)
        cls.assertEqual(await subscription_socket.resolved(), test_fixtures.subscription_updates()['rejected'])
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))
        cls.sdk.payload.unsubscribe()

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

        # cls.assertEqual(subscription_socket.websocket.status(), 101)

        received_messages = 0

        def received_ws_message(received_messages=received_messages):
            received_messages += 1

        subscription_socket.websocket._on_message = received_ws_message

        time.sleep(1)
        subscription_socket.resolve({'dummyObject': True})
        # cls.assertEqual(received_messages, 3)
        cls.assertEqual(await subscription_socket.resolved(), {'dummyObject': True})
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))
        cls.sdk.payload.unsubscribe()

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

        # cls.assertEqual(subscription_socket.websocket.sock.getstatus(), 101)
        cls.assertEqual(await subscription_socket.resolved(), test_fixtures.subscription_updates()['rejected'])
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))
        cls.sdk.payload.unsubscribe()

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

        # cls.assertEqual(subscription_socket.websocket.sock.getstatus(), 101)
        cls.assertEqual(await subscription_socket.resolved(), test_fixtures.subscription_updates()['rejected'])
        # expect(wsEol).toEqual(expect.arrayContaining([subscriptionSocket.websocket.readyState]))
        cls.sdk.payload.unsubscribe()

    async def _test_payload_subscribe(cls, loop):

        def start_server():
            asyncio.run(ws_main())
        
        thread = Thread(target=start_server, daemon=True)
        thread.start()

        await asyncio.sleep(3)

        await cls._test_payload_subscribe_inner()

        await cls._test_payload_subscribe_return()

        await cls._test_payload_create_subscribe_inner()

        await cls._test_payload_create_subscribe_return()

        await asyncio.sleep(2)

        loop.call_soon_threadsafe(loop.stop)
        # thread.join()  # This doesnt work?
        raise ValueError(200)  # Do this beacuse the thread never comes back...

    def test_test_payload(cls):
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(cls._test_payload_subscribe(loop))
            loop.close()
        except Exception as e:
            cls.assertEqual(str(e), '200')


