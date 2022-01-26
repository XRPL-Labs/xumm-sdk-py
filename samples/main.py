#!/usr/bin/env python
# coding: utf-8

import xumm

import logging
logger = logging.getLogger('app')


def main():

    try:
        sdk = xumm.XummSdk()
        pong = sdk.ping()
        logger.info(pong)
    except Exception as e:
        print(e)

    # payload = sdk.payload.create({
    #   'custom_meta': {
    #     'instruction': 'Hey ❤️! Please sign for\n\nThis\nThat 🍻'
    #   },
    #   'user_token': 'ec079824-b804-49be-b521-a9502bc306ae',
    #   'txjson': {
    #     'TransactionType' : 'Payment',
    #     'Destination' : 'rPEPPER7kfTD9w2To4CQk6UCfuHM9c6GDY'
    #   }
    # })
    # logger.info(payload)
    
main()