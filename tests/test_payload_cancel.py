import os
import json
from testing_config import BaseTestConfig
from tests.fixtures import xumm_api as test_fixtures
from unittest.mock import Mock, patch

import xumm

class TestXummSDKPayloadCancel(BaseTestConfig):

    @patch('xumm.client.requests.delete')
    def test_payload_cancel(cls, mock_delete):
        print('should cancel a payload by UUID')
        payloadId = '00000000-0000-4839-af2f-f794874a80b0'

        mock_delete.return_value = Mock(status_code=200)
        mock_delete.return_value.json.return_value = cls.json_fixtures['payload']['cancelled']
        
        cls.assertEqual(cls.sdk.payload_cancel(payloadId).to_dict(), cls.json_fixtures['payload']['cancelled'])

    @patch('xumm.client.requests.delete')
    def test_payload_not_found_null(cls, mock_delete):
        print('should return numm if payload not found')
        payloadId = '00000000-0000-4839-af2f-f794874a80b0'

        mock_delete.return_value = Mock(status_code=404)
        mock_delete.return_value.json.return_value = cls.json_fixtures['payload']['notfound']

        try:
            cls.sdk.payload_cancel(payloadId)
            cls.fail("payload_cancel() raised Exception unexpectedly!")
        except Exception as e:
            cls.assertEqual(e.error['reference'], cls.json_fixtures['payload']['notfound']['error']['reference'])
            cls.assertEqual(e.error['code'], cls.json_fixtures['payload']['notfound']['error']['code'])
            # cls.assertEqual(response.error['message'], cls.json_fixtures['payload']['notfound']['error']['message'])

    @patch('xumm.client.requests.delete')
    def test_payload_not_found_errors(cls, mock_delete):
        print('should throw if payload not found with `returnErrors`')
        payloadId = '00000000-0000-4839-af2f-f794874a80b0'

        mock_delete.return_value = Mock(status_code=404)
        mock_delete.return_value.json.return_value = cls.json_fixtures['payload']['notfound']

        try:
            cls.sdk.payload_cancel(payloadId)
            cls.fail("payload_cancel() raised Exception unexpectedly!")
        except Exception as e:
            cls.assertEqual(e.error['reference'], cls.json_fixtures['payload']['notfound']['error']['reference'])
            cls.assertEqual(e.error['code'], cls.json_fixtures['payload']['notfound']['error']['code'])
            # cls.assertEqual(response.error['message'], cls.json_fixtures['payload']['notfound']['error']['message'])

    @patch('xumm.client.requests.delete')
    @patch('xumm.client.requests.post')
    def test_payload_create_cancel(cls, mock_post, mock_delete):
        print('should cancel a payload by Created Payload')

        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = cls.json_fixtures['payload']['created']

        created_payload = cls.sdk.payload_create(test_fixtures.valid_payload())
        if created_payload:
            mock_delete.return_value = Mock(status_code=200)
            mock_delete.return_value.json.return_value = cls.json_fixtures['payload']['cancelled']
            cls.assertEqual(cls.sdk.payload_cancel(created_payload.uuid).to_dict(), cls.json_fixtures['payload']['cancelled'])

    @patch('xumm.client.requests.delete')
    @patch('xumm.client.requests.get')
    def test_payload_get_cancel(cls, mock_get, mock_delete):
        print('should cancel a payload by Fetched Payload')
        payloadId = '00000000-0000-4839-af2f-f794874a80b0'
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['payload']['get']

        get_payload = cls.sdk.payload_get(payloadId)
        if get_payload:
            mock_delete.return_value = Mock(status_code=200)
            mock_delete.return_value.json.return_value = cls.json_fixtures['payload']['cancelled']
            cls.assertEqual(cls.sdk.payload_cancel(get_payload.meta.uuid).to_dict(), cls.json_fixtures['payload']['cancelled'])