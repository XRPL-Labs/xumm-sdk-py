#!/usr/bin/env python
# coding: utf-8

from testing_config import BaseTestConfig
from unittest.mock import Mock, patch

from xumm.resource.types import (
    XummPushEventRequest,
)

import xumm

class TestXapp(BaseTestConfig):

    token: str = ''

    @classmethod
    def setUp(cls):
        xumm.api_key = cls.json_fixtures['api']['key']
        xumm.api_secret = cls.json_fixtures['api']['secret']
        cls.sdk = xumm.XummSdk()

    @patch('xumm.client.requests.post')
    def test_push_event(cls, mock_post):
        print('should set push event')
        
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = cls.json_fixtures['xApp']['event']
        
        payload: XummPushEventRequest = XummPushEventRequest(
            user_token='',
            body='',
        )
        result = cls.sdk.push.event(payload)
        cls.assertEqual(result.to_dict(), cls.json_fixtures['xApp']['event'])

    @patch('xumm.client.requests.post')
    def test_push_push(cls, mock_post):
        print('should set push event')
        
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = cls.json_fixtures['xApp']['push']
        
        payload: XummPushEventRequest = XummPushEventRequest(
            user_token='',
            body='',
        )
        result = cls.sdk.push.push(payload)
        cls.assertEqual(result.to_dict(), cls.json_fixtures['xApp']['push'])