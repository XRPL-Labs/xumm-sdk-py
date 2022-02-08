import pytest
from testing_config import BaseTestConfig

from xumm.resource.types import (
    KycInfoResponse
)

class TestKycInfoResponse(BaseTestConfig):

    def test_kyc_info_response(cls):
        print('should set kyc info response')

        dict = cls.json_fixtures['kycStatus']['get']
        cls.assertEqual(KycInfoResponse(**dict).to_dict(), dict)

    def test_kyc_info_response_fail(cls):
        print('should fail to set kyc info details')

        dict = {
            "account": 1,  # FAILS
            "kycApproved": True
        }

        with pytest.raises(ValueError, match=r"Invalid value: 1 for `account`, must be a `<class 'str'>` found: <class 'int'>"):
            KycInfoResponse(**dict)
            cls.fail("KycInfoResponse: raised Exception unexpectedly!")