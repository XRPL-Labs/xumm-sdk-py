
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
def main(mock_get):
    def callback_func(msg):
        print('CALLBACK')
        # print('CALLBACK: {}'.format(msg))

    xumm.api_key = 'aaaaaaaa-bbbb-cccc-dddd-1234567890ab'
    xumm.api_secret = 'cbbbbbbb-aaaa-cccc-dddd-1234567890ab'
    sdk = xumm.XummSdk()
    ws_sdk = xumm.XummWs()
    ws_client = xumm.XummWsClient()
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = json_fixtures['payload']['get']

    # try:
    #     payload = await ws_client.subscribe(
    #         sdk,
    #         '0ef943e9-18ae-4fa2-952a-6f55dce363f0',
    #         callback_func,
    #     )
    # except KeyboardInterrupt as e:
    #     ws_client.close()

    try:
        ws_sdk.subscribe(
            sdk,
            '0ef943e9-18ae-4fa2-952a-6f55dce363f0',
            callback_func,
        )
    except KeyboardInterrupt as e:
        ws_sdk.unsubscribe()
    
    # while True:
    #     print('SLEEP LOOP')
    #     await asyncio.sleep(60)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

main()