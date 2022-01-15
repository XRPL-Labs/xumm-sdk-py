from unittest import TestCase

from xumm.util import read_json

import xumm


class BaseTestConfig(TestCase):

    sdk = None
    ws_client = None
    ws_sdk = None
    json_fixtures = {}

    @classmethod
    def setUpClass(cls):
        cls.json_fixtures = read_json('./tests/fixtures/xumm_api.json')
        xumm.api_key = cls.json_fixtures['api']['key']
        xumm.api_secret = cls.json_fixtures['api']['secret']
        cls.sdk = xumm.XummSdk()
        cls.ws_client = xumm.XummWsClient()
        cls.ws_sdk = xumm.XummWs()

    def tearDown(cls):
        print('Tear Down Testing')