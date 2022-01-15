import os
from xumm import (
    client, 
    api_key, 
    api_secret,
    error
)
from xumm.resource import XummResource
from xumm.util import (
    cached_property,
)
import json
import time
import re

from xumm.resource.ping import PongResponse  # noqa - avoid circular import
from xumm.resource.curated_assets import CuratedAssetsResponse  # noqa - avoid circular import
from xumm.resource.kyc_status import KYCStatusResponse  # noqa - avoid circular import
from xumm.resource.xrpl_tx import XRPLTxResponse  # noqa - avoid circular import
from xumm.resource.payload import (
    PayloadSubscription,
    PostPayloadResponse,  # noqa - avoid circular import
    DeletePayloadResponse,  # noqa - avoid circular import
    GetPayloadResponse,  # noqa - avoid circular import
    Payload  # noqa - avoid circular import
)
from xumm.resource.storage import (
    SetStorageResponse,  # noqa - avoid circular import
    GetStorageResponse,  # noqa - avoid circular import
    DeleteStorageResponse  # noqa - avoid circular import
)

import websocket



class XummSdk(XummResource):

    def refresh_from(cls, **kwargs):
        print('BASE KWARGS: {}'.format(kwargs))

    # @cached_property
    def ping(cls) -> PongResponse:
        """Returns the dict as a model

        :return: The PongResponse of this PongResponse.  # noqa: E501
        :rtype: PongResponse
        """
        
        res = client.get(PongResponse.get_url())
        return PongResponse(**res)

    # @cached_property
    def curated_assets(cls) -> CuratedAssetsResponse:
        """Returns the dict as a model

        :return: The CuratedAssetsResponse of this CuratedAssetsResponse.  # noqa: E501
        :rtype: CuratedAssetsResponse
        """
        
        res = client.get(CuratedAssetsResponse.get_url())
        return CuratedAssetsResponse(**res)

    # @cached_property
    def kyc_status(cls) -> KYCStatusResponse:
        """Returns the dict as a model

        :return: The KYCStatusResponse of this KYCStatusResponse.  # noqa: E501
        :rtype: KYCStatusResponse
        """
        
        res = client.get(KYCStatusResponse.get_url())
        return KYCStatusResponse(**res)

    # @cached_property
    def xrpl_tx(cls, id: str=None):
        """Returns the dict as a model

        :return: The XRPLTxResponse of this XRPLTxResponse.  # noqa: E501
        :rtype: XRPLTxResponse
        """
        
        res = client.get(XRPLTxResponse.get_url(id))
        return XRPLTxResponse(**res)

    # @cached_property
    def payload_create(cls, payload) -> PostPayloadResponse:
        """Returns the dict as a model

        :return: The PostPayloadResponse of this PostPayloadResponse.  # noqa: E501
        :rtype: PostPayloadResponse
        """
        
        res = client.post(PostPayloadResponse.post_url(), payload)
        return PostPayloadResponse(**res)

    # @cached_property
    def payload_cancel(cls, id: str=None) -> DeletePayloadResponse:
        """Returns the dict as a model

        :return: The DeletePayloadResponse of this DeletePayloadResponse.  # noqa: E501
        :rtype: DeletePayloadResponse
        """
        
        res = client.delete(DeletePayloadResponse.delete_url(id))
        return DeletePayloadResponse(**res)
        
    # @cached_property
    def payload_get(cls, id: str=None) -> GetPayloadResponse:
        """Returns the dict as a model

        :return: The GetPayloadResponse of this GetPayloadResponse.  # noqa: E501
        :rtype: GetPayloadResponse
        """
        
        res = client.get(GetPayloadResponse.get_url(id))
        return GetPayloadResponse(**res)

    # @cached_property
    def storage_set(cls, data):
        """Returns the dict as a model

        :return: The SetStorageResponse of this SetStorageResponse.  # noqa: E501
        :rtype: SetStorageResponse
        """
        
        res = client.post(SetStorageResponse.post_url(), data)
        return SetStorageResponse(**res)

    # @cached_property
    def storage_get(cls):
        """Returns the dict as a model

        :return: The GetStorageResponse of this GetStorageResponse.  # noqa: E501
        :rtype: GetStorageResponse
        """
        
        res = client.get(GetStorageResponse.get_url())
        return GetStorageResponse(**res)

    # @cached_property
    def storage_delete(cls):
        """Returns the dict as a model

        :return: The DeleteStorageResponse of this DeleteStorageResponse.  # noqa: E501
        :rtype: DeleteStorageResponse
        """
        
        res = client.delete(DeleteStorageResponse.delete_url())
        return DeleteStorageResponse(**res)

    def __unicode__(cls):
        return '<{} {}>'.format(cls.__class__.__name__, cls.id)

class CallbackPromise:

    def __init__(cls):
        cls.data = None
        
    def _resolve(cls, resolveData: any):
        cls.data = resolveData
        return cls.data

    async def _resolved(cls):
        return cls.data
        
class XummWs(XummResource):

    def refresh_from(cls, **kwargs):
        cls._callback = None
        cls._conn = None
        cls._sock = None

    @classmethod
    async def subscribe(
        cls, 
        client: XummSdk, 
        payload: Payload, 
        callback
    ) -> PayloadSubscription:

        callback_promise = CallbackPromise()

        # TODO: add this to payload functions
        def resolve_payload(payload):
            if isinstance(payload, str):
                return client.payload_get(payload)
            if isinstance(payload, Payload):
                return payload
        
        payload_details = resolve_payload(payload)

        def on_message(ws, msg):
            json_data: dict(str, object)
            try:
                json_data = json.loads(msg)
            except Exception as e:
                print('Payload {}: Received message, unable to parse as JSON: {}'.format(payload_details.meta.uuid, e))
            
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
                    raise e

        def on_error(ws, error):
            raise error

        def on_close(ws, close_status_code, close_msg):
            print('Payload {}: Subscription ended (WebSocket closed)'.format(payload_details.meta.uuid))

        def on_open(ws):
            cls._sock = ws.sock
            print('Payload {}: Subscription active (WebSocket opened)'.format(payload_details.meta.uuid))

        if payload_details:
            # self = XummWsClient()
            # websocket.enableTrace(True)
            cls._callback = callback
            cls._conn = websocket.WebSocketApp(
                # 'wss://xumm.app/sign/'.format(payload_details.meta.uuid),
                # 'wss://xumm.app/sign/'.format(payload),
                # 'ws://xumm.local/{}'.format(payload_details.meta.uuid),
                'ws://localhost:8765',
                on_message = on_message,
                on_error = on_error,
                on_close = on_close
            )
            cls._conn.on_open = on_open
            cls._conn.run_forever()
            
            cls._conn.sock = cls._sock
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
        payload: Payload, 
        callback
    ) -> PayloadSubscription:

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