#!/usr/bin/env python
# coding: utf-8

from typing import List, Dict, Any, Tuple  # noqa: F401

from xumm.resource import XummResource

from requests_oauthlib import OAuth2Session

from .types import OAuth2TokenResponse


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

    # @classmethod
    # def userinfo_url(cls) -> str:
    #     """
    #     Gets the USERINFO url of this OAuth2Resource

    #     :return: The USERINFO url of this OAuth2Resource.
    #     :rtype: str
    #     """
    #     return super(OAuth2Resource, cls).oauth2_url() + 'userinfo'

    def refresh_from(cls, **kwargs) -> 'OAuth2Resource':
        return cls

    def auth(cls, redirect_uri: str) -> Tuple[str, str]:
        """Returns the dict as a model

        :return: The authorization url and the state.  # noqa: E501
        :rtype: Tuple[str, str]
        """
        from xumm import api_key
        oauth = OAuth2Session(api_key, redirect_uri=redirect_uri)
        return oauth.authorization_url(cls.auth_url())

    def token(cls, authorization_response: str) -> OAuth2TokenResponse:
        """Returns the dict as a model

        :return: The OAuth2TokenResponse of this OAuth2TokenResponse.  # noqa: E501
        :rtype: OAuth2TokenResponse
        """

        from xumm import api_key, api_secret
        oauth = OAuth2Session(api_key)
        token = oauth.fetch_token(
            cls.token_url(),
            client_secret=api_secret,
            authorization_response=authorization_response
        )
        return OAuth2TokenResponse(**token)

    # def userinfo(cls) -> OAuth2UserInfoResponse:
    #     """Returns the dict as a model

    #     :return: The OAuth2UserInfoResponse of this OAuth2UserInfoResponse.  # noqa: E501
    #     :rtype: OAuth2UserInfoResponse
    #     """

    #     res = client.delete(cls.delete_url())
    #     return OAuth2UserInfoResponse(**res)
