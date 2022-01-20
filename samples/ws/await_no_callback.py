#!/usr/bin/env python
# coding: utf-8

import asyncio
import xumm

# https://gist.github.com/WietseWind/76890afd39a01e9876c8a629b3e58174


async def main():

    payload_by_uuid = '289e9ae-7d5d-4d5f-b89c-18633112ce09'

    sdk = xumm.XummSdk()

    try:
        subscription = await sdk.payload.subscribe(
            '1289e9ae-7d5d-4d5f-b89c-18633112ce09',
            # callback_func,
        )
        
        async def callback_func(event):
            print('CALLBACK: {}'.format(event['data']))
            if 'signed' in event['data']:
                subscription.resolve()
        
        subscription.websocket._on_message = callback_func

        await subscription.resolved

        print('Payload {} resolved'.format(subscription.payload.meta.uuid))
    except Exception as e:
        print('ERROR: {}'.format(e))
    except KeyboardInterrupt as e:
        print(e)
        sdk.unsubscribe()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())