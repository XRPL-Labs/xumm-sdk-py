import os
from xumm.resource import XummResource
import six
import json
from typing import List, Dict  # noqa: F401


class StorageSetRequest(XummResource):

    @classmethod
    def post_url(cls):
        """post_url."""
        return super(StorageSetRequest, cls).platform_url() + 'storage' + '/'


class StorageGetRequest(XummResource):

    @classmethod
    def get_url(cls):
        """get_url."""
        return super(StorageGetRequest, cls).platform_url() + 'storage' + '/'


class StorageDeleteRequest(XummResource):

    @classmethod
    def delete_url(cls):
        """delete_url."""
        return super(StorageDeleteRequest, cls).platform_url() + 'storage' + '/'
