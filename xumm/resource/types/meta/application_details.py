#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource
import six
from typing import Union, List, Dict, Callable, Any  # noqa: F401


class Call(XummResource):

    required = {
        'uuidv4': True
    }

    model_types = {
        'uuidv4': str
    }

    attribute_map = {
        'uuidv4': 'uuidv4',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Call of this Call.  # noqa: E501
        :rtype: Call
        """
        cls.sanity_check(kwargs)
        cls._uuidv4 = None
        cls.uuidv4 = kwargs['uuidv4']

    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.model_types):
            value = getattr(cls, attr)
            attr = cls.attribute_map[attr]
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

        return {k: v for k, v in result.items() if v is not None}

    @property
    def uuidv4(cls) -> str:
        """Gets the uuidv4 of this Call.


        :return: The uuidv4 of this Call.
        :rtype: str
        """
        return cls._uuidv4

    @uuidv4.setter
    def uuidv4(cls, uuidv4: str):
        """Sets the uuidv4 of this Call.


        :param uuidv4: The uuidv4 of this Call.
        :type uuidv4: str
        """
        if uuidv4 is None:
            raise ValueError("Invalid value for `uuidv4`, must not be `None`")  # noqa: E501

        cls._uuidv4 = uuidv4

class Application(XummResource):

    required = {
        'name': True,
        'uuidv4': True,
        'webhookurl': True,
        'disabled': True
    }

    model_types = {
        'name': str,
        'uuidv4': str,
        'webhookurl': str,
        'disabled': int
    }

    attribute_map = {
        'name': 'name',
        'uuidv4': 'uuidv4',
        'webhookurl': 'webhookurl',
        'disabled': 'disabled'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Application of this Application.  # noqa: E501
        :rtype: Application
        """
        cls.sanity_check(kwargs)
        cls._name = None
        cls._uuidv4 = None
        cls._webhookurl = None
        cls._disabled = None
        cls.name = kwargs['name']
        cls.uuidv4 = kwargs['uuidv4']
        cls.webhookurl = kwargs['webhookurl']
        cls.disabled = kwargs['disabled']
    
    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.attribute_map):
            value = getattr(cls, attr)
            attr = cls.attribute_map[attr]
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
    def name(cls) -> str:
        """Gets the name of this Application.


        :return: The name of this Application.
        :rtype: str
        """
        return cls._name

    @name.setter
    def name(cls, name: str):
        """Sets the name of this Application.


        :param name: The name of this Application.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        cls._name = name

    @property
    def description(cls) -> str:
        """Gets the description of this Application.


        :return: The description of this Application.
        :rtype: str
        """
        return cls._description

    @description.setter
    def description(cls, description: str):
        """Sets the description of this Application.


        :param description: The description of this Application.
        :type description: str
        """

        cls._description = description

    @property
    def uuidv4(cls) -> str:
        """Gets the uuidv4 of this Application.


        :return: The uuidv4 of this Application.
        :rtype: str
        """
        return cls._uuidv4

    @uuidv4.setter
    def uuidv4(cls, uuidv4: str):
        """Sets the uuidv4 of this Application.


        :param uuidv4: The uuidv4 of this Application.
        :type uuidv4: str
        """
        if uuidv4 is None:
            raise ValueError("Invalid value for `uuidv4`, must not be `None`")  # noqa: E501

        cls._uuidv4 = uuidv4

    @property
    def webhookurl(cls) -> str:
        """Gets the webhookurl of this Application.


        :return: The webhookurl of this Application.
        :rtype: str
        """
        return cls._webhookurl

    @webhookurl.setter
    def webhookurl(cls, webhookurl: str):
        """Sets the webhookurl of this Application.


        :param webhookurl: The webhookurl of this Application.
        :type webhookurl: str
        """

        cls._webhookurl = webhookurl

    @property
    def disabled(cls) -> int:
        """Gets the disabled of this Application.


        :return: The disabled of this Application.
        :rtype: int
        """
        return cls._disabled

    @disabled.setter
    def disabled(cls, disabled: int):
        """Sets the disabled of this Application.


        :param disabled: The disabled of this Application.
        :type disabled: int
        """

        cls._disabled = disabled

    @property
    def icon_url(cls) -> str:
        """Gets the icon_url of this Application.


        :return: The icon_url of this Application.
        :rtype: str
        """
        return cls._icon_url

    @icon_url.setter
    def icon_url(cls, icon_url: str):
        """Sets the icon_url of this Application.


        :param icon_url: The icon_url of this Application.
        :type icon_url: str
        """

        cls._icon_url = icon_url

class Quota(XummResource):

    model_types = {
        'ratelimit': str
    }

    attribute_map = {
        'ratelimit': 'ratelimit',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Quota of this Quota.  # noqa: E501
        :rtype: Quota
        """
        cls.sanity_check(kwargs)
        cls._ratelimit = None
        if 'ratelimit' in kwargs:
            cls.ratelimit = kwargs['ratelimit']
    
    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.model_types):
            value = getattr(cls, attr)
            attr = cls.attribute_map[attr]
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

        return {k: v for k, v in result.items() if v is not None}

    @property
    def ratelimit(cls) -> str:
        """Gets the ratelimit of this Quota.


        :return: The ratelimit of this Quota.
        :rtype: str
        """
        return cls._ratelimit

    @ratelimit.setter
    def ratelimit(cls, ratelimit: str):
        """Sets the ratelimit of this Quota.


        :param ratelimit: The ratelimit of this Quota.
        :type ratelimit: str
        """
        if ratelimit is None:
            raise ValueError("Invalid value for `ratelimit`, must not be `None`")  # noqa: E501

        cls._ratelimit = ratelimit


class ApplicationDetails(XummResource):

    required = {
        'quota': True,
        'application': True,
        'call': True
    }

    model_types = {
        'quota': dict,
        'application': dict,
        'call': dict
    }

    attribute_map = {
        'quota': 'quota',
        'application': 'application',
        'call': 'call',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The PongResponse of this PongResponse.  # noqa: E501
        :rtype: PongResponse
        """
        cls.sanity_check(kwargs)
        cls._quota = None
        cls._application = None
        cls._call = None
        cls.quota = Quota(**kwargs['quota'])
        cls.application = Application(**kwargs['application'])
        cls.call = Call(**kwargs['call'])

    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.attribute_map):
            value = getattr(cls, attr)
            attr = cls.attribute_map[attr]
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
        if issubclass(ApplicationDetails, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def quota(cls) -> Quota:
        """Gets the quota of this ApplicationDetails.


        :return: The quota of this ApplicationDetails.
        :rtype: Quota
        """
        return cls._quota

    @quota.setter
    def quota(cls, quota: Quota):
        """Sets the quota of this ApplicationDetails.


        :param quota: The quota of this ApplicationDetails.
        :type quota: Quota
        """
        if quota is None:
            raise ValueError("Invalid value for `quota`, must not be `None`")  # noqa: E501

        cls._quota = quota

    @property
    def application(cls) -> Application:
        """Gets the application of this ApplicationDetails.


        :return: The application of this ApplicationDetails.
        :rtype: Application
        """
        return cls._application

    @application.setter
    def application(cls, application: Application):
        """Sets the application of this ApplicationDetails.


        :param application: The application of this ApplicationDetails.
        :type application: Application
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        cls._application = application

    @property
    def call(cls) -> Call:
        """Gets the call of this ApplicationDetails.


        :return: The call of this ApplicationDetails.
        :rtype: Call
        """
        return cls._call

    @call.setter
    def call(cls, call: Call):
        """Sets the call of this ApplicationDetails.


        :param call: The call of this ApplicationDetails.
        :type call: Call
        """
        if call is None:
            raise ValueError("Invalid value for `call`, must not be `None`")  # noqa: E501

        cls._call = call