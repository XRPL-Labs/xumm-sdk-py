import os
import json
from testing_config import BaseTestConfig

from xumm.resource.types import (
    ApplicationDetails
)

class TestTypes(BaseTestConfig):

    def test_application_details(cls):
        print('should set application details')

        dict = {
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
        cls.assertEqual(ApplicationDetails(**dict).to_dict(), dict)

    def test_application_details_fail(cls):
        print('should set application details')

        dict = {
            "quota": {},
            "application": {
                "uuidv4": 1,
                "name": "SomeApplication",
                "webhookurl": "https://webhook.site/00000000-0000-4e34-8112-c4391247a8ee",
                "disabled": 0
            },
            "call": {
                "uuidv4": "2904b05f-5b37-4f3e-a624-940ad817943c"
            }
        }
        try:
            ApplicationDetails(**dict)
        except Exception as e:
            cls.assertEqual(str(e), "Invalid value for `uuidv4`, must be a `<class 'str'>`")