#!/usr/bin/env python
# coding: utf-8
import logging
import asyncio

import xumm


class StorageExample:
    def __init__(self):
        logging.debug('')
        self.sdk = xumm.XummSdk('API_KEY', 'API_SECRET')
        self.logger = logging.getLogger(self.__module__)
        self.logger.setLevel(level=logging.DEBUG)

    async def run(self):
        # storge some json value in storage
        self.logger.info("Set storage value")
        set_storage_result = self.sdk.storage.set({'name': 'Wietse', 'age': 32, 'male': True})
        # True

        if not set_storage_result:
            self.logger.error("Unable to set to storage: %s" % e)
            return

        # GET the storage content
        get_storage_result = self.sdk.storage.get()
        self.logger.info("Current storage value: %s" % get_storage_result.data)
        # { 'name': 'Wietse', 'age': 32, 'male': True }


        self.logger.info("Delete storage value")
        delete_storage_result = self.sdk.storage.delete()

        if not delete_storage_result:
            self.logger.error("Unable to delete the storage: %s" % delete_storage_result)

        get_storage_result_after_delete = self.sdk.storage.get()
        self.logger.info("Current storage value after delete: %s" % get_storage_result_after_delete.data)
        # None
               


if __name__ == "__main__":
    example = StorageExample()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(example.run())

