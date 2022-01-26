import os
import json
from testing_config import BaseTestConfig

from xumm.resource.types import (
    SubscriptionCallbackParams
)

def resolve_callback():
    print('CALLING BACK')

class TestOnPayloadEvent(BaseTestConfig):

    def test_on_payload_event(cls):
        print('should set on payload event')

        dict = {
            'uuid': '00000000-0000-4839-af2f-f794874a80b0',
            'data': {
                'opened': True
            },
            'payload': cls.json_fixtures['payload']['get'],
            'resolve': resolve_callback,
        }
        cls.assertEqual(SubscriptionCallbackParams(**dict).to_dict(), dict)
    
    def test_on_payload_event_fail(cls):
        print('should fail to set application details')

        dict = {
            'uuid': '00000000-0000-4839-af2f-f794874a80b0',
            'data': {
                'opened': True
            },
            'payload': None,
            'resolve': resolve_callback,
        }
        try:
            SubscriptionCallbackParams(**dict)
            cls.fail("SubscriptionCallbackParams: raised Exception unexpectedly!")
        except Exception as e:
            cls.assertEqual(str(e), "xumm.resource.types.xumm_api.XummGetPayloadResponse() argument after ** must be a mapping, not NoneType")