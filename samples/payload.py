#!/usr/bin/env python
# coding: utf-8
import logging
import asyncio

import xumm

from fixtures import sample_payload


class PayloadExample:
    def __init__(self):
        logging.debug('')
        self.sdk = xumm.XummSdk('API_KEY', 'API_SECRET')
        self.logger = logging.getLogger(self.__module__)
        self.logger.setLevel(level=logging.DEBUG)

    def subscription_callback(self, event):
        self.logger.info('Subscription Event data: {}'.format(event['data']))
        if 'expired' in event['data'] or 'signed' in event['data']:
            # payload is reolved reuturn the data
            return event['data']
            

    async def run(self):
        # create the payload by passing the details and get payload UUID
        try: 
            create_payload_resp = self.sdk.payload.create(sample_payload)
            self.logger.info("Payload created with id: %s" % create_payload_resp.uuid)            
        except Exception as e:
            self.logger.error("Unable to create the payload: %s" % e)
            return

        # start the websocket subscription on this payload and listen for changes
        subscription = await self.sdk.payload.subscribe(create_payload_resp.uuid, self.subscription_callback)
        # wait for the payload to resolve
        resolve_data = await subscription.resolved()
        # now we can cancel the subscription
        self.sdk.payload.unsubscribe()

        # fetch the payload from backend
        get_payload_resp = self.sdk.payload.get(create_payload_resp.uuid)
        self.logger.info("Payload resolved: %s" % get_payload_resp.meta.resolved)            


if __name__ == "__main__":
    example = PayloadExample()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(example.run())

