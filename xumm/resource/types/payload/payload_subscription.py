#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource
import six
from typing import Union, List, Dict, Callable, Any  # noqa: F401

from xumm.ws_client import WSClient
from ..xumm_api import XummGetPayloadResponse as XummPayload

# export interface PayloadSubscription {
#   payload: XummPayload,
#   resolved: Promise<unknown> | undefined
#   resolve: (resolveData?: unknown) => void
#   websocket: WebSocket
# }

class PayloadSubscription(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'payload': 'XummPayload',
        'resolved': 'Callable[[Any], Any]',
        'resolve': 'Callable[[Any], Any]',
        'websocket': 'WSClient',
    }

    attribute_map = {
        'payload': 'payload',
        'resolved': 'resolved',
        'resolve': 'resolve',
        'websocket': 'websocket',
    }
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The PayloadSubscription of this PayloadSubscription.  # noqa: E501
        :rtype: PayloadSubscription
        """
        cls._payload = None
        cls._resolved = None
        cls._resolve = None
        cls._websocket = None
        cls.payload = XummPayload(**kwargs['payload'])
        cls.resolved = kwargs['resolved']
        cls.resolve = kwargs['resolve']
        cls.websocket = kwargs['websocket']

    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.model_types):
            value = getattr(cls, attr)
            attr = cls.attribute_map[attr]
            if attr == 'websocket' or attr == 'resolve':
                result[attr] = value
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PayloadSubscription, dict):
            for key, value in cls.items():
                result[key] = value

        return result
        # return {k: v for k, v in result.items() if v is not None}

    @property
    def payload(cls) -> XummPayload:
        """Gets the payload of this PayloadSubscription.


        :return: The payload of this PayloadSubscription.
        :rtype: XummPayload
        """
        return cls._payload

    @payload.setter
    def payload(cls, payload: XummPayload):
        """Sets the payload of this PayloadSubscription.


        :param payload: The payload of this PayloadSubscription.
        :type meta: CreatedPayload
        """
        if payload is None:
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        cls._payload = payload
        
    @property
    def resolved(cls) -> Callable[[Any], Any]:
        """Gets the resolved of this PayloadSubscription.


        :return: The resolved of this PayloadSubscription.
        :rtype: Callable
        """
        return cls._resolved

    @resolved.setter
    def resolved(cls, resolved: Callable[[Any], Any]):
        """Sets the resolved of this PayloadSubscription.


        :param resolved: The resolved of this PayloadSubscription.
        :type meta: Payload
        """
        if resolved is None:
            raise ValueError("Invalid value for `resolve`, must not be `None`")  # noqa: E501

        cls._resolved = resolved

    @property
    def resolve(cls) -> Callable[[Any], Any]:
        """Gets the resolve of this PayloadSubscription.


        :return: The resolve of this PayloadSubscription.
        :rtype: Callable
        """
        return cls._resolve

    @resolve.setter
    def resolve(cls, resolve: Callable[[Any], Any]):
        """Sets the resolve of this PayloadSubscription.


        :param resolve: The resolve of this PayloadSubscription.
        :type meta: Callable
        """
        if resolve is None:
            raise ValueError("Invalid value for `resolve`, must not be `None`")  # noqa: E501

        cls._resolve = resolve

    @property
    def websocket(cls) -> WSClient:
        """Gets the websocket of this PayloadSubscription.


        :return: The websocket of this PayloadSubscription.
        :rtype: WSClient
        """
        return cls._websocket

    @websocket.setter
    def websocket(cls, websocket: WSClient):
        """Sets the websocket of this PayloadSubscription.


        :param websocket: The websocket of this PayloadSubscription.
        :type meta: WSClient
        """
        if websocket is None:
            raise ValueError("Invalid value for `websocket`, must not be `None`")  # noqa: E501

        cls._websocket = websocket