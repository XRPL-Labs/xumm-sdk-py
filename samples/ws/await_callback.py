#!/usr/bin/env python
# coding: utf-8

import asyncio
import xumm

# https://gist.github.com/WietseWind/76890afd39a01e9876c8a629b3e58174

from unittest.mock import Mock, patch
from xumm.util import read_json
json_fixtures = read_json('./tests/fixtures/xumm_api.json')
@patch('xumm.client.requests.get')
async def main(mock_get):
    payload_by_uuid = '289e9ae-7d5d-4d5f-b89c-18633112ce09'
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = json_fixtures['payload']['get']

    def callback_func(event):
        print('Payload {} data: {}'.format(event['uuid'], event['data']))
        if 'signed' in event['data']:
            return event['data']

    xumm.env = 'sandbox'
    sdk = xumm.XummSdk()
    
    try:
        subscription = await sdk.payload.subscribe(
            payload_by_uuid,
            callback_func,
        )

        await subscription.resolved()
        print('Payload {} {}'.format(subscription.payload.meta.uuid, await subscription.resolved()))
    except Exception as e:
        print('ERROR: {}'.format(e))
    except KeyboardInterrupt as e:
        sdk.payload.unsubscribe()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())