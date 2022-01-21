#!/usr/bin/env python
# coding: utf-8

import asyncio
import xumm

# https://gist.github.com/WietseWind/76890afd39a01e9876c8a629b3e58174


async def main():
    payload_by_uuid = '289e9ae-7d5d-4d5f-b89c-18633112ce09'

    def callback_func(event):
        print('Payload {} data: {}'.format(event['uuid'], event['data']))
        if 'signed' in event['data']:
            """
            Handle payload resolving, eg:
              1. Fetch updated payload results, with `Sdk.payload.get()`
              2. Fetch the transaction by hash (retrieved with 1.) on the XRPL to verify the transaction
              3. Persist the results in your own app's database
              4. Inform (async) the user (notification, mail, ...) if required
            """

            print('ON SIGNED DOING...')
            # Resolve & close the subscription
            return True

    sdk = xumm.XummSdk()
    
    try:
        await sdk.payload.subscribe(
            payload_by_uuid,
            callback_func,
        )
        print('NOT WAITING...')

        # Just continue doing things here. No need to wait.
    except Exception as e:
        print('ERROR: {}'.format(e))
    except KeyboardInterrupt as e:
        sdk.payload.unsubscribe()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())