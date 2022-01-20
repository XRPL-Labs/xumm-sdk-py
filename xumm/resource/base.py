#!/usr/bin/env python
# coding: utf-8

import re
from cmath import e
from typing import Dict, Union, Any
from xumm import (
    client,
    error
)
from xumm.resource import XummResource

from .types import (
    KycInfoResponse,
    KycStatusResponse,
    PongResponse,
    CuratedAssetsResponse,
    XrplTransaction,
)

from xumm.resource.ping import PingResource
from xumm.resource.kyc_status import KycStatusResource
from xumm.resource.curated_assets import CuratedAssetsResource
from xumm.resource.xrpl_tx import XrplTxResource
from xumm.resource.payload import PayloadResource
from xumm.resource.storage import StorageResource


class XummSdk(XummResource):

    def refresh_from(cls, **kwargs):
        from xumm import api_key, api_secret

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
            
        cls.payload = PayloadResource()
        cls.storage = StorageResource()

    def ping(cls) -> PongResponse:
        """Returns the dict as a model

        :return: The PongResponse of this PongResponse.  # noqa: E501
        :rtype: PongResponse
        """
        
        res = client.get(PingResource.get_url())
        return PongResponse(**res)

    def get_kyc_status(cls, id: str=None) -> Union[KycInfoResponse, KycStatusResponse]:
        """Returns the dict as a model

        :return: The kyc_status of this kyc_status.  # noqa: E501
        :rtype: kyc_status
        """
        if re.match('^r', id.strip()):
            res = client.get(KycStatusResource.get_url(id))
            return KycInfoResponse(**res)
            # return call?.kycApproved ? 'SUCCESSFUL' : 'NONE'
        else:
            res = client.post(KycStatusResource.post_url(), {
                'user_token': id
            })
            return KycStatusResponse(**res)
            # return call?.kycStatus || 'NONE'

    def get_curated_assets(cls) -> CuratedAssetsResponse:
        """Returns the dict as a model

        :return: The CuratedAssetsResponse of this CuratedAssetsResponse.  # noqa: E501
        :rtype: CuratedAssetsResponse
        """
        
        res = client.get(CuratedAssetsResource.get_url())
        return CuratedAssetsResponse(**res)

    def get_transaction(cls, id: str=None) -> XrplTransaction:
        """Returns the dict as a model

        :return: The XrplTransaction of this XrplTransaction.  # noqa: E501
        :rtype: XrplTransaction
        """
        
        res = client.get(XrplTxResource.get_url(id))
        return XrplTransaction(**res)