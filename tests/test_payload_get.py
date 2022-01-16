import os
import json
from testing_config import BaseTestConfig
from tests.fixtures import xumm_api as test_fixtures
from unittest.mock import Mock, patch

import xumm

class TestPayloadGet(BaseTestConfig):

    @classmethod
    def setUp(cls):
        xumm.api_key = cls.json_fixtures['api']['key']
        xumm.api_secret = cls.json_fixtures['api']['secret']
        cls.sdk = xumm.XummSdk()
        cls.ws_sdk = xumm.XummWs()

    @patch('xumm.client.requests.get')
    def test_payload_get(cls, mock_post):
        print('should get a simple payment')
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = cls.json_fixtures['payload']['get']
        result = cls.sdk.payload_get('00000000-0000-4839-af2f-f794874a80b0')
        cls.assertEqual(result.to_dict(), cls.json_fixtures['payload']['get'])
    
    @patch('xumm.client.requests.get')
    @patch('xumm.client.requests.post')
    def test_payload_create_cancel(cls, mock_post, mock_delete):
        print('should get a payload by Created Payload')

        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = cls.json_fixtures['payload']['created']

        created_payload = cls.sdk.payload_create(test_fixtures.valid_payload())
        if created_payload:
            mock_delete.return_value = Mock(status_code=200)
            mock_delete.return_value.json.return_value = cls.json_fixtures['payload']['get']
            cls.assertEqual(cls.sdk.payload_get(created_payload.uuid).to_dict(), cls.json_fixtures['payload']['get'])

    @patch('xumm.client.requests.get')
    def test_payload_get_invalid_null(cls, mock_get):
        print('should null on getting an invalid/non existent payload')

        mock_get.return_value = Mock(status_code=400)
        mock_get.return_value.json.return_value = cls.json_fixtures['payload']['notfound']

        try:
            cls.sdk.payload_get('00000000-0000-4839-af2f-f794874a80b0')
            cls.fail("payload_get() raised Exception unexpectedly!")
        except Exception as e:
            cls.assertEqual(e.error['reference'], cls.json_fixtures['payload']['notfound']['error']['reference'])
            cls.assertEqual(e.error['code'], cls.json_fixtures['payload']['notfound']['error']['code'])
            # cls.assertEqual(e.error['message'], cls.json_fixtures['payload']['error']['error']['message'])

    @patch('xumm.client.requests.get')
    def test_payload_get_invalid_errors(cls, mock_get):
        print('should throw on getting an invalid/non existent payload with `returnErrors`')

        mock_get.return_value = Mock(status_code=400)
        mock_get.return_value.json.return_value = cls.json_fixtures['payload']['notfound']

        try:
            cls.sdk.payload_get('00000000-0000-4839-af2f-f794874a80b0')
            cls.fail("payload_get() raised Exception unexpectedly!")
        except Exception as e:
            cls.assertEqual(e.error['reference'], cls.json_fixtures['payload']['notfound']['error']['reference'])
            cls.assertEqual(e.error['code'], cls.json_fixtures['payload']['notfound']['error']['code'])
            # cls.assertEqual(e.error['message'], cls.json_fixtures['payload']['error']['error']['message'])
