#!/usr/bin/env python
# coding: utf-8
import pytest
from testing_config import BaseTestConfig
from tests.fixtures import xumm_api as test_fixtures
from unittest.mock import Mock, patch

import xumm

class TestPayloadCreate(BaseTestConfig):

    @classmethod
    def setUp(cls):
        cls.sdk = xumm.XummSdk(
            cls.json_fixtures['api']['key'],
            cls.json_fixtures['api']['secret']
        )

    @patch('xumm.client.requests.post')
    def test_payload_create(cls, mock_post):
        print('should create a simple payment')
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = cls.json_fixtures['payload']['created']
        result = cls.sdk.payload.create(test_fixtures.valid_payload())
        cls.assertEqual(result.to_dict(), cls.json_fixtures['payload']['created'])
    
    @patch('xumm.client.requests.post')
    def test_payload_create_unwrapped(cls, mock_post):
        print('should create a simple payment based on only (unwrapped payload) TX Json')
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = cls.json_fixtures['payload']['created']
        result = cls.sdk.payload.create(test_fixtures.valid_payload()['txjson'])
        cls.assertEqual(result.to_dict(), cls.json_fixtures['payload']['created'])

    @patch('xumm.client.requests.post')
    def test_payload_create_invalid_errors(cls, mock_post):
        print('should throw on invalid payload with `returnErrors`')

        mock_post.return_value = Mock(status_code=400)
        mock_post.return_value.json.return_value = cls.json_fixtures['payload']['error']

        with pytest.raises(xumm.error.InvalidRequestError, match=r"Error code 602, see XUMM Dev Console, reference: a61ba59a-0304-44ae-a86e-efefegewgew4"):
            cls.sdk.payload.create(test_fixtures.invalid_payload())
            cls.fail("payload_create() raised Exception unexpectedly!")

        
