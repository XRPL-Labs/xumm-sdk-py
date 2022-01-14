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


    def test_payload_create_cancel(cls):
        print('should cancel a payload by Created Payload')
        created_payload = cls.sdk.payload_create(test_fixtures.valid_payload())
        result = cls.sdk.payload_cancel(created_payload.uuid)
        cls.assertEqual(result.to_dict(), cls.json_fixtures['payload']['cancelled'])

    # def _test_payload_get_cancel(cls):
    #     print('should cancel a payload by Fetched Payload')
    #     payloadId = '00000000-0000-4839-af2f-f794874a80b0'
    #     get_payload = PayloadApi(cls.sdk).payload_get(payloadId)
    #     result = PayloadApi(cls.sdk).payload_delete(get_payload.uuid)
    #     cls.assertEqual(result.to_dict(), cls.json_fixtures['payload']['cancelled'])
