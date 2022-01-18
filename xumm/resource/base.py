from cmath import e
import os
from typing import Dict, Union, Any
from xumm import (
    client,
    error
)
from xumm.resource import XummResource
import json
import time
import re
import websocket

from xumm.ws_client import WSClient
from xumm.resource.ping import PingRequest
from xumm.resource.curated_assets import GetCuratedAssetsRequest
from xumm.resource.kyc_status import (
    GetKycStatusRequest,
    PostKycStatusRequest,
)
from xumm.resource.xrpl_tx import GetXrplTxRequest
from xumm.resource.payload import (
    PostPayloadRequest,
    DeletePayloadRequest,
    GetPayloadRequest,
    PayloadSubscription,
)
from xumm.resource.storage import (
    StorageSetRequest,
    StorageGetRequest,
    StorageDeleteRequest
)

from .types import (
    CreatedPayload,
    XummPayload,
    XummPostPayloadBodyJson,
    XummPostPayloadBodyBlob,
    XummJsonTransaction,
    XummPostPayloadResponse,
    XummDeletePayloadResponse,
    XummGetPayloadResponse,
    StorageSetResponse,
    StorageGetResponse,
    StorageDeleteResponse,
    CuratedAssetsResponse,
    KycInfoResponse,
    KycStatusResponse,
    PongResponse,
    XrplTransaction,
)


def resolve_payload(payload: Union[str, XummPayload, CreatedPayload]) -> XummPayload:
    if isinstance(payload, str):
        return client.payload_get(payload)
    if isinstance(payload, CreatedPayload):
        return client.payload_get(payload.uuid)
    if isinstance(payload, XummPayload):
        return payload

    raise error.APIError('Could not resolve payload (not found)')

class XummSdk(XummResource):

    def refresh_from(cls, **kwargs):
        from xumm import api_key, api_secret

        # print(api_key)
        # print(api_secret)

        if api_key is None:
            raise error.AuthenticationError(
                'No API key provided. (HINT: set your API key using '
                '"xumm.api_key = <API-KEY>"). You can generate API keys '
                'from the Xumm web interface.'
            )
        if api_secret is None:
            raise error.AuthenticationError(
                'No API secret provided. (HINT: set your API key using '
                '"xumm.api_secret = <API-SECRET>"). You can generate API keys '
                'from the Xumm web interface.'
            )
        # print('BASE KWARGS: {}'.format(kwargs))

    def ping(cls) -> PongResponse:
        """Returns the dict as a model

        :return: The PongResponse of this PongResponse.  # noqa: E501
        :rtype: PongResponse
        """
        
        res = client.get(PingRequest.get_url())
        return PongResponse(**res)

    def curated_assets(cls) -> CuratedAssetsResponse:
        """Returns the dict as a model

        :return: The CuratedAssetsResponse of this CuratedAssetsResponse.  # noqa: E501
        :rtype: CuratedAssetsResponse
        """
        
        res = client.get(GetCuratedAssetsRequest.get_url())
        return CuratedAssetsResponse(**res)

    def kyc_status(cls, id: str=None) -> Union[KycInfoResponse, KycStatusResponse]:
        """Returns the dict as a model

        :return: The kyc_status of this kyc_status.  # noqa: E501
        :rtype: kyc_status
        """
        if re.match('^r', id.strip()):
            res = client.get(GetKycStatusRequest.get_url(id))
            return KycInfoResponse(**res)
            # return call?.kycApproved ? 'SUCCESSFUL' : 'NONE'
        else:
            res = client.post(PostKycStatusRequest.post_url(), {
                'user_token': id
            })
            return KycStatusResponse(**res)
            # return call?.kycStatus || 'NONE'

    def xrpl_tx(cls, id: str=None) -> XrplTransaction:
        """Returns the dict as a model

        :return: The XrplTransaction of this XrplTransaction.  # noqa: E501
        :rtype: XrplTransaction
        """
        
        res = client.get(GetXrplTxRequest.get_url(id))
        return XrplTransaction(**res)

    # TODO: USE PAYLOAD MODEL
    def payload_create(
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
                res = client.post(PostPayloadRequest.post_url(), payload)
                return XummPostPayloadResponse(**res)
            except:
                return None

        res = client.post(PostPayloadRequest.post_url(), payload)
        return XummPostPayloadResponse(**res)

    def payload_cancel(cls, id: str=None) -> XummDeletePayloadResponse:
        """Returns the dict as a model

        :return: The XummDeletePayloadResponse of this XummDeletePayloadResponse.  # noqa: E501
        :rtype: XummDeletePayloadResponse
        """
        
        res = client.delete(DeletePayloadRequest.delete_url(id))
        return XummDeletePayloadResponse(**res)
        
    def payload_get(cls, id: str=None) -> XummGetPayloadResponse:
        """Returns the dict as a model

        :return: The XummGetPayloadResponse of this XummGetPayloadResponse.  # noqa: E501
        :rtype: XummGetPayloadResponse
        """
        
        res = client.get(GetPayloadRequest.get_url(id))
        return XummGetPayloadResponse(**res)

    # TODO: USE PAYLOAD MODEL
    def storage_set(cls, data) -> StorageSetResponse:
        """Returns the dict as a model

        :return: The StorageSetResponse of this StorageSetResponse.  # noqa: E501
        :rtype: StorageSetResponse
        """
        
        res = client.post(StorageSetRequest.post_url(), data)
        return StorageSetResponse(**res)

    def storage_get(cls) -> StorageGetResponse:
        """Returns the dict as a model

        :return: The StorageGetResponse of this StorageGetResponse.  # noqa: E501
        :rtype: StorageGetResponse
        """
        
        res = client.get(StorageGetRequest.get_url())
        return StorageGetResponse(**res)

    def storage_delete(cls) -> StorageDeleteResponse:
        """Returns the dict as a model

        :return: The StorageDeleteResponse of this StorageDeleteResponse.  # noqa: E501
        :rtype: StorageDeleteResponse
        """
        
        res = client.delete(StorageDeleteRequest.delete_url())
        return StorageDeleteResponse(**res)

    def __unicode__(cls):
        return '<{} {}>'.format(cls.__class__.__name__, cls.id)

class CallbackPromise:

    def __init__(cls):
        cls.data: object = None
        
    def _resolve(cls, resolveData):
        cls.data = resolveData
        return cls.data

    async def _resolved(cls):
        return cls.data
        
import logging

class XummWs(XummResource):

    def refresh_from(cls, **kwargs):
        cls._conn = None
        cls._callback = None
        cls._mock = True

    @classmethod
    async def subscribe(
        cls, 
        client: XummSdk, 
        payload: Union[str, XummPayload, CreatedPayload], 
        callback
    ) -> PayloadSubscription:
        """Subscribe to a channel
        :returns: PayloadSubscription
        """

        callback_promise = CallbackPromise()
        
        payload_details = resolve_payload(payload)

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
            raise error

        # def on_close(ws, close_status_code, close_msg):
        def on_close(close_status_code, close_msg):
            print('Payload {}: Subscription ended (WebSocket closed)'.format(payload_details.meta.uuid))

        def on_open(connection):
            print(connection)
            print('Payload {}: Subscription active (WebSocket opened)'.format(payload_details.meta.uuid))

        if payload_details:
            cls._callback = callback
            cls._mock = False
            cls._conn = WSClient(
                # server='ws://localhost:8765',
                # log_level=logging.DEBUG,
                server='ws://localhost:8765' if cls._mock else 'wss://xumm.app/sign/{}'.format(payload_details.meta.uuid),
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

        # throwIfError(payloadDetails)

        # raise ValueError('Could not subscribe: could not fetch payload')

    @classmethod
    async def create_subscribe(
        cls, 
        client: XummSdk, 
        payload: CreatedPayload, 
        callback
    ) -> PayloadSubscription:
        """Create payload and subscribe to a channel
        :returns: PayloadSubscription
        """

        created_payload = await client.payload_create(payload)
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
        cls._conn.close()