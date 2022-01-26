import os
import json
import time
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
            # on_response=on_message,
            # on_error=on_error,
            # on_close=on_close,
            # on_open=on_open
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

        # websocket_conn = WSClient(
        #     server='ws://localhost:8765',  # noqa: E501
        #     # on_response=on_message,
        #     # on_error=on_error,
        #     # on_close=on_close,
        #     # on_open=on_open
        # )

        dict = {
            'payload': cls.json_fixtures['payload']['get'],
            'resolve': resolve_callback,
            'resolved': resolved_callback,
            'websocket': None,  # FAILS
        }
        try:
            PayloadSubscription(**dict)
            cls.fail("PayloadAndSubscription: raised Exception unexpectedly!")
        except Exception as e:
            cls.assertEqual(str(e), "Invalid value for `websocket`, must not be `None`")