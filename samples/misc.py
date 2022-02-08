#!/usr/bin/env python
# coding: utf-8
import logging
import asyncio

import xumm

class MiscExample:
    def __init__(self):
        logging.debug('')
        self.sdk = xumm.XummSdk('API_KEY', 'API_SECRET')
        self.logger = logging.getLogger(self.__module__)
        self.logger.setLevel(level=logging.DEBUG)

    async def run(self):
        # send ping to the backend and print application name
        ping_response = self.sdk.ping()
        self.logger.info("Ping response: application name: %s" % ping_response.application.name)

        # get curated assets and print available currencies count
        curated_assets_response = self.sdk.get_curated_assets()
        self.logger.info("Curated_assets response: currencies count %s" % str(len(curated_assets_response.currencies)))


        # get kyc status of a xrpl address
        address = "rDWLGshgAxSX2G4TEv3gA6QhtLgiXrWQXB"
        kyc_status_response = self.sdk.get_kyc_status(address)
        self.logger.info("Kyc status for account %s: %s" % (address, kyc_status_response))


        # get transaction by hash from ledger
        tx_hash = "017DED8F5E20F0335C6F56E3D5EE7EF5F7E83FB81D2904072E665EEA69402567"
        get_tx_response = self.sdk.get_transaction(tx_hash)
        self.logger.info("transaction balance changes: %s" % get_tx_response.balance_changes)


if __name__ == "__main__":
    example = MiscExample()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(example.run())

