import asyncio
import xumm
from unittest.mock import Mock, patch
from tests.fixtures import xumm_api as test_fixtures
from xumm.util import read_json

import websockets
import time
import json

mock_ws = None

json_fixtures = read_json('./tests/fixtures/xumm_api.json')

@patch('xumm.client.requests.get')
async def main(mock_get):
    def callback_func(msg):
        print('CALLBACK: {}'.format(msg['data']))

    xumm.api_key = 'aaaaaaaa-bbbb-cccc-dddd-1234567890ab'
    xumm.api_secret = 'cbbbbbbb-aaaa-cccc-dddd-1234567890ab'
    sdk = xumm.XummSdk()
    ws_sdk = xumm.XummWs()
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = json_fixtures['payload']['get']

    try:
        await ws_sdk.subscribe(
            sdk,
            '0ef943e9-18ae-4fa2-952a-6f55dce363f0',
            callback_func,
        )
    except KeyboardInterrupt as e:
        ws_sdk.unsubscribe()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())