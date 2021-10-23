from unittest import TestCase

import xumm


class BaseTestConfig(TestCase):

    client_id = ''
    client_secret = ''
    version = 'v2'
    client = None

    def __main__(self):
        self.setUp()

    def setUp(self):
        print('Set Up Testing Auth')
        xumm.env = 'production'
        xumm.api_client_id = self.client_id
        xumm.api_client_secret = self.client_secret
        xumm.api_version = self.version
        self.xumm_auth()

    def xumm_auth(self):
        self.client = xumm.Payload
        self.assertNotEqual(self.client, None)

    def tearDown(self):
        print('Tear Down')
