#!/usr/bin/env python
# coding: utf-8

from urllib import request
from xumm.resource import XummResource
import six
from typing import Union, List, Dict, Callable, Any  # noqa: F401


class Currency(XummResource):

    required = {
        'id': True,
        'issuer_id': True,
        'issuer': True,
        'currency': True,
        'name': True,
        'avatar': True,
        'shortlist': True
    }

    model_types = {
        'id': int,
        'issuer_id': int,
        'issuer': str,
        'currency': str,
        'name': str,
        'avatar': str,
        'shortlist': int
    }

    attribute_map = {
        'id': 'id',
        'issuer_id': 'issuer_id',
        'issuer': 'issuer',
        'currency': 'currency',
        'name': 'name',
        'avatar': 'avatar',
        'shortlist': 'shortlist'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Currency of this Currency.  # noqa: E501
        :rtype: Currency
        """
        cls.sanity_check(kwargs)
        cls._id = None
        cls._issuer_id = None
        cls._issuer = None
        cls._currency = None
        cls._name = None
        cls._avatar = None
        cls._shortlist = None
        cls.id = kwargs['id']
        cls.issuer_id = kwargs['issuer_id']
        cls.issuer = kwargs['issuer']
        cls.currency = kwargs['currency']
        cls.name = kwargs['name']
        cls.avatar = kwargs['avatar']
        cls.shortlist = kwargs['shortlist']
    
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
        if issubclass(Currency, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def id(cls) -> int:
        """Gets the id of this Currency.


        :return: The id of this Currency.
        :rtype: int
        """
        return cls._id

    @id.setter
    def id(cls, id: int):
        """Sets the id of this Currency.


        :param id: The id of this Currency.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        cls._id = id

    @property
    def issuer_id(cls) -> int:
        """Gets the issuer_id of this Currency.


        :return: The issuer_id of this Currency.
        :rtype: int
        """
        return cls._issuer_id

    @issuer_id.setter
    def issuer_id(cls, issuer_id: int):
        """Sets the issuer_id of this Currency.


        :param issuer_id: The issuer_id of this Currency.
        :type issuer_id: int
        """
        if issuer_id is None:
            raise ValueError("Invalid value for `issuer_id`, must not be `None`")  # noqa: E501

        cls._issuer_id = issuer_id

    @property
    def issuer(cls) -> str:
        """Gets the issuer of this Currency.


        :return: The issuer of this Currency.
        :rtype: str
        """
        return cls._issuer

    @issuer.setter
    def issuer(cls, issuer: str):
        """Sets the issuer of this Currency.


        :param issuer: The issuer of this Currency.
        :type issuer: str
        """
        if issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")  # noqa: E501

        cls._issuer = issuer

    @property
    def currency(cls) -> str:
        """Gets the currency of this Currency.


        :return: The currency of this Currency.
        :rtype: str
        """
        return cls._currency

    @currency.setter
    def currency(cls, currency: str):
        """Sets the currency of this Currency.


        :param currency: The currency of this Currency.
        :type currency: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        cls._currency = currency

    @property
    def name(cls) -> str:
        """Gets the name of this Currency.


        :return: The name of this Currency.
        :rtype: str
        """
        return cls._name

    @name.setter
    def name(cls, name: str):
        """Sets the name of this Currency.


        :param name: The name of this Currency.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        cls._name = name

    @property
    def avatar(cls) -> str:
        """Gets the avatar of this Currency.


        :return: The avatar of this Currency.
        :rtype: str
        """
        return cls._avatar

    @avatar.setter
    def avatar(cls, avatar: str):
        """Sets the avatar of this Currency.


        :param avatar: The avatar of this Currency.
        :type avatar: str
        """

        cls._avatar = avatar

    @property
    def shortlist(cls) -> int:
        """Gets the shortlist of this Currency.


        :return: The shortlist of this Currency.
        :rtype: int
        """
        return cls._shortlist

    @shortlist.setter
    def shortlist(cls, shortlist: int):
        """Sets the shortlist of this Currency.


        :param shortlist: The shortlist of this Currency.
        :type shortlist: int
        """

        cls._shortlist = shortlist


class Asset(XummResource):

    required = {
        'id': True,
        'name': True,
        'domain': True,
        'avatar': True,
        'shortlist': True,
        'currencies': True
    }

    model_types = {
        'id': int,
        'name': str,
        'domain': str,
        'avatar': str,
        'shortlist': int,
        'currencies': dict
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'domain': 'domain',
        'avatar': 'avatar',
        'shortlist': 'shortlist',
        'currencies': 'currencies'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Asset of this Asset.  # noqa: E501
        :rtype: Asset
        """
        cls.sanity_check(kwargs)
        cls._id = None
        cls._name = None
        cls._domain = None
        cls._avatar = None
        cls._shortlist = None
        cls._currencies = None
        cls.id = kwargs['id']
        cls.name = kwargs['name']
        cls.domain = kwargs['domain']
        cls.avatar = kwargs['avatar']
        cls.shortlist = kwargs['shortlist']
        cls.currencies = {k: Currency(**v) for k, v in kwargs['currencies'].items()}

    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.attribute_map):
            value = getattr(cls, attr)
            print(attr)
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
        if issubclass(Asset, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def id(cls) -> int:
        """Gets the id of this Asset.


        :return: The id of this Asset.
        :rtype: int
        """
        return cls._id

    @id.setter
    def id(cls, id: int):
        """Sets the id of this Asset.


        :param id: The id of this Asset.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        cls._id = id

    @property
    def name(cls) -> str:
        """Gets the name of this Asset.


        :return: The name of this Asset.
        :rtype: str
        """
        return cls._name

    @name.setter
    def name(cls, name: str):
        """Sets the name of this Asset.


        :param name: The name of this Asset.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        cls._name = name

    @property
    def domain(cls) -> str:
        """Gets the domain of this Asset.


        :return: The domain of this Asset.
        :rtype: str
        """
        return cls._domain

    @domain.setter
    def domain(cls, domain: str):
        """Sets the domain of this Asset.


        :param domain: The domain of this Asset.
        :type domain: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        cls._domain = domain

    @property
    def avatar(cls) -> str:
        """Gets the avatar of this Asset.


        :return: The avatar of this Asset.
        :rtype: str
        """
        return cls._avatar

    @avatar.setter
    def avatar(cls, avatar: str):
        """Sets the avatar of this Asset.


        :param avatar: The avatar of this Asset.
        :type avatar: str
        """
        if avatar is None:
            raise ValueError("Invalid value for `avatar`, must not be `None`")  # noqa: E501

        cls._avatar = avatar

    @property
    def shortlist(cls) -> int:
        """Gets the shortlist of this Asset.


        :return: The shortlist of this Asset.
        :rtype: int
        """
        return cls._shortlist

    @shortlist.setter
    def shortlist(cls, shortlist: int):
        """Sets the shortlist of this Asset.


        :param shortlist: The shortlist of this Asset.
        :type shortlist: int
        """
        if shortlist is None:
            raise ValueError("Invalid value for `shortlist`, must not be `None`")  # noqa: E501

        cls._shortlist = shortlist

    @property
    def currencies(cls) -> Dict[str, Currency]:
        """Gets the currencies of this Asset.


        :return: The currencies of this Asset.
        :rtype: Dict[str, Currency]
        """
        return cls._currencies

    @currencies.setter
    def currencies(cls, currencies: Dict[str, Currency]):
        """Sets the currencies of this Asset.


        :param currencies: The currencies of this Asset.
        :type currencies: Dict[str, Currency]
        """
        if currencies is None:
            raise ValueError("Invalid value for `currencies`, must not be `None`")  # noqa: E501

        cls._currencies = currencies


class CuratedAssetsResponse(XummResource):

    model_types = {
        'issuers': 'list[str]',
        'currencies': 'list[str]',
        'details': 'dict(str, Asset)'
    }
    attribute_list = {
        'issuers': 'issuers',
        'currencies': 'currencies',
        'details': 'details'
    }
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The CuratedAssetsResponse of this CuratedAssetsResponse.  # noqa: E501
        :rtype: CuratedAssetsResponse
        """
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._issuers = None
        cls._currencies = None
        cls._details = None
        cls.issuers = kwargs['issuers']
        cls.currencies = kwargs['currencies']
        cls.details = {k: Asset(**v) for k, v in kwargs['details'].items()}

    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.model_types):
            value = getattr(cls, attr)
            attr = cls.attribute_list[attr]
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
        if issubclass(CuratedAssetsResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def issuers(cls) -> List[str]:
        """Gets the issuers of this CuratedAssetsResponse.


        :return: The issuers of this CuratedAssetsResponse.
        :rtype: List[str]
        """
        return cls._issuers

    @issuers.setter
    def issuers(cls, issuers: List[str]):
        """Sets the issuers of this CuratedAssetsResponse.


        :param issuers: The issuers of this CuratedAssetsResponse.
        :type issuers: List[str]
        """
        if issuers is None:
            raise ValueError("Invalid value for `issuers`, must not be `None`")  # noqa: E501

        cls._issuers = issuers

    @property
    def currencies(cls) -> List[str]:
        """Gets the currencies of this CuratedAssetsResponse.


        :return: The currencies of this CuratedAssetsResponse.
        :rtype: List[str]
        """
        return cls._currencies

    @currencies.setter
    def currencies(cls, currencies: List[str]):
        """Sets the currencies of this CuratedAssetsResponse.


        :param currencies: The currencies of this CuratedAssetsResponse.
        :type currencies: List[str]
        """
        if currencies is None:
            raise ValueError("Invalid value for `currencies`, must not be `None`")  # noqa: E501

        cls._currencies = currencies

    @property
    def details(cls) -> Dict[str, Asset]:
        """Gets the details of this CuratedAssetsResponse.


        :return: The details of this CuratedAssetsResponse.
        :rtype: Dict[str, Asset]
        """
        return cls._details

    @details.setter
    def details(cls, details: Dict[str, Asset]):
        """Sets the details of this CuratedAssetsResponse.


        :param details: The details of this CuratedAssetsResponse.
        :type details: Dict[str, Asset]
        """
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        cls._details = details