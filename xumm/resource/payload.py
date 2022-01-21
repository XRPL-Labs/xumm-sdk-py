#!/usr/bin/env python
# coding: utf-8

import logging
from typing import List, Dict, Any, Union, Callable  # noqa: F401
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
    PayloadAndSubscription,
    on_payload_event
)

from xumm.ws_client import WSClient

logger = logging.getLogger('app')


class CallbackPromise:

    resolved = None
    error = None
    data = None

    def in_res(cls, args):
        cls.data = args
        return args

    def in_rej(cls, error):
        cls.error = error
        return error

    def __init__(cls):
        cls.resolve_fn = cls.in_res
        cls.reject_fn = cls.in_res
        cls.data = None

    def _resolve(cls, arg: Any):
        cls.resolve_fn(arg)

    def _reject(cls, error):
        cls.reject_fn(error)

    async def _resolved(cls):
        while not cls.data and not cls.error:
            continue

        if cls.error:
            return None

        return cls.data

# class CallbackPromise:

#     resolved = None
#     args = None
#     kwargs = None

#     def in_res(cls, *args, **kwargs):
#         cls.args = args
#         cls.kwargs = kwargs
#         return cls

#     def __init__(cls, *args, **kwargs):
#         cls.resolve_fn = cls.in_res
#         cls.data = None

#     def _resolve(cls, *args, **kwargs):
#         cls.resolve_fn(*args, **kwargs)

#     async def _resolved(cls):
#         while not cls.args or not cls.kwargs:
#             continue

#         return cls.args, cls.kwargs


class PayloadResource(XummResource):

    _conn: WSClient = None
    _callback: Callable = None

    @classmethod
    def post_url(cls) -> str:
        """post_url."""
        return super(PayloadResource, cls).platform_url() + 'payload' + '/'

    @classmethod
    def get_url(cls, id: str = None) -> str:
        """get_url."""
        return super(PayloadResource, cls).platform_url() + 'payload' + '/' + id  # noqa: E501

    @classmethod
    def delete_url(cls, id: str = None) -> str:
        """delete_url."""
        return super(PayloadResource, cls).platform_url() + 'payload' + '/' + id  # noqa: E501

    def refresh_from(cls, **kwargs) -> 'PayloadResource':
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
        payload: Union[
            XummPostPayloadBodyJson,
            XummPostPayloadBodyBlob,
            XummJsonTransaction
        ],
        return_errors: bool = False
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
            except:  # noqa: E722
                return None

        res = client.post(cls.post_url(), payload)
        return XummPostPayloadResponse(**res)

    @classmethod
    def cancel(
        cls,
        id: str = None,
        return_errors: bool = False
    ) -> XummDeletePayloadResponse:
        """Returns the dict as a model

        :return: The XummDeletePayloadResponse of this XummDeletePayloadResponse.  # noqa: E501
        :rtype: XummDeletePayloadResponse
        """

        if not return_errors:
            try:
                res = client.delete(cls.delete_url(id))
                return XummDeletePayloadResponse(**res)
            except:  # noqa: E722
                return None

        res = client.delete(cls.delete_url(id))
        return XummDeletePayloadResponse(**res)

    @classmethod
    def get(
        cls,
        id: str = None,
        return_errors: bool = False
    ) -> XummGetPayloadResponse:
        """Returns the dict as a model

        :return: The XummGetPayloadResponse of this XummGetPayloadResponse.  # noqa: E501
        :rtype: XummGetPayloadResponse
        """

        if not return_errors:
            try:
                res = client.get(cls.get_url(id))
                return XummGetPayloadResponse(**res)
            except:  # noqa: E722
                return None

        res = client.get(cls.get_url(id))
        return XummGetPayloadResponse(**res)

    @classmethod
    async def subscribe(
        cls,
        payload: Union[str, XummPayload, CreatedPayload],
        callback: on_payload_event
    ) -> PayloadSubscription:
        """Subscribe to a channel
        :returns: PayloadSubscription
        """
        from xumm import env

        callback_promise = CallbackPromise()
        payload_details = cls.resolve_payload(payload)

        def on_message(json_data):
            if json_data and cls._callback and 'devapp_fetched' not in json_data:  # noqa: E501
                try:
                    callback_result = cls._callback({
                        'uuid': payload_details.meta.uuid,
                        'data': json_data,
                        'resolve': callback_promise._resolve,
                        'payload': payload_details
                    })

                    if callback_result:
                        callback_promise._resolve(callback_result)

                except Exception as e:
                    logger.debug('Payload {}: Callback exception: {}'.format(payload_details.meta.uuid, e))  # noqa: E501

        def on_error(error):
            logger.debug('Payload {}: Subscription error: {}'.format(payload_details.meta.uuid, error))  # noqa: E501
            cls._conn.disconnect()
            callback_promise._reject(error)
            # raise ValueError(error)

        # def on_close(ws, close_status_code, close_msg):
        def on_close():
            logger.debug('Payload {}: Subscription ended (WebSocket closed)'.format(payload_details.meta.uuid))  # noqa: E501

        def on_open(connection):
            logger.debug('Payload {}: Subscription active (WebSocket opened)'.format(payload_details.meta.uuid))  # noqa: E501

        if payload_details:
            cls._callback = callback
            cls._conn = WSClient(
                log_level=logging.ERROR if env == 'sandbox' else logging.ERROR,
                server='ws://localhost:8765' if env == 'sandbox' else 'wss://xumm.app/sign/{}'.format(payload_details.meta.uuid),  # noqa: E501
                on_response=on_message,
                on_error=on_error,
                on_close=on_close,
                on_open=on_open
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
        callback: on_payload_event
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
        raise ValueError('Error creating payload or subscribing to created payload')  # noqa: E501

    @classmethod
    def unsubscribe(cls):
        """Unsubscribe to a channel
        :returns: None
        """
        cls._conn.disconnect()
