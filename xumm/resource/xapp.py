#!/usr/bin/env python
# coding: utf-8

from xumm import client
from xumm.resource import XummResource

from .types import (
    XappOttResponse,
)


class XappResource(XummResource):

    @classmethod
    def ott_url(cls, token: str) -> str:
        """
        Gets the GET url of this XappResource

        :param tx_hash: A string contain transaction hash.
        :type: str
        :return: The GET url of this XappResource.
        :rtype: str
        """
        return super(XappResource, cls).platform_url() + 'xapp/ott' + '/' + token  # noqa: E501

    def refresh_from(cls, **kwargs) -> 'XappResource':
        return cls

    def ott(cls, token: str) -> XappOttResponse:
        """Returns the dict as a model

        :return: The XappOttResponse of this XappOttResponse.  # noqa: E501
        :rtype: XappOttResponse
        """

        res = client.get(cls.ott_url(token))
        return XappOttResponse(**res)

