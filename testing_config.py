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
        self.client = xumm.Account()
        self.assertNotEqual(self.client, None)
        self.assertEqual(self.client.scope, 'read:calendar write:calendar')
        self.assertEqual(self.client.expires_in, 86400)
        self.assertEqual(self.client.token_type, 'Bearer')

    def tearDown(self):
        print('Tear Down')
