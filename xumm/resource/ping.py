import os
from xumm import client
from xumm.resource import XummResource
from xumm.util import (
    cached_property,
)
import json
import time
import six


class Call(XummResource):

    swagger_types = {
        'uuidv4': 'str'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Call of this Call.  # noqa: E501
        :rtype: Call
        """
        cls.uuidv4 = kwargs['uuidv4']

    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.swagger_types):
            value = getattr(cls, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Call, dict):
            for key, value in cls.items():
                result[key] = value

        return result

    @property
    def uuidv4(self) -> str:
        """Gets the uuidv4 of this Call.


        :return: The uuidv4 of this Call.
        :rtype: str
        """
        return self._uuidv4

    @uuidv4.setter
    def uuidv4(self, uuidv4: str):
        """Sets the uuidv4 of this Call.


        :param uuidv4: The uuidv4 of this Call.
        :type uuidv4: str
        """
        if uuidv4 is None:
            raise ValueError("Invalid value for `uuidv4`, must not be `None`")  # noqa: E501

        self._uuidv4 = uuidv4

class Application(XummResource):

    swagger_types = {
        'name': 'str',
        'description': 'str',
        'uuidv4': 'str',
        'webhookurl': 'str',
        'disabled': 'int',
        'icon_url': 'str',
        'issued_user_token': 'str'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Application of this Application.  # noqa: E501
        :rtype: Application
        """
        cls._name = kwargs['name']
        cls._uuidv4 = kwargs['uuidv4']
        
        cls._description = None
        if 'description' in kwargs:
            cls._description = kwargs['description']
        cls._webhookurl = None
        if 'webhookurl' in kwargs:
            cls._webhookurl = kwargs['webhookurl']
        cls._disabled = None
        if 'disabled' in kwargs:
            cls._disabled = kwargs['disabled']
        cls._icon_url = None
        if 'icon_url' in kwargs:
            cls._icon_url = kwargs['icon_url']
        cls._issued_user_token = None
        if 'issued_user_token' in kwargs:
            cls._issued_user_token = kwargs['issued_user_token']
    
    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.swagger_types):
            value = getattr(cls, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Application, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def name(self) -> str:
        """Gets the name of this Application.


        :return: The name of this Application.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Application.


        :param name: The name of this Application.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this Application.


        :return: The description of this Application.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Application.


        :param description: The description of this Application.
        :type description: str
        """

        self._description = description

    @property
    def uuidv4(self) -> str:
        """Gets the uuidv4 of this Application.


        :return: The uuidv4 of this Application.
        :rtype: str
        """
        return self._uuidv4

    @uuidv4.setter
    def uuidv4(self, uuidv4: str):
        """Sets the uuidv4 of this Application.


        :param uuidv4: The uuidv4 of this Application.
        :type uuidv4: str
        """
        if uuidv4 is None:
            raise ValueError("Invalid value for `uuidv4`, must not be `None`")  # noqa: E501

        self._uuidv4 = uuidv4

    @property
    def webhookurl(self) -> str:
        """Gets the webhookurl of this Application.


        :return: The webhookurl of this Application.
        :rtype: str
        """
        return self._webhookurl

    @webhookurl.setter
    def webhookurl(self, webhookurl: str):
        """Sets the webhookurl of this Application.


        :param webhookurl: The webhookurl of this Application.
        :type webhookurl: str
        """

        self._webhookurl = webhookurl

    @property
    def disabled(self) -> int:
        """Gets the disabled of this Application.


        :return: The disabled of this Application.
        :rtype: int
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled: int):
        """Sets the disabled of this Application.


        :param disabled: The disabled of this Application.
        :type disabled: int
        """

        self._disabled = disabled

    @property
    def icon_url(self) -> str:
        """Gets the icon_url of this Application.


        :return: The icon_url of this Application.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url: str):
        """Sets the icon_url of this Application.


        :param icon_url: The icon_url of this Application.
        :type icon_url: str
        """

        self._icon_url = icon_url

    @property
    def issued_user_token(self) -> str:
        """Gets the issued_user_token of this Application.


        :return: The issued_user_token of this Application.
        :rtype: str
        """
        return self._issued_user_token

    @issued_user_token.setter
    def issued_user_token(self, issued_user_token: str):
        """Sets the issued_user_token of this Application.


        :param issued_user_token: The issued_user_token of this Application.
        :type issued_user_token: str
        """

        self._issued_user_token = issued_user_token

class Quota(XummResource):

    swagger_types = {
        'ratelimit': 'str'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Quota of this Quota.  # noqa: E501
        :rtype: Quota
        """
        # cls._ratelimit = None
        if 'ratelimit' in kwargs:
            cls._ratelimit = kwargs['ratelimit']
    
    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.swagger_types):
            value = getattr(cls, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Quota, dict):
            for key, value in cls.items():
                result[key] = value

        return result

    @property
    def ratelimit(self) -> str:
        """Gets the ratelimit of this Quota.


        :return: The ratelimit of this Quota.
        :rtype: str
        """
        return self._ratelimit

    @ratelimit.setter
    def ratelimit(self, ratelimit: str):
        """Sets the ratelimit of this Quota.


        :param ratelimit: The ratelimit of this Quota.
        :type ratelimit: str
        """
        if ratelimit is None:
            raise ValueError("Invalid value for `ratelimit`, must not be `None`")  # noqa: E501

        self._ratelimit = ratelimit


class Auth(XummResource):

    swagger_types = {
        'quota': 'Quota',
        'application': 'Application',
        'call': 'Call'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The PongResponse of this PongResponse.  # noqa: E501
        :rtype: PongResponse
        """
        cls._quota = {}
        if kwargs['quota'] != {}:
            cls._quota = Quota(**kwargs['quota'])
        cls._application = Application(**kwargs['application'])
        cls._call = Call(**kwargs['call'])

    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.swagger_types):
            value = getattr(cls, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Auth, dict):
            for key, value in cls.items():
                result[key] = value

        return result

    @property
    def quota(self) -> Quota:
        """Gets the quota of this Auth.


        :return: The quota of this Auth.
        :rtype: Quota
        """
        return self._quota

    @quota.setter
    def quota(self, quota: Quota):
        """Sets the quota of this Auth.


        :param quota: The quota of this Auth.
        :type quota: Quota
        """
        if quota is None:
            raise ValueError("Invalid value for `quota`, must not be `None`")  # noqa: E501

        self._quota = quota

    @property
    def application(self) -> Application:
        """Gets the application of this Auth.


        :return: The application of this Auth.
        :rtype: Application
        """
        return self._application

    @application.setter
    def application(self, application: Application):
        """Sets the application of this Auth.


        :param application: The application of this Auth.
        :type application: Application
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        self._application = application

    @property
    def call(self) -> Call:
        """Gets the call of this Auth.


        :return: The call of this Auth.
        :rtype: Call
        """
        return self._call

    @call.setter
    def call(self, call: Call):
        """Sets the call of this Auth.


        :param call: The call of this Auth.
        :type call: Call
        """
        if call is None:
            raise ValueError("Invalid value for `call`, must not be `None`")  # noqa: E501

        self._call = call


class PongResponse(XummResource):

    swagger_types = {
        'pong': 'bool',
        'auth': 'Auth'
    }

    @classmethod
    def get_url(cls):
        """get_url."""
        return super(PongResponse, cls).platform_url() + 'ping' + '/'
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PongResponse of this PongResponse.  # noqa: E501
        :rtype: PongResponse
        """
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._pong = kwargs['pong']
        cls._auth = Auth(**kwargs['auth'])

    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.swagger_types):
            value = getattr(cls, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PongResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return result

    @property
    def pong(self) -> bool:
        """Gets the pong of this PongResponse.


        :return: The pong of this PongResponse.
        :rtype: bool
        """
        return self._pong

    @pong.setter
    def pong(self, pong: bool):
        """Sets the pong of this PongResponse.


        :param pong: The pong of this PongResponse.
        :type pong: bool
        """
        if pong is None:
            raise ValueError("Invalid value for `pong`, must not be `None`")  # noqa: E501

        self._pong = pong
    
    @property
    def auth(self) -> Auth:
        """Gets the auth of this PongResponse.


        :return: The auth of this PongResponse.
        :rtype: Auth
        """
        return self._auth

    @auth.setter
    def auth(self, auth: Auth):
        """Sets the auth of this PongResponse.


        :param auth: The auth of this PongResponse.
        :type auth: Auth
        """
        if auth is None:
            raise ValueError("Invalid value for `auth`, must not be `None`")  # noqa: E501

        self._auth = auth
