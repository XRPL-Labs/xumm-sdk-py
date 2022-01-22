#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource
import six
from typing import Union, List, Dict, Callable, Any  # noqa: F401

from xumm.ws_client import WSClient
from ..xumm_api import (
    XummGetPayloadResponse as XummPayload,
    XummPostPayloadResponse as CreatedPayload,
)

# export interface PayloadAndSubscription extends PayloadSubscription {
#   created: CreatedPayload
# }


class PayloadAndSubscription(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'created': True,
        'payload': True,
        'resolve': True,
        'resolved': True,
        'websocket': True,
    }

    model_types = {
        'created': dict,
        'payload': dict,
        'resolve': Callable,
        'resolved': Callable,
        'websocket': WSClient,
    }

    attribute_map = {
        'payload': 'payload',
        'resolve': 'resolve',
        'resolved': 'resolved',
        'websocket': 'websocket',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The PayloadAndSubscription of this PayloadAndSubscription.  # noqa: E501
        :rtype: PayloadAndSubscription
        """
        cls.sanity_check(kwargs)
        cls._payload = None
        cls._resolve = None
        cls._resolved = None
        cls._websocket = None
        cls.payload = XummPayload(**kwargs['payload'])
        cls.resolve = kwargs['resolve']
        cls.resolved = kwargs['resolved']
        cls.websocket = kwargs['websocket']

    def to_dict(cls) -> Dict[str, object]:
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.attribute_map):
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
        if issubclass(PayloadAndSubscription, dict):
            for key, value in cls.items():
                result[key] = value

        return {
            k: v for k, v in result.items()
            if v is not None or k in
            cls.required and k in cls.nullable
        }

    @property
    def created(cls) -> CreatedPayload:
        """Gets the created of this PayloadAndSubscription.


        :return: The created of this PayloadAndSubscription.
        :rtype: PostPayloadResponse
        """
        return cls._created

    @created.setter
    def created(cls, created: CreatedPayload):
        """Sets the created of this PayloadAndSubscription.


        :param created: The created of this PayloadAndSubscription.
        :type meta: PostPayloadResponse
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        cls._created = created

    @property
    def payload(cls) -> XummPayload:
        """Gets the payload of this PayloadAndSubscription.


        :return: The payload of this PayloadAndSubscription.
        :rtype: GetPayloadResponse
        """
        return cls._payload

    @payload.setter
    def payload(cls, payload: XummPayload):
        """Sets the payload of this PayloadAndSubscription.


        :param payload: The payload of this PayloadAndSubscription.
        :type payload: XummPayload
        """
        if payload is None:
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        cls._payload = payload

    @property
    def resolve(cls) -> Callable[[Any], Any]:
        """Gets the resolve of this PayloadAndSubscription.


        :return: The resolve of this PayloadAndSubscription.
        :rtype: Callable
        """
        return cls._resolve

    @resolve.setter
    def resolve(cls, resolve: Callable[[Any], Any]):
        """Sets the resolve of this PayloadAndSubscription.


        :param resolve: The resolve of this PayloadAndSubscription.
        :type meta: Callable
        """
        if resolve is None:
            raise ValueError("Invalid value for `resolve`, must not be `None`")  # noqa: E501

        cls._resolve = resolve

    @property
    def resolved(cls) -> Callable[[Any], Any]:
        """Gets the resolved of this PayloadAndSubscription.


        :return: The resolved of this PayloadAndSubscription.
        :rtype: Callable
        """
        return cls._resolved

    @resolve.setter
    def resolve(cls, resolved: Callable[[Any], Any]):
        """Sets the resolved of this PayloadAndSubscription.


        :param resolved: The resolved of this PayloadAndSubscription.
        :type meta: Payload
        """
        if resolved is None:
            raise ValueError("Invalid value for `resolve`, must not be `None`")  # noqa: E501

        cls._resolved = resolved

    @property
    def websocket(cls) -> WSClient:
        """Gets the websocket of this PayloadAndSubscription.


        :return: The websocket of this PayloadAndSubscription.
        :rtype: WSClient
        """
        return cls._websocket

    @websocket.setter
    def websocket(cls, websocket: WSClient):
        """Sets the websocket of this PayloadAndSubscription.


        :param websocket: The websocket of this PayloadAndSubscription.
        :type meta: WSClient
        """
        if websocket is None:
            raise ValueError("Invalid value for `websocket`, must not be `None`")  # noqa: E501

        cls._websocket = websocket
