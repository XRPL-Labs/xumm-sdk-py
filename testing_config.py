from unittest import TestCase
from tests.fixtures import xumm_api

from xumm.util import read_json

import xumm


class BaseTestConfig(TestCase):

    sdk = None
    json_fixtures = {}

    def __main__(cls):
        cls.setUp()

    def setUp(cls):
        print('Set Up Testing')
        cls.json_fixtures = read_json('./tests/fixtures/xumm_api.json')
        xumm.api_key = cls.json_fixtures['api']['key']
        xumm.api_secret = cls.json_fixtures['api']['secret']
        cls.sdk = xumm.XummSdk()

    def tearDown(cls):
        print('Tear Down Testing')
