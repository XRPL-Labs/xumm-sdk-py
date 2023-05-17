#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class OAuth2TokenResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'access_token': True,
        'token_type': True,
        'expires_in': True,
        'refresh_token': False,
        'expires_at': True,
    }

    model_types = {
        'access_token': str,
        'token_type': str,
        'expires_in': int,
        'refresh_token': str,
        'expires_at': float,
    }

    attribute_map = {
        'access_token': 'access_token',
        'token_type': 'token_type',
        'expires_in': 'expires_in',
        'refresh_token': 'refresh_token',
        'expires_at': 'expires_at',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The OAuth2Response of this OAuth2Response.  # noqa: E501
        :rtype: OAuth2Response
        """
        cls.sanity_check(kwargs)
        cls._access_token = None
        cls._token_type = None
        cls._expires_in = None
        cls._refresh_token = None
        cls._expires_at = None
        cls.access_token = kwargs['access_token']
        cls.token_type = kwargs['token_type']
        cls.expires_in = kwargs['expires_in']
        cls.refresh_token = kwargs['refresh_token']
        cls.expires_at = kwargs['expires_at']

    @property
    def access_token(cls) -> str:
        """Gets the access_token of this OAuth2Response.


        :return: The access_token of this OAuth2Response.
        :rtype: str
        """
        return cls._access_token

    @access_token.setter
    def access_token(cls, access_token: str):
        """Sets the access_token of this OAuth2Response.


        :param access_token: The access_token of this OAuth2Response.
        :type access_token: str
        """
        if access_token is None:
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        cls._access_token = access_token

    @property
    def token_type(cls) -> str:
        """Gets the token_type of this OAuth2Response.


        :return: The token_type of this OAuth2Response.
        :rtype: str
        """
        return cls._token_type

    @token_type.setter
    def token_type(cls, token_type: str):
        """Sets the token_type of this OAuth2Response.


        :param token_type: The token_type of this OAuth2Response.
        :type token_type: str
        """
        if token_type is None:
            raise ValueError("Invalid value for `token_type`, must not be `None`")  # noqa: E501

        cls._token_type = token_type

    @property
    def expires_in(cls) -> int:
        """Gets the expires_in of this OAuth2Response.


        :return: The expires_in of this OAuth2Response.
        :rtype: int
        """
        return cls._expires_in

    @expires_in.setter
    def expires_in(cls, expires_in: int):
        """Sets the expires_in of this OAuth2Response.


        :param expires_in: The expires_in of this OAuth2Response.
        :type expires_in: int
        """
        if expires_in is None:
            raise ValueError("Invalid value for `expires_in`, must not be `None`")  # noqa: E501

        cls._expires_in = expires_in

    @property
    def refresh_token(cls) -> int:
        """Gets the refresh_token of this OAuth2Response.


        :return: The refresh_token of this OAuth2Response.
        :rtype: int
        """
        return cls._refresh_token

    @refresh_token.setter
    def refresh_token(cls, refresh_token: int):
        """Sets the refresh_token of this OAuth2Response.


        :param refresh_token: The refresh_token of this OAuth2Response.
        :type refresh_token: int
        """
        if refresh_token is None:
            raise ValueError("Invalid value for `refresh_token`, must not be `None`")  # noqa: E501

        cls._refresh_token = refresh_token

    @property
    def expires_at(cls) -> float:
        """Gets the expires_at of this OAuth2Response.


        :return: The expires_at of this OAuth2Response.
        :rtype: float
        """
        return cls._expires_at

    @expires_at.setter
    def expires_at(cls, expires_at: float):
        """Sets the expires_at of this OAuth2Response.


        :param expires_at: The expires_at of this OAuth2Response.
        :type expires_at: float
        """
        if expires_at is None:
            raise ValueError("Invalid value for `expires_at`, must not be `None`")  # noqa: E501

        cls._expires_at = expires_at
