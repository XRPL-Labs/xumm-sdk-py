from cmath import e
from testing_config import BaseTestConfig
import os
from unittest.mock import Mock, patch

import pytest
import xumm

class TestXummSDK(BaseTestConfig):

    @pytest.mark.skip(reason="Using Prod Cert")
    def test_common(cls):
        print('Common XUMM API client tests')
        # cls.test_xumm_dotenv()
        # cls.test_xumm_construct()
        # cls._test_xumm_ping()
        # cls._test_invalid_credentials()

    def _test_xumm_dotenv(cls):
        print('should construct based on dotenv')
        os.environ['XUMM_APIKEY'] = cls.json_fixtures['api']['key']
        os.environ['XUMM_APISECRET'] = cls.json_fixtures['api']['secret']
        try:
            sdk = xumm.XummSdk()
        except Exception:
            cls.fail("XummSdk() raised Exception unexpectedly!")

    def _test_xumm_construct(cls):
        print('should construct based on provided api key & secret')
        try:
            xumm.api_key = cls.json_fixtures['api']['key']
            xumm.api_secret = cls.json_fixtures['api']['secret']
            sdk = xumm.XummSdk()
        except Exception:
            cls.fail("XummSdk() raised Exception unexpectedly!")
            
    def _test_xumm_invalid_keys(cls):
        print('should get error results on invalid api key / secret')
        try:
            xumm.api_key = cls.json_fixtures['api']['key']
            xumm.api_secret = cls.json_fixtures['api']['secret']
            sdk = xumm.XummSdk()
        except Exception:
            cls.fail("XummSdk() raised Exception unexpectedly!")
        # self.assertNotEqual(len(result), 0)

    @pytest.mark.skip(reason="Using Prod Cert")
    @patch('xumm.client.requests.get')
    def test_xumm_ping(cls, mock_get):
        print('should get app name on valid credentials')
        xumm.api_key = cls.json_fixtures['api']['key']
        xumm.api_secret = cls.json_fixtures['api']['secret']
        sdk = xumm.XummSdk()

        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['ping']['pong']
        cls.assertEqual(sdk.ping().to_dict(), cls.json_fixtures['ping']['pong'])

    @pytest.mark.skip(reason="Using Prod Cert")
    @patch('xumm.client.requests.get')
    def test_invalid_credentials(cls, mock_get):
        print('should get auth error on invalid credentials')
        xumm.api_key = cls.json_fixtures['api']['key']
        xumm.api_secret = cls.json_fixtures['api']['secret']
        sdk = xumm.XummSdk()

        mock_get.return_value = Mock(status_code=403)
        mock_get.return_value.json.return_value = cls.json_fixtures['invalidCredentials']

        try:
           result = sdk.ping()
        except Exception as e:
            cls.assertEqual(e.error['reference'], cls.json_fixtures['invalidCredentials']['error']['reference'])
            cls.assertEqual(e.error['code'], cls.json_fixtures['invalidCredentials']['error']['code'])
    
    @pytest.mark.skip(reason="Using Prod Cert")
    @patch('xumm.client.requests.get')
    def test_fetch_curated_assets(cls, mock_get):
        print('should fetch curated assets')
        xumm.api_key = cls.json_fixtures['api']['key']
        xumm.api_secret = cls.json_fixtures['api']['secret']
        sdk = xumm.XummSdk()

        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['curatedAssets']
        cls.assertEqual(sdk.curated_assets().to_dict(), cls.json_fixtures['curatedAssets'])

    @pytest.mark.skip(reason="Using Prod Cert")
    @patch('xumm.client.requests.get')
    def test_fetch_kyc_status(cls, mock_get):
        print('should fetch user KYC status')
        xumm.api_key = cls.json_fixtures['api']['key']
        xumm.api_secret = cls.json_fixtures['api']['secret']
        sdk = xumm.XummSdk()

        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['kycResult']
        cls.assertEqual(sdk.kyc_status().to_dict(), cls.json_fixtures['kycResult'])

    @pytest.mark.skip(reason="Using Prod Cert")
    @patch('xumm.client.requests.get')
    def test_fetch_tx(cls, mock_get):
        print('should fetch an XRPL tx')
        xumm.api_key = cls.json_fixtures['api']['key']
        xumm.api_secret = cls.json_fixtures['api']['secret']
        sdk = xumm.XummSdk()
        
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['xrplTx']

        print(sdk.xrpl_tx(cls.json_fixtures['xrplTx']['txid']).to_dict()['balanceChanges'])
        print(cls.json_fixtures['xrplTx']['balanceChanges'])
        print(sdk.xrpl_tx(cls.json_fixtures['xrplTx']['txid']).to_dict()['transaction'])
        print(cls.json_fixtures['xrplTx']['transaction'])

        # cls.assertEqual(sdk.xrpl_tx(cls.json_fixtures['xrplTx']['txid']).to_dict(), cls.json_fixtures['xrplTx'])
        print(ee)