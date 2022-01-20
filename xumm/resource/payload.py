#!/usr/bin/env python
# coding: utf-8

import logging
from typing import Union, Callable
from xumm import (
    client,
    error
)
from xumm.resource import XummResource

from .types import (
    XummPostPayloadBodyJson,
    XummPostPayloadBodyBlob,
    XummJsonTransaction,
    XummPostPayloadResponse,
    XummDeletePayloadResponse,
    XummGetPayloadResponse,
    XummPayload,
    CreatedPayload,
    PayloadSubscription,
    PayloadAndSubscription
)

from xumm.ws_client import WSClient


class CallbackPromise:

    def __init__(cls):
        cls.data: object = None
        
    def _resolve(cls, resolveData):
        cls.data = resolveData
        return cls.data

    async def _resolved(cls):
        return cls.data


class PayloadResource(XummResource):

    _conn: WSClient = None
    _callback: Callable = None
    _mock: bool = False

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

    @classmethod
    def resolve_payload(
        cls,
        payload: Union[str, XummPayload, CreatedPayload]
    ) -> XummPayload:
        if isinstance(payload, str):
            return cls.get(payload)
        if isinstance(payload, CreatedPayload):
            return cls.get(payload.uuid)
        if isinstance(payload, XummPayload):
            return payload

        raise error.APIError('Could not resolve payload (not found)')

    @classmethod
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
    
    @classmethod
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
        
    @classmethod
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

    @classmethod
    async def subscribe(
        cls, 
        payload: Union[str, XummPayload, CreatedPayload], 
        callback
    ) -> PayloadSubscription:
        """Subscribe to a channel
        :returns: PayloadSubscription
        """

        callback_promise = CallbackPromise()
        
        payload_details = cls.resolve_payload(payload)

        def on_message(json_data):
            if json_data and cls._callback and 'devapp_fetched' not in json_data:
                try:
                    kwargs = {
                        'payload': payload_details.to_dict(),
                        'websocket': cls._conn
                    }
                    callback_result = cls._callback({
                        'uuid': payload_details.meta.uuid,
                        'data': json_data,
                        'resolve': callback_promise._resolve,
                        'payload': payload_details
                    })

                    if callback_result:
                        callback_promise._resolve(callback_result)

                except Exception as e:
                    print('Payload {}: Callback exception: {}'.format(payload_details.meta.uuid, e))

        def on_error(error):
            print('Payload {}: Received message, unable to parse as JSON'.format(payload_details.meta.uuid))
            cls._conn.disconnect()
            # raise error

        # def on_close(ws, close_status_code, close_msg):
        def on_close():
            print('Payload {}: Subscription ended (WebSocket closed)'.format(payload_details.meta.uuid))

        def on_open(connection):
            print('Payload {}: Subscription active (WebSocket opened)'.format(payload_details.meta.uuid))

        if payload_details:
            cls._callback = callback
            cls._conn = WSClient(
                log_level=logging.ERROR if cls.mock else logging.ERROR,
                server='ws://localhost:8765' if getattr(cls, '_mock') == True else 'wss://xumm.app/sign/{}'.format(payload_details.meta.uuid),
                on_response = on_message,
                on_error = on_error,
                on_close = on_close,
                on_open = on_open
            )
            cls._conn.connect()
            
            resp = {
                'payload': payload_details.to_dict(),
                'resolve': callback_promise._resolve,
                'resolved': callback_promise._resolved,
                'websocket': cls._conn
            }
            return PayloadSubscription(**resp)

        raise ValueError('Could not subscribe: could not fetch payload')

    @classmethod
    async def create_and_subscribe(
        cls,
        payload: CreatedPayload,
        callback
    ) -> PayloadAndSubscription:
        """Create payload and subscribe to a channel
        :returns: PayloadAndSubscription
        """

        created_payload = await cls.create(payload)
        if created_payload:
            subscription = await cls.subscribe(created_payload, callback)
            return {
                'created': created_payload,
                'subscription': subscription
            }
        raise ValueError('Error creating payload or subscribing to created payload')

    @classmethod
    def unsubscribe(cls):
        """Unsubscribe to a channel
        :returns: None
        """
        cls._conn.disconnect()

    @property
    def mock(cls) -> bool:
        """Gets the resolve of this PayloadResource.


        :return: The resolve of this PayloadResource.
        :rtype: Callable
        """
        return cls._mock

    @mock.setter
    def mock(cls, mock: bool):
        """Sets the mock of this PayloadResource.


        :param mock: The mock of this PayloadResource.
        :type meta: Callable
        """
        if mock is None:
            raise ValueError("Invalid value for `mock`, must not be `None`")  # noqa: E501

        cls._mock = mock