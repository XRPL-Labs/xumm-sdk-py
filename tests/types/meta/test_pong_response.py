import os
import json
from testing_config import BaseTestConfig

from xumm.resource.types import (
    PongResponse
)

class TestPongResponse(BaseTestConfig):

    def test_pong_response(cls):
        print('should set pong response')

        dict = cls.json_fixtures['ping']['pong']
        cls.assertEqual(PongResponse(**dict).to_dict(), dict)

    def test_pong_response_fail(cls):
        print('should fail to pong details')

        dict = {
            "pong": 'true',  # FAILS
            "auth": {
                "quota": {},
                "application": {
                    "uuidv4": "00000000-0000-4839-af2f-f794874a80b0",
                    "name": "SomeApplication",
                    "webhookurl": "https://webhook.site/00000000-0000-4e34-8112-c4391247a8ee",
                    "disabled": 0
                },
                "call": {
                    "uuidv4": "2904b05f-5b37-4f3e-a624-940ad817943c"
                }
            }
        }
        try:
            PongResponse(**dict)
            cls.fail("PongResponse: raised Exception unexpectedly!")
        except Exception as e:
            cls.assertEqual(str(e), "Invalid value for `pong`, must be a `<class 'bool'>`")