#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase

from xumm.util import read_json


class BaseTestConfig(TestCase):

    sdk = None
    json_fixtures = {}

    @classmethod
    def setUpClass(cls):
        cls.json_fixtures = read_json('./tests/fixtures/xumm_api.json')

    def tearDown(cls):
        print('Tear Down Testing')
