#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource

from .application_details import ApplicationDetails


class PongResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'pong': True,
        'auth': True
    }

    model_types = {
        'pong': bool,
        'auth': dict
    }

    attribute_map = {
        'pong': 'pong',
        'auth': 'auth',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PongResponse of this PongResponse.  # noqa: E501
        :rtype: PongResponse
        """
        cls.sanity_check(kwargs)
        cls._pong = None
        cls._auth = None
        cls.pong = kwargs['pong']
        cls.auth = ApplicationDetails(**kwargs['auth'])

    @property
    def pong(cls) -> bool:
        """Gets the pong of this PongResponse.


        :return: The pong of this PongResponse.
        :rtype: bool
        """
        return cls._pong

    @pong.setter
    def pong(cls, pong: bool):
        """Sets the pong of this PongResponse.


        :param pong: The pong of this PongResponse.
        :type pong: bool
        """
        if pong is None:
            raise ValueError("Invalid value for `pong`, must not be `None`")  # noqa: E501

        cls._pong = pong

    @property
    def auth(cls) -> ApplicationDetails:
        """Gets the auth of this PongResponse.


        :return: The auth of this PongResponse.
        :rtype: ApplicationDetails
        """
        return cls._auth

    @auth.setter
    def auth(cls, auth: ApplicationDetails):
        """Sets the auth of this PongResponse.


        :param auth: The auth of this PongResponse.
        :type auth: ApplicationDetails
        """
        if auth is None:
            raise ValueError("Invalid value for `auth`, must not be `None`")  # noqa: E501

        cls._auth = auth
