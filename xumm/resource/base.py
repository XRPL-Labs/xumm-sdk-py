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
    PostPayloadResponse,  # noqa - avoid circular import
    DeletePayloadResponse,  # noqa - avoid circular import
    GetPayloadResponse,  # noqa - avoid circular import
)
from xumm.resource.storage import (
    SetStorageResponse,  # noqa - avoid circular import
    GetStorageResponse,  # noqa - avoid circular import
    DeleteStorageResponse,  # noqa - avoid circular import
)


class XummSdk(XummResource):

    def refresh_from(cls, **kwargs):
        print('BASE KWARGS: {}'.format(kwargs))

    # @cached_property
    def ping(cls):
        """Returns the dict as a model

        :return: The PongResponse of this PongResponse.  # noqa: E501
        :rtype: PongResponse
        """
        
        res = client.get(PongResponse.get_url())
        return PongResponse(**res)

    # @cached_property
    def curated_assets(cls):
        """Returns the dict as a model

        :return: The CuratedAssetsResponse of this CuratedAssetsResponse.  # noqa: E501
        :rtype: CuratedAssetsResponse
        """
        
        res = client.get(CuratedAssetsResponse.get_url())
        return CuratedAssetsResponse(**res)

    # @cached_property
    def kyc_status(cls):
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
    def payload_create(cls, payload):
        """Returns the dict as a model

        :return: The PostPayloadResponse of this PostPayloadResponse.  # noqa: E501
        :rtype: PostPayloadResponse
        """
        
        res = client.post(PostPayloadResponse.post_url(), payload)
        return PostPayloadResponse(**res)

    # @cached_property
    def payload_cancel(cls, id: str=None):
        """Returns the dict as a model

        :return: The DeletePayloadResponse of this DeletePayloadResponse.  # noqa: E501
        :rtype: DeletePayloadResponse
        """
        
        res = client.delete(DeletePayloadResponse.delete_url(id))
        return DeletePayloadResponse(**res)
        
    # @cached_property
    def payload_get(cls, id: str=None):
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