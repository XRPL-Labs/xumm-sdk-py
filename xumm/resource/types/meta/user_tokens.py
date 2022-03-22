#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource
from typing import List


class UserTokenValidity(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'user_token': True,
        'active': True,
        'token_issued': True,
        'token_expiration': True
    }

    model_types = {
        'user_token': str,
        'active': bool,
        'token_issued': int,
        'token_expiration': int
    }

    attribute_map = {
        'user_token': 'user_token',
        'active': 'active',
        'token_issued': 'token_issued',
        'token_expiration': 'token_expiration'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The UserToken of this UserToken.  # noqa: E501
        :rtype: UserToken
        """
        cls.sanity_check(kwargs)
        cls._user_token = None
        cls._active = None
        cls._token_issued = None
        cls._token_expiration = None
        cls.user_token = kwargs['user_token']
        cls.active = kwargs['active']
        cls.token_issued = kwargs['token_issued']
        cls.token_expiration = kwargs['token_expiration']
        return cls

    @property
    def user_token(cls) -> str:
        """Gets the user_token of this UserTokenValidity.


        :return: The user_token of this UserTokenValidity.
        :rtype: str
        """
        return cls._user_token

    @user_token.setter
    def user_token(cls, user_token: str):
        """Sets the user_token of this UserTokenValidity.


        :param user_token: The user_token of this UserTokenValidity.
        :type user_token: str
        """
        if user_token is None:
            raise ValueError("Invalid value for `user_token`, must not be `None`")  # noqa: E501

        cls._user_token = user_token

    @property
    def active(cls) -> str:
        """Gets the active of this UserTokenValidity.


        :return: The active of this UserTokenValidity.
        :rtype: str
        """
        return cls._active

    @active.setter
    def active(cls, active: str):
        """Sets the active of this UserTokenValidity.


        :param active: The active of this UserTokenValidity.
        :type active: str
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        cls._active = active

    @property
    def token_issued(cls) -> int:
        """Gets the token_issued of this UserTokenValidity.


        :return: The token_issued of this UserTokenValidity.
        :rtype: int
        """
        return cls._token_issued

    @token_issued.setter
    def token_issued(cls, token_issued: int):
        """Sets the token_issued of this UserTokenValidity.


        :param token_issued: The token_issued of this UserTokenValidity.
        :type token_issued: int
        """
        if token_issued is None:
            raise ValueError("Invalid value for `token_issued`, must not be `None`")  # noqa: E501

        cls._token_issued = token_issued

    @property
    def token_expiration(cls) -> int:
        """Gets the token_expiration of this UserTokenValidity.


        :return: The token_expiration of this UserTokenValidity.
        :rtype: int
        """
        return cls._token_expiration

    @token_expiration.setter
    def token_expiration(cls, token_expiration: int):
        """Sets the token_expiration of this UserTokenValidity.


        :param token_expiration: The token_expiration of this UserTokenValidity.  # noqa: E501
        :type token_expiration: int
        """
        if token_expiration is None:
            raise ValueError("Invalid value for `token_expiration`, must not be `None`")  # noqa: E501

        cls._token_expiration = token_expiration


class UserTokenResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'tokens': True,
    }

    model_types = {
        'tokens': list,
    }

    attribute_map = {
        'tokens': 'tokens',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserTokenResponse of this UserTokenResponse.  # noqa: E501
        :rtype: UserTokenResponse
        """
        cls.sanity_check(kwargs)
        cls._tokens = None
        cls.tokens = [UserTokenValidity(**t) for t in kwargs['tokens']]

    @property
    def tokens(cls) -> List[UserTokenValidity]:
        """Gets the tokens of this UserTokenResponse.


        :return: The tokens of this UserTokenResponse.
        :rtype: List[UserTokenValidity]
        """
        return cls._tokens

    @tokens.setter
    def tokens(cls, tokens: List[UserTokenValidity]):
        """Sets the tokens of this UserTokenResponse.


        :param tokens: The tokens of this UserTokenResponse.
        :type tokens: List[UserTokenValidity]
        """
        if tokens is None:
            raise ValueError("Invalid value for `tokens`, must not be `None`")  # noqa: E501

        cls._tokens = tokens
