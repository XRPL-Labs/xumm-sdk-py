#!/usr/bin/env python
# coding: utf-8

import asyncio
import xumm
from unittest.mock import Mock, patch
from tests.fixtures import xumm_api as test_fixtures
from xumm.util import read_json
import time
import json

mock_ws = None

# json_fixtures = read_json('./tests/fixtures/xumm_api.json')

@patch('xumm.client.requests.get')
async def main(mock_get):
    def callback_func(msg):
        print('CALLBACK: {}'.format(msg['data']))

    xumm.api_key = "json_fixtures['api']['key']"
    xumm.api_secret = "json_fixtures['api']['secret']"
    sdk = xumm.XummSdk()
    mock_get.return_value = Mock(status_code=200)
    # mock_get.return_value.json.return_value = json_fixtures['payload']['get']
    mock_get.return_value.json.return_value = {}

    try:
        sdk.payload.mock = True
        await sdk.payload.subscribe(
            '0ef943e9-18ae-4fa2-952a-6f55dce363f0',
            callback_func,
        )
    except Exception as e:
        print('ERROR: {}'.format(e))
    except KeyboardInterrupt as e:
        print(e)
        sdk.unsubscribe()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())