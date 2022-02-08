import time
import pytest

from testing_config import BaseTestConfig

from xumm.ws_client import WSClient
from xumm.resource.types import (
    PayloadAndSubscription
)

def resolve_callback(*args):
    print('CALLING BACK')
    resolved_callback(args)

def resolved_callback(*args):
    print('CALLING BACK')
    time.sleep(3)
    return args

class TestPayloadAndSubscription(BaseTestConfig):

    def test_payload_and_subscription(cls):
        print('should set subscription w/created response')

        websocket_conn = WSClient(
            server='ws://localhost:8765',  # noqa: E501
            # on_response=on_message,
            # on_error=on_error,
            # on_close=on_close,
            # on_open=on_open
        )

        dict = {
            'created': cls.json_fixtures['payload']['created'],
            'payload': cls.json_fixtures['payload']['get'],
            'resolve': resolve_callback,
            'resolved': resolved_callback,
            'websocket': websocket_conn,
        }
        cls.assertEqual(PayloadAndSubscription(**dict).to_dict(), dict)
    
    def test_payload_and_subscription_fail(cls):
        print('should fail to set subscription w/created response')

        websocket_conn = WSClient(
            server='ws://localhost:8765',  # noqa: E501
            # on_response=on_message,
            # on_error=on_error,
            # on_close=on_close,
            # on_open=on_open
        )

        dict = {
            'created': None,  # FAILS
            'payload': cls.json_fixtures['payload']['get'],
            'resolve': resolve_callback,
            'resolved': resolved_callback,
            'websocket': websocket_conn,
        }
        
        with pytest.raises(TypeError, match=r'argument after \*\* must be a mapping, not NoneType'):
            PayloadAndSubscription(**dict)
            cls.fail("PayloadAndSubscription: raised Exception unexpectedly!")