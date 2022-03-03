import pytest
from testing_config import BaseTestConfig

from xumm.resource.types import (
    XummWebhookBody
)

class TestXummApiTypes(BaseTestConfig):

    def test_webhook_body(cls):
        print('should set on webhook body')

        dict = {
            'meta': cls.json_fixtures['webhook']['meta'],
            'custom_meta': cls.json_fixtures['webhook']['custom_meta'],
            'payloadResponse': cls.json_fixtures['webhook']['payloadResponse'],
            # 'userToken': cls.json_fixtures['webhook']['userToken'],  # Can be null
        }
        cls.assertEqual(XummWebhookBody(**dict).to_dict(), dict)
    
    def test_webhook_body_fail(cls):
        print('should fail to set webhook body')

        dict = {
            'meta': cls.json_fixtures['webhook']['meta'],
            'custom_meta': cls.json_fixtures['webhook']['custom_meta'],
            'payloadResponse': cls.json_fixtures['webhook']['payloadResponse'],
            'userToken': cls.json_fixtures['webhook']['userToken'],
        }
        dict['payloadResponse']['txid'] = None
        
        with pytest.raises(ValueError, match=r'Invalid value for `txid`, must not be `None`'):
            XummWebhookBody(**dict)
            cls.fail("XummWebhookBody: raised Exception unexpectedly!")