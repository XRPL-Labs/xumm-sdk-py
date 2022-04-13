#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource

# from .oauth2_response import StorageResponse


class OAuth2AuthResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'client_id': True,
        'client_secret': True,
        'response_type': True,
        'redirect_uri': True,
        'state': True,
        'nonce': True,
    }

    model_types = {
        'client_id': str,
        'client_secret': str,
        'response_type': str,
        'redirect_uri': str,
        'state': str,
        'nonce': str,
    }

    attribute_map = {
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'response_type': 'response_type',
        'redirect_uri': 'redirect_uri',
        'state': 'state',
        'nonce': 'nonce',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The OAuth2AuthResponse of this OAuth2AuthResponse.  # noqa: E501
        :rtype: OAuth2AuthResponse
        """
        print(kwargs)
        cls.sanity_check(kwargs)
        cls._client_id = None
        cls._client_secret = None
        cls._response_type = None
        cls._redirect_uri = None
        cls._state = None
        cls._nonce = None
        cls.client_id = kwargs['client_id']
        cls.client_secret = kwargs['client_secret']
        cls.response_type = kwargs['response_type']
        cls.redirect_uri = kwargs['redirect_uri']
        cls.state = kwargs['state']
        cls.nonce = kwargs['nonce']

    @property
    def client_id(self) -> str:
        """Gets the client_id of this OAuth2AuthResponse.


        :return: The client_id of this OAuth2AuthResponse.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: str):
        """Sets the client_id of this OAuth2AuthResponse.


        :param client_id: The client_id of this OAuth2AuthResponse.
        :type client_id: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self) -> str:
        """Gets the client_secret of this OAuth2AuthResponse.


        :return: The client_secret of this OAuth2AuthResponse.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret: str):
        """Sets the client_secret of this OAuth2AuthResponse.


        :param client_secret: The client_secret of this OAuth2AuthResponse.
        :type client_secret: str
        """
        if client_secret is None:
            raise ValueError("Invalid value for `client_secret`, must not be `None`")  # noqa: E501

        self._client_secret = client_secret

    @property
    def response_type(self) -> str:
        """Gets the response_type of this OAuth2AuthResponse.


        :return: The response_type of this OAuth2AuthResponse.
        :rtype: str
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type: str):
        """Sets the response_type of this OAuth2AuthResponse.


        :param response_type: The response_type of this OAuth2AuthResponse.
        :type response_type: str
        """
        if response_type is None:
            raise ValueError("Invalid value for `response_type`, must not be `None`")  # noqa: E501

        self._response_type = response_type

    @property
    def redirect_uri(self) -> str:
        """Gets the redirect_uri of this OAuth2AuthResponse.


        :return: The redirect_uri of this OAuth2AuthResponse.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri: str):
        """Sets the redirect_uri of this OAuth2AuthResponse.


        :param redirect_uri: The redirect_uri of this OAuth2AuthResponse.
        :type redirect_uri: str
        """
        if redirect_uri is None:
            raise ValueError("Invalid value for `redirect_uri`, must not be `None`")  # noqa: E501

        self._redirect_uri = redirect_uri

    @property
    def state(self) -> str:
        """Gets the state of this OAuth2AuthResponse.


        :return: The state of this OAuth2AuthResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this OAuth2AuthResponse.


        :param state: The state of this OAuth2AuthResponse.
        :type state: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def nonce(self) -> str:
        """Gets the nonce of this OAuth2AuthResponse.


        :return: The nonce of this OAuth2AuthResponse.
        :rtype: str
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce: str):
        """Sets the nonce of this OAuth2AuthResponse.


        :param nonce: The nonce of this OAuth2AuthResponse.
        :type nonce: str
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce
