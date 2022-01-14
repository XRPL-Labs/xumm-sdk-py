import os
import json
from testing_config import BaseTestConfig
from tests.fixtures import xumm_api as test_fixtures
from unittest.mock import Mock, patch

import xumm

class TestXummSDKPayloadCreate(BaseTestConfig):

    @patch('xumm.client.requests.post')
    def test_payload_create(cls, mock_post):
        print('should create a simple payment')
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = cls.json_fixtures['payload']['created']
        result = cls.sdk.payload_create(test_fixtures.valid_payload())
        cls.assertEqual(result.to_dict(), cls.json_fixtures['payload']['created'])
    
    @patch('xumm.client.requests.post')
    def test_payload_create_unwrapped(cls, mock_post):
        print('should create a simple payment based on only (unwrapped payload) TX Json')
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = cls.json_fixtures['payload']['created']
        result = cls.sdk.payload_create(test_fixtures.valid_payload()['txjson'])
        cls.assertEqual(result.to_dict(), cls.json_fixtures['payload']['created'])

    @patch('xumm.client.requests.post')
    def test_payload_create_invalid_null(cls, mock_post):
        print('should return null on invalid payload')

        mock_post.return_value = Mock(status_code=400)
        mock_post.return_value.json.return_value = cls.json_fixtures['payload']['error']

        try:
            cls.sdk.payload_create(test_fixtures.invalid_payload())
            cls.fail("payload_create() raised Exception unexpectedly!")
        except Exception as e:
            cls.assertEqual(e.error['reference'], cls.json_fixtures['payload']['error']['error']['reference'])
            cls.assertEqual(e.error['code'], cls.json_fixtures['payload']['error']['error']['code'])
            # cls.assertEqual(e.error['message'], cls.json_fixtures['payload']['error']['error']['message'])

    @patch('xumm.client.requests.post')
    def test_payload_create_invalid_errors(cls, mock_post):
        print('should throw on invalid payload with `returnErrors`')

        mock_post.return_value = Mock(status_code=400)
        mock_post.return_value.json.return_value = cls.json_fixtures['payload']['error']

        try:
            cls.sdk.payload_create(test_fixtures.invalid_payload())
            cls.fail("payload_create() raised Exception unexpectedly!")
        except Exception as e:
            cls.assertEqual(e.error['reference'], cls.json_fixtures['payload']['error']['error']['reference'])
            cls.assertEqual(e.error['code'], cls.json_fixtures['payload']['error']['error']['code'])
            # cls.assertEqual(e.error['message'], cls.json_fixtures['payload']['error']['error']['message'])
