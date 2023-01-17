#!/usr/bin/env python
# coding: utf-8

from xumm import client
from xumm.resource import XummResource

from .types import (
    PushEventResponse,
    PushPushResponse,
    XummPushEventRequest,
)


class PushResource(XummResource):

    @classmethod
    def event_url(cls) -> str:
        """
        Gets the POST url of this PushResource

        :return: The POST url of this PushResource.
        :rtype: str
        """
        return super(PushResource, cls).platform_url() + 'xapp/event' + '/'  # noqa: E501

    @classmethod
    def push_url(cls) -> str:
        """
        Gets the POST url of this PushResource

        :return: The POST url of this PushResource.
        :rtype: str
        """
        return super(PushResource, cls).platform_url() + 'xapp/push' + '/'  # noqa: E501

    def refresh_from(cls, **kwargs) -> 'PushResource':
        return cls

    def event(cls, payload: XummPushEventRequest) -> PushEventResponse:
        """Returns the dict as a model

        :return: The PushEventResponse of this PushEventResponse.  # noqa: E501
        :rtype: PushEventResponse
        """

        res = client.post(cls.event_url(), payload.to_dict())
        return PushEventResponse(**res)

    def push(cls, payload: XummPushEventRequest) -> PushPushResponse:
        """Returns the dict as a model

        :return: The PushPushResponse of this PushPushResponse.  # noqa: E501
        :rtype: PushPushResponse
        """

        res = client.post(cls.push_url(), payload.to_dict())
        return PushPushResponse(**res)
