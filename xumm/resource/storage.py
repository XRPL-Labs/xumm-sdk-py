#!/usr/bin/env python
# coding: utf-8

from xumm import client
from xumm.resource import XummResource

from .types import (
    StorageSetResponse,
    StorageGetResponse,
    StorageDeleteResponse,
)

class StorageResource(XummResource):

    @classmethod
    def post_url(cls):
        """post_url."""
        return super(StorageResource, cls).platform_url() + 'storage' + '/'

    @classmethod
    def get_url(cls):
        """get_url."""
        return super(StorageResource, cls).platform_url() + 'storage' + '/'

    @classmethod
    def delete_url(cls):
        """delete_url."""
        return super(StorageResource, cls).platform_url() + 'storage' + '/'

    def refresh_from(cls, **kwargs):
        return cls

    def set(cls, data) -> StorageSetResponse:
        """Returns the dict as a model

        :return: The StorageSetResponse of this StorageSetResponse.  # noqa: E501
        :rtype: StorageSetResponse
        """
        
        res = client.post(cls.post_url(), data)
        return StorageSetResponse(**res)

    def get(cls) -> StorageGetResponse:
        """Returns the dict as a model

        :return: The StorageGetResponse of this StorageGetResponse.  # noqa: E501
        :rtype: StorageGetResponse
        """
        
        res = client.get(cls.get_url())
        return StorageGetResponse(**res)

    def delete(cls) -> StorageDeleteResponse:
        """Returns the dict as a model

        :return: The StorageDeleteResponse of this StorageDeleteResponse.  # noqa: E501
        :rtype: StorageDeleteResponse
        """
        
        res = client.delete(cls.delete_url())
        return StorageDeleteResponse(**res)
