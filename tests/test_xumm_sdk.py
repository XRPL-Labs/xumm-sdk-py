from testing_config import BaseTestConfig
import pytest


# @pytest.mark.skip(reason="Using Prod Cert")
class TestXummSDK(BaseTestConfig):

    '''
    Test sdk
    '''

    # @pytest.mark.skip(reason="Using Prod Cert")
    def test_xumm_submit_payload(self):
        result = self.client.submit({})
        self.assertNotEqual(len(result), 0)
