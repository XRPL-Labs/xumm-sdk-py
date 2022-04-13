#!/usr/bin/env python
# coding: utf-8

from typing import List, Dict, Any  # noqa: F401

from xumm import client
from xumm.resource import XummResource

from .types import (
    OAuth2AuthResponse,
    # OAuth2TokenResponse,
    # OAuth2UserInfoResponse,
)


class OAuth2Resource(XummResource):

    @classmethod
    def auth_url(cls) -> str:
        """
        Gets the AUTH url of this OAuth2Resource

        :return: The AUTH url of this OAuth2Resource.
        :rtype: str
        """
        return super(OAuth2Resource, cls).oauth2_url() + 'auth'

    @classmethod
    def token_url(cls) -> str:
        """
        Gets the TOKEN url of this OAuth2Resource

        :return: The TOKEN url of this OAuth2Resource.
        :rtype: str
        """
        return super(OAuth2Resource, cls).oauth2_url() + 'token'

    @classmethod
    def userinfo_url(cls) -> str:
        """
        Gets the USERINFO url of this OAuth2Resource

        :return: The USERINFO url of this OAuth2Resource.
        :rtype: str
        """
        return super(OAuth2Resource, cls).oauth2_url() + 'userinfo'

    def refresh_from(cls, **kwargs) -> 'OAuth2Resource':
        return cls

    def auth(cls, data: Dict[str, object]) -> OAuth2AuthResponse:
        """Returns the dict as a model

        :return: The OAuth2AuthResponse of this OAuth2AuthResponse.  # noqa: E501
        :rtype: OAuth2AuthResponse
        """

        res = client.auth(cls.auth_url(), data)
        return OAuth2AuthResponse(**res)

    # def token(cls) -> OAuth2TokenResponse:
    #     """Returns the dict as a model

    #     :return: The OAuth2TokenResponse of this OAuth2TokenResponse.  # noqa: E501
    #     :rtype: OAuth2TokenResponse
    #     """

    #     res = client.get(cls.get_url())
    #     return OAuth2TokenResponse(**res)

    # def userinfo(cls) -> OAuth2UserInfoResponse:
    #     """Returns the dict as a model

    #     :return: The OAuth2UserInfoResponse of this OAuth2UserInfoResponse.  # noqa: E501
    #     :rtype: OAuth2UserInfoResponse
    #     """

    #     res = client.delete(cls.delete_url())
    #     return OAuth2UserInfoResponse(**res)
