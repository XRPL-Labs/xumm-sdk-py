import time
import pytest
from testing_config import BaseTestConfig

from xumm.ws_client import WSClient
from xumm.resource.types import (
    PayloadSubscription
)

def resolve_callback(*args):
    print('CALLING BACK')
    resolved_callback(args)

def resolved_callback(*args):
    print('CALLING BACK')
    time.sleep(3)
    return args

class TestPayloadSubscription(BaseTestConfig):

    def test_payload_subscription(cls):
        print('should set subscription response')

        websocket_conn = WSClient(
            server='ws://localhost:8765',  # noqa: E501
        )

        dict = {
            'payload': cls.json_fixtures['payload']['get'],
            'resolve': resolve_callback,
            'resolved': resolved_callback,
            'websocket': websocket_conn,
        }
        cls.assertEqual(PayloadSubscription(**dict).to_dict(), dict)
    
    def test_payload_subscription_fail(cls):
        print('should fail to set subscription response')

        dict = {
            'payload': cls.json_fixtures['payload']['get'],
            'resolve': resolve_callback,
            'resolved': resolved_callback,
            'websocket': None,  # FAILS
        }

        with pytest.raises(ValueError, match=r'Invalid value for `websocket`, must not be `None`'):
            PayloadSubscription(**dict)
            cls.fail("PayloadAndSubscription: raised Exception unexpectedly!")
   
            
 