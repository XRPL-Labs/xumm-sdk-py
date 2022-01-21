#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase

from xumm.util import read_json


class BaseTestConfig(TestCase):

    sdk = None
    json_fixtures = {}

    @classmethod
    def setUpClass(cls):
        print('Set Up Class Testing')
        cls.json_fixtures = read_json('./tests/fixtures/xumm_api.json')

    @classmethod
    def tearDownClass(cls):
        print('Tear Down Class Testing')
