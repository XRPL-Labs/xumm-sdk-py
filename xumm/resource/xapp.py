#!/usr/bin/env python
# coding: utf-8

from xumm import client
from xumm.resource import XummResource

from .types import (
    XappOttResponse,
    XappEventResponse,
    XappPushResponse,
    XummXappEventRequest,
    XummXappPushRequest,
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

    @classmethod
    def event_url(cls) -> str:
        """
        Gets the POST url of this XappResource

        :return: The POST url of this XappResource.
        :rtype: str
        """
        return super(XappResource, cls).platform_url() + 'xapp/event' + '/'  # noqa: E501

    @classmethod
    def push_url(cls) -> str:
        """
        Gets the POST url of this XappResource

        :return: The POST url of this XappResource.
        :rtype: str
        """
        return super(XappResource, cls).platform_url() + 'xapp/push' + '/'  # noqa: E501

    def refresh_from(cls, **kwargs) -> 'XappResource':
        return cls

    def ott(cls, token: str) -> XappOttResponse:
        """Returns the dict as a model

        :return: The XappOttResponse of this XappOttResponse.  # noqa: E501
        :rtype: XappOttResponse
        """

        res = client.get(cls.ott_url(token))
        return XappOttResponse(**res)

    def event(cls, payload: XummXappEventRequest) -> XappEventResponse:
        """Returns the dict as a model

        :return: The XappEventResponse of this XappEventResponse.  # noqa: E501
        :rtype: XappEventResponse
        """

        res = client.post(cls.event_url(), payload.to_dict())
        return XappEventResponse(**res)

    def push(cls, payload: XummXappPushRequest) -> XappPushResponse:
        """Returns the dict as a model

        :return: The XappPushResponse of this XappPushResponse.  # noqa: E501
        :rtype: XappPushResponse
        """

        res = client.post(cls.push_url(), payload.to_dict())
        return XappPushResponse(**res)
