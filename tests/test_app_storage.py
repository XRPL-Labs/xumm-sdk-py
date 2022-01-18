import os
import json
from testing_config import BaseTestConfig
from tests.fixtures import xumm_api as test_fixtures
from unittest.mock import Mock, patch

import xumm

class TestAppStorage(BaseTestConfig):

    @classmethod
    def setUp(cls):
        xumm.api_key = cls.json_fixtures['api']['key']
        xumm.api_secret = cls.json_fixtures['api']['secret']
        cls.sdk = xumm.XummSdk()

    @patch('xumm.client.requests.post')
    def test_storage_set(cls, mock_post):
        print('should set app storage')
        
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = cls.json_fixtures['storage']['setResponse']
        result = cls.sdk.storage.set({'name': 'Wietse'})
        cls.assertEqual(result.to_dict(), cls.json_fixtures['storage']['setResponse'])
    
    @patch('xumm.client.requests.get')
    def test_storage_get(cls, mock_get):
        print('should get app storage')

        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['storage']['getResponse']
        cls.assertEqual(cls.sdk.storage.get().to_dict(), cls.json_fixtures['storage']['getResponse'])

    @patch('xumm.client.requests.delete')
    def test_storage_delete(cls, mock_delete):
        print('should clear app storage')

        mock_delete.return_value = Mock(status_code=200)
        mock_delete.return_value.json.return_value = cls.json_fixtures['storage']['deleteResponse']
        cls.assertEqual(cls.sdk.storage.delete().to_dict(), cls.json_fixtures['storage']['deleteResponse'])