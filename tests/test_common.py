#!/usr/bin/env python
# coding: utf-8

from testing_config import BaseTestConfig
from unittest.mock import Mock, patch
from dotenv import dotenv_values

import xumm


class TestCommon(BaseTestConfig):

    def test_xumm_dotenv(cls):
        print('should construct based on dotenv')
        configs = { **dotenv_values(".env.sample") }
        cls.assertEqual(configs['XUMM_APIKEY'], 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX')
        cls.assertEqual(configs['XUMM_APISECRET'], 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX')
        try:
            sdk = xumm.XummSdk()
        except Exception:
            cls.fail("XummSdk() raised Exception unexpectedly!")

    def test_xumm_construct(cls):
        print('should construct based on provided api key & secret')
        try:
            sdk = xumm.XummSdk(
                cls.json_fixtures['api']['key'],
                cls.json_fixtures['api']['secret']
            )
        except Exception:
            cls.fail("XummSdk() raised Exception unexpectedly!")
            
    def test_xumm_invalid_keys(cls):
        print('should get error results on invalid api key / secret')
        try:
            sdk = xumm.XummSdk(
                'xxxxxx',
                'yyyyyyy'
            )
            cls.fail("XummSdk() raised Exception unexpectedly!")
        except Exception as e:
            cls.assertEqual(str(e), 'Invalid API secret provided. (HINT: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX).')

    @patch('xumm.client.requests.get')
    def test_xumm_ping(cls, mock_get):
        print('should get app name on valid credentials')
        sdk = xumm.XummSdk(
            cls.json_fixtures['api']['key'],
            cls.json_fixtures['api']['secret']
        )

        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['ping']['pong']

        cls.assertEqual(sdk.ping().to_dict(), cls.json_fixtures['ping']['pong'])

    @patch('xumm.client.requests.get')
    def test_invalid_credentials(cls, mock_get):
        print('should get auth error on invalid credentials')
        sdk = xumm.XummSdk(
            cls.json_fixtures['api']['key'],
            cls.json_fixtures['api']['secret']
        )

        mock_get.return_value = Mock(status_code=403)
        mock_get.return_value.json.return_value = cls.json_fixtures['invalidCredentials']

        try:
           sdk.ping()
           cls.fail("ping() raised Exception unexpectedly!")
        except Exception as e:
            cls.assertEqual(e.error['reference'], cls.json_fixtures['invalidCredentials']['error']['reference'])
            cls.assertEqual(e.error['code'], cls.json_fixtures['invalidCredentials']['error']['code'])
    
    @patch('xumm.client.requests.get')
    def test_fetch_curated_assets(cls, mock_get):
        print('should fetch curated assets')
        sdk = xumm.XummSdk(
            cls.json_fixtures['api']['key'],
            cls.json_fixtures['api']['secret']
        )

        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['curatedAssets']
        cls.assertEqual(sdk.get_curated_assets().to_dict(), cls.json_fixtures['curatedAssets'])

    @patch('xumm.client.requests.get')
    def test_fetch_kyc_status(cls, mock_get):
        print('should fetch user KYC status')
        sdk = xumm.XummSdk(
            cls.json_fixtures['api']['key'],
            cls.json_fixtures['api']['secret']
        )
        
        user_token = 'rPEPPER7kfTD9w2To4CQk6UCfuHM9c6GDY'
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['kycStatus']['get']
        cls.assertEqual(sdk.get_kyc_status(user_token).to_dict(), cls.json_fixtures['kycStatus']['get'])

    @patch('xumm.client.requests.post')
    def test_create_kyc_status(cls, mock_post):
        print('should create user KYC status')
        sdk = xumm.XummSdk(
            cls.json_fixtures['api']['key'],
            cls.json_fixtures['api']['secret']
        )

        user_token = '2557f69c-6617-40dc-9d1e-a34487cb3f90'

        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = cls.json_fixtures['kycStatus']['post']

        cls.assertEqual(sdk.get_kyc_status(user_token).kyc_status, 'IN_PROGRESS')

    @patch('xumm.client.requests.get')
    def test_fetch_tx(cls, mock_get):
        print('should fetch an XRPL tx')
        sdk = xumm.XummSdk(
            cls.json_fixtures['api']['key'],
            cls.json_fixtures['api']['secret']
        )
        
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = cls.json_fixtures['xrplTx']

        cls.assertEqual(sdk.get_transaction(cls.json_fixtures['xrplTx']['txid']).to_dict(), cls.json_fixtures['xrplTx'])