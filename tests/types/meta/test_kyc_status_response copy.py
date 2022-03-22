#!/usr/bin/env python
# coding: utf-8

import pytest
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

        with pytest.raises(ValueError, match=r"Invalid value for `kyc_status` \(TEMP\), must be one of \['NONE', 'IN_PROGRESS', 'REJECTED', 'SUCCESSFUL']"):
            KycStatusResponse(**dict)
            cls.fail("KycStatusResponse: raised Exception unexpectedly!")