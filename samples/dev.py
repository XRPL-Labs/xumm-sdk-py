#!/usr/bin/env python
# coding: utf-8
import asyncio

import xumm
from xumm.resource.types import XummPostPayloadBodyJson

import logging
logger = logging.getLogger('app')


async def main():
    try:
        sdk = xumm.XummSdk('someAppKey', 'someAppSecret')
        pong = sdk.ping()
        logger.info(pong)

        curated_assets = sdk.get_curated_assets()
        logger.info(curated_assets)

        kwargs = {
            'txjson': {
                'TransactionType' : 'Payment',
                'Destination' : 'rPEPPER7kfTD9w2To4CQk6UCfuHM9c6GDY',
                'DestinationTag': 495,
                'Amount': '1337'
            }
        }
        payment_payload: XummPostPayloadBodyJson = XummPostPayloadBodyJson(**kwargs)
        payload = sdk.payload.create(payment_payload)
        logger.info(payload)

        if payload:
            async def callback(event):
                logger.info('Subscription Event data: {}'.format(event['data']))
                if 'expired' in event['data'] or 'signed' in event['data']:
                    return event['data']
            
            await sdk.payload.subscribe(payload, callback)
    
    except Exception as e:
        logger.info(e)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())