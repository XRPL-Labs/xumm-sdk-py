import os
import json
from testing_config import BaseTestConfig

from xumm.resource.types import (
    KycStatusResponse
)

class TestKycStatusResponse(BaseTestConfig):

    def test_kyc_status_response(cls):
        print('should set kyc status response')

        dict = cls.json_fixtures['kycStatus']['post']
        cls.assertEqual(KycStatusResponse(**dict).to_dict(), dict)

    def test_kyc_status_response_fail(cls):
        print('should fail to set application details')

        dict = {
            "kycStatus": "TEMP",  # FAILS
            "possibleStatuses": {
                "NONE": "No KYC attempt has been made",
                "IN_PROGRESS": "KYC flow has been started, but did not finish (yet)",
                "REJECTED": "KYC flow has been started and rejected (NO SUCCESSFUL KYC)",
                "SUCCESSFUL": "KYC flow has been started and was SUCCESSFUL :)"
            }
        }
        try:
            KycStatusResponse(**dict)
            cls.fail("KycStatusResponse: raised Exception unexpectedly!")
        except Exception as e:
            cls.assertEqual(str(e), "Invalid value for `kyc_status` (TEMP), must be one of ['NONE', 'IN_PROGRESS', 'REJECTED', 'SUCCESSFUL']")