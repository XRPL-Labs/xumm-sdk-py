import os
from xumm import client
from xumm.resource import XummResource
from xumm.util import (
    cached_property,
)
import json
import time
import six

from typing import List, Dict  # noqa: F401

class Currency(XummResource):

    swagger_types = {
        'id': 'int',
        'issuer_id': 'int',
        'issuer': 'str',
        'currency': 'str',
        'name': 'str',
        'avatar': 'str',
        'shortlist': 'int'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Currency of this Currency.  # noqa: E501
        :rtype: Currency
        """
        cls._id = kwargs['id']
        cls._issuer_id = kwargs['issuer_id']
        cls._issuer = kwargs['issuer']
        cls._currency = kwargs['currency']
        cls._name = kwargs['name']
        cls._avatar = kwargs['avatar']
        cls._shortlist = kwargs['shortlist']
    
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
        if issubclass(Currency, dict):
            for key, value in cls.items():
                result[key] = value

        return result

    @property
    def id(self) -> int:
        """Gets the id of this Currency.


        :return: The id of this Currency.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Currency.


        :param id: The id of this Currency.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def issuer_id(self) -> int:
        """Gets the issuer_id of this Currency.


        :return: The issuer_id of this Currency.
        :rtype: int
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id: int):
        """Sets the issuer_id of this Currency.


        :param issuer_id: The issuer_id of this Currency.
        :type issuer_id: int
        """
        if issuer_id is None:
            raise ValueError("Invalid value for `issuer_id`, must not be `None`")  # noqa: E501

        self._issuer_id = issuer_id

    @property
    def issuer(self) -> str:
        """Gets the issuer of this Currency.


        :return: The issuer of this Currency.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer: str):
        """Sets the issuer of this Currency.


        :param issuer: The issuer of this Currency.
        :type issuer: str
        """
        if issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")  # noqa: E501

        self._issuer = issuer

    @property
    def currency(self) -> str:
        """Gets the currency of this Currency.


        :return: The currency of this Currency.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        """Sets the currency of this Currency.


        :param currency: The currency of this Currency.
        :type currency: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def name(self) -> str:
        """Gets the name of this Currency.


        :return: The name of this Currency.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Currency.


        :param name: The name of this Currency.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def avatar(self) -> str:
        """Gets the avatar of this Currency.


        :return: The avatar of this Currency.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar: str):
        """Sets the avatar of this Currency.


        :param avatar: The avatar of this Currency.
        :type avatar: str
        """

        self._avatar = avatar

    @property
    def shortlist(self) -> int:
        """Gets the shortlist of this Currency.


        :return: The shortlist of this Currency.
        :rtype: int
        """
        return self._shortlist

    @shortlist.setter
    def shortlist(self, shortlist: int):
        """Sets the shortlist of this Currency.


        :param shortlist: The shortlist of this Currency.
        :type shortlist: int
        """

        self._shortlist = shortlist


class Asset(XummResource):

    swagger_types = {
        'id': 'int',
        'name': 'str',
        'domain': 'str',
        'avatar': 'str',
        'shortlist': 'int',
        'currencies': 'dict(str, Currency)'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Asset of this Asset.  # noqa: E501
        :rtype: Asset
        """
        cls._id = kwargs['id']
        cls._name = kwargs['name']
        cls._domain = kwargs['domain']
        cls._avatar = kwargs['avatar']
        cls._shortlist = kwargs['shortlist']
        cls._currencies = {k: Currency(**v) for k, v in kwargs['currencies'].items()}

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
        if issubclass(Asset, dict):
            for key, value in cls.items():
                result[key] = value

        return result

    @property
    def id(self) -> int:
        """Gets the id of this Asset.


        :return: The id of this Asset.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Asset.


        :param id: The id of this Asset.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Asset.


        :return: The name of this Asset.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Asset.


        :param name: The name of this Asset.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def domain(self) -> str:
        """Gets the domain of this Asset.


        :return: The domain of this Asset.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain: str):
        """Sets the domain of this Asset.


        :param domain: The domain of this Asset.
        :type domain: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def avatar(self) -> str:
        """Gets the avatar of this Asset.


        :return: The avatar of this Asset.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar: str):
        """Sets the avatar of this Asset.


        :param avatar: The avatar of this Asset.
        :type avatar: str
        """
        if avatar is None:
            raise ValueError("Invalid value for `avatar`, must not be `None`")  # noqa: E501

        self._avatar = avatar

    @property
    def shortlist(self) -> int:
        """Gets the shortlist of this Asset.


        :return: The shortlist of this Asset.
        :rtype: int
        """
        return self._shortlist

    @shortlist.setter
    def shortlist(self, shortlist: int):
        """Sets the shortlist of this Asset.


        :param shortlist: The shortlist of this Asset.
        :type shortlist: int
        """
        if shortlist is None:
            raise ValueError("Invalid value for `shortlist`, must not be `None`")  # noqa: E501

        self._shortlist = shortlist

    @property
    def currencies(self) -> Dict[str, Currency]:
        """Gets the currencies of this Asset.


        :return: The currencies of this Asset.
        :rtype: Dict[str, Currency]
        """
        return self._currencies

    @currencies.setter
    def currencies(self, currencies: Dict[str, Currency]):
        """Sets the currencies of this Asset.


        :param currencies: The currencies of this Asset.
        :type currencies: Dict[str, Currency]
        """
        if currencies is None:
            raise ValueError("Invalid value for `currencies`, must not be `None`")  # noqa: E501

        self._currencies = currencies


class CuratedAssetsResponse(XummResource):

    swagger_types = {
        'issuers': 'list[str]',
        'currencies': 'list[str]',
        'details': 'dict(str, Asset)'
    }

    @classmethod
    def get_url(cls):
        """get_url."""
        return super(CuratedAssetsResponse, cls).platform_url() + 'curated_assets' + '/'
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The CuratedAssetsResponse of this CuratedAssetsResponse.  # noqa: E501
        :rtype: CuratedAssetsResponse
        """
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._issuers = kwargs['issuers']
        cls._currencies = kwargs['currencies']
        cls._details = {k: Asset(**v) for k, v in kwargs['details'].items()}

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
        if issubclass(CuratedAssetsResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return result

    @property
    def issuers(self) -> List[str]:
        """Gets the issuers of this CuratedAssetsResponse.


        :return: The issuers of this CuratedAssetsResponse.
        :rtype: List[str]
        """
        return self._issuers

    @issuers.setter
    def issuers(self, issuers: List[str]):
        """Sets the issuers of this CuratedAssetsResponse.


        :param issuers: The issuers of this CuratedAssetsResponse.
        :type issuers: List[str]
        """
        if issuers is None:
            raise ValueError("Invalid value for `issuers`, must not be `None`")  # noqa: E501

        self._issuers = issuers

    @property
    def currencies(self) -> List[str]:
        """Gets the currencies of this CuratedAssetsResponse.


        :return: The currencies of this CuratedAssetsResponse.
        :rtype: List[str]
        """
        return self._currencies

    @currencies.setter
    def currencies(self, currencies: List[str]):
        """Sets the currencies of this CuratedAssetsResponse.


        :param currencies: The currencies of this CuratedAssetsResponse.
        :type currencies: List[str]
        """
        if currencies is None:
            raise ValueError("Invalid value for `currencies`, must not be `None`")  # noqa: E501

        self._currencies = currencies

    @property
    def details(self) -> Dict[str, Asset]:
        """Gets the details of this CuratedAssetsResponse.


        :return: The details of this CuratedAssetsResponse.
        :rtype: Dict[str, Asset]
        """
        return self._details

    @details.setter
    def details(self, details: Dict[str, Asset]):
        """Sets the details of this CuratedAssetsResponse.


        :param details: The details of this CuratedAssetsResponse.
        :type details: Dict[str, Asset]
        """
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        self._details = details