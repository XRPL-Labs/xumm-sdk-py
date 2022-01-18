from cmath import e
import os
from typing import Callable, Dict, Union, Any
from xumm import (
    client,
    error
)
from xumm.resource import XummResource
import json
import time
import re
import websocket
from websocket import WebSocketApp


from .types import (
    CreatedPayload,
    XummPayload,
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
        return_errors: bool=True
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
    
    def cancel(cls, id: str=None) -> XummDeletePayloadResponse:
        """Returns the dict as a model

        :return: The XummDeletePayloadResponse of this XummDeletePayloadResponse.  # noqa: E501
        :rtype: XummDeletePayloadResponse
        """
        
        res = client.delete(cls.delete_url(id))
        return XummDeletePayloadResponse(**res)
        
    def get(cls, id: str=None) -> XummGetPayloadResponse:
        """Returns the dict as a model

        :return: The XummGetPayloadResponse of this XummGetPayloadResponse.  # noqa: E501
        :rtype: XummGetPayloadResponse
        """
        
        res = client.get(cls.get_url(id))
        return XummGetPayloadResponse(**res)


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
        'resolve': 'Callable[[Any], Any]',
        'resolved': 'Callable[[Any], Any]',
        'websocket': 'Response',
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
        :return: The PayloadSubscription of this PayloadSubscription.  # noqa: E501
        :rtype: PayloadSubscription
        """
        # print(kwargs)
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._payload = None
        cls._payload = XummPayload(**kwargs['payload'])
        cls._resolve = None
        cls._resolve = kwargs['resolve']
        cls._resolved = None
        cls._resolved = kwargs['resolved']
        cls._websocket = None
        cls._websocket = kwargs['websocket']

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
    def resolved(cls) -> Callable[[Any], Any]:
        """Gets the resolved of this PayloadSubscription.


        :return: The resolved of this PayloadSubscription.
        :rtype: Callable
        """
        return cls._resolved

    @resolve.setter
    def resolve(cls, resolved: Callable[[Any], Any]):
        """Sets the resolved of this PayloadSubscription.


        :param resolved: The resolved of this PayloadSubscription.
        :type meta: Payload
        """
        if resolved is None:
            raise ValueError("Invalid value for `resolve`, must not be `None`")  # noqa: E501

        cls._resolved = resolved

    @property
    def websocket(cls) -> WebSocketApp:
        """Gets the websocket of this PayloadSubscription.


        :return: The websocket of this PayloadSubscription.
        :rtype: Payload
        """
        return cls._websocket

    @websocket.setter
    def websocket(cls, websocket: WebSocketApp):
        """Sets the websocket of this PayloadSubscription.


        :param websocket: The websocket of this PayloadSubscription.
        :type meta: Payload
        """
        if websocket is None:
            raise ValueError("Invalid value for `websocket`, must not be `None`")  # noqa: E501

        cls._websocket = websocket

class PayloadAndSubscription(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'created': 'CreatedPayload',
        'payload': 'XummPayload',
        'resolve': 'Callable[[Any], Any]',
        'resolved': 'Callable[[Any], Any]',
        'websocket': 'WebSocketApp',
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
        # print(kwargs)
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._payload = None
        cls._payload = XummPayload(**kwargs['payload'])
        cls._resolve = None
        cls._resolve = kwargs['resolve']
        cls._resolved = None
        cls._resolved = kwargs['resolved']
        cls._websocket = None
        cls._websocket = kwargs['websocket']

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
        if issubclass(PayloadAndSubscription, dict):
            for key, value in cls.items():
                result[key] = value

        return result
        # return {k: v for k, v in result.items() if v is not None}

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
    def websocket(cls) -> WebSocketApp:
        """Gets the websocket of this PayloadAndSubscription.


        :return: The websocket of this PayloadAndSubscription.
        :rtype: WebSocketApp
        """
        return cls._websocket

    @websocket.setter
    def websocket(cls, websocket: WebSocketApp):
        """Sets the websocket of this PayloadAndSubscription.


        :param websocket: The websocket of this PayloadAndSubscription.
        :type meta: WebSocketApp
        """
        if websocket is None:
            raise ValueError("Invalid value for `websocket`, must not be `None`")  # noqa: E501

        cls._websocket = websocket