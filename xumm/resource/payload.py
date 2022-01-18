#!/usr/bin/env python
# coding: utf-8

from typing import Union
from xumm import (
    client
)
from xumm.resource import XummResource

from .types import (
    XummPostPayloadBodyJson,
    XummPostPayloadBodyBlob,
    XummJsonTransaction,
    XummPostPayloadResponse,
    XummDeletePayloadResponse,
    XummGetPayloadResponse,
)

class PayloadResource(XummResource):

    @classmethod
    def post_url(cls):
        """post_url."""
        return super(PayloadResource, cls).platform_url() + 'payload' + '/'

    @classmethod
    def get_url(cls, id):
        """get_url."""
        return super(PayloadResource, cls).platform_url() + 'payload' + '/' + id

    @classmethod
    def delete_url(cls, id):
        """delete_url."""
        return super(PayloadResource, cls).platform_url() + 'payload' + '/' + id

    def refresh_from(cls, **kwargs):
        return cls

    def create(
        cls, 
        payload: Union[XummPostPayloadBodyJson, XummPostPayloadBodyBlob, XummJsonTransaction],
        return_errors: bool=False
    ) -> XummPostPayloadResponse:
        """Returns the dict as a model

        :param payload: The payload of this payload_create.
        :type payload: XummPostPayloadBodyJson | XummPostPayloadBodyBlob | XummJsonTransaction
        :param return_errors: The return_errors of this payload_create.
        :type return_errors: bool

        :return: The XummPostPayloadResponse of this XummPostPayloadResponse.  # noqa: E501
        :rtype: XummPostPayloadResponse
        """
        
        if not return_errors:
            try:
                res = client.post(cls.post_url(), payload)
                return XummPostPayloadResponse(**res)
            except:
                return None

        res = client.post(cls.post_url(), payload)
        return XummPostPayloadResponse(**res)
    
    def cancel(
        cls, 
        id: str=None,
        return_errors: bool=False
    ) -> XummDeletePayloadResponse:
        """Returns the dict as a model

        :return: The XummDeletePayloadResponse of this XummDeletePayloadResponse.  # noqa: E501
        :rtype: XummDeletePayloadResponse
        """

        if not return_errors:
            try:
                res = client.delete(cls.delete_url(id))
                return XummDeletePayloadResponse(**res)
            except:
                return None
        
        res = client.delete(cls.delete_url(id))
        return XummDeletePayloadResponse(**res)
        
    def get(
        cls, 
        id: str=None,
        return_errors: bool=False
    ) -> XummGetPayloadResponse:
        """Returns the dict as a model

        :return: The XummGetPayloadResponse of this XummGetPayloadResponse.  # noqa: E501
        :rtype: XummGetPayloadResponse
        """

        if not return_errors:
            try:
                res = client.get(cls.get_url(id))
                return XummGetPayloadResponse(**res)
            except:
                return None
        
        res = client.get(cls.get_url(id))
        return XummGetPayloadResponse(**res)