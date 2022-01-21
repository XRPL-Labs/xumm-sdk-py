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
            payload_by_uuid,
            # callback_func,
        )

        def callback_func(event):
            print('Payload {} data: {}'.format(event['uuid'], event['data']))
            if 'signed' in event['data']:
                subscription.resolve(event['data'])
        
        subscription.websocket._on_message = callback_func

        await subscription.resolved()
        print('Payload {} {}'.format(subscription.payload.meta.uuid, await subscription.resolved()))
    except Exception as e:
        print('ERROR: {}'.format(e))
    except KeyboardInterrupt as e:
        sdk.payload.unsubscribe()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())