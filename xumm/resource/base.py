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
)


class XummSdk(XummResource):

    def refresh_from(cls, **kwargs):
        print('BASE KWARGS: {}'.format(kwargs))
        # p = re.compile('^[a-f0-9]{8}\-[a-f0-9]{4}\-[a-f0-9]{4}\-[a-f0-9]{4}\-[a-f0-9]{12}$')
        # cls.application = kwargs['application']
        # cls.custom_meta = kwargs['custom_meta']
        # cls.meta = kwargs['meta']
        # cls.payload = kwargs['payload']
        # cls.response = kwargs['response']
        # print(p.match(api_key))
        # print(p.match(api_secret))
        # if not p.match(api_key) or  not p.match(api_secret):
        #     raise error.AuthenticationError(
        #         'Invalid API key provided. (HINT: set your API key using '
        #         '"xumm.api_key = <API-KEY>"). You can generate API keys '
        #         'from the Xumm web interface.'
        #     )

    # def to_any_object(cls):
    #     return {
    #         'application': cls.application,
    #         'custom_meta': cls.custom_meta,
    #         'meta': cls.meta,
    #         'payload': cls.payload,
    #         'response': cls.response,
    #     }

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
    def xrpl_tx(cls, id):
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
    def payload_cancel(cls, id):
        """Returns the dict as a model

        :return: The DeletePayloadResponse of this DeletePayloadResponse.  # noqa: E501
        :rtype: DeletePayloadResponse
        """
        
        res = client.delete(DeletePayloadResponse.delete_url(id))
        return DeletePayloadResponse(**res)

    def __unicode__(cls):
        return '<{} {}>'.format(cls.__class__.__name__, cls.id)