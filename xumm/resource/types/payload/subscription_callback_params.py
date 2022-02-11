#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource
from typing import Dict, Callable, Any

from ..xumm_api import XummGetPayloadResponse as XummPayload


class SubscriptionCallbackParams(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'uuid': True,
        'data': True,
        'payload': True,
        'resolve': True,
    }

    model_types = {
        'uuid': str,
        'data': dict,
        'payload': dict,
        'resolve': Callable,
    }

    attribute_map = {
        'uuid': 'uuid',
        'data': 'data',
        'payload': 'payload',
        'resolve': 'resolve',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The PayloadSubscription of this PayloadSubscription.  # noqa: E501
        :rtype: PayloadSubscription
        """
        cls.sanity_check(kwargs)
        cls._uuid = None
        cls._data = None
        cls._payload = None
        cls._resolve = None
        cls.uuid = kwargs['uuid']
        cls.data = kwargs['data']
        cls.payload = XummPayload(**kwargs['payload'])
        cls.resolve = kwargs['resolve']

    @property
    def uuid(cls) -> str:
        """Gets the uuid of this XummPostPayloadResponse.


        :return: The uuid of this XummPostPayloadResponse.
        :rtype: str
        """
        return cls._uuid

    @uuid.setter
    def uuid(cls, uuid: str):
        """Sets the uuid of this XummPostPayloadResponse.


        :param uuid: The uuid of this XummPostPayloadResponse.
        :type uuid: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        cls._uuid = uuid

    @property
    def data(cls) -> Dict[str, object]:
        """Gets the data of this XummCustomMeta.


        :return: The data of this XummCustomMeta.
        :rtype: Dict[str, object]
        """
        return cls._blob

    @data.setter
    def data(cls, data: Dict[str, object]):
        """Sets the data of this XummCustomMeta.


        :param data: The data of this XummCustomMeta.
        :type data: Dict[str, object]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        cls._blob = data

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
