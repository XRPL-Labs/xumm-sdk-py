#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource
import six
from typing import Union, List, Dict, Callable, Any  # noqa: F401


class RateCurrency(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        # 'en': True,
        'code': True,
        'symbol': True,
        'iso_decimals': True,
    }

    model_types = {
        'en': str,
        'code': str,
        'symbol': str,
        'iso_decimals': int,
    }

    attribute_map = {
        'en': 'en',
        'code': 'code',
        'symbol': 'symbol',
        'iso_decimals': 'isoDecimals',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RateCurrency of this RateCurrency.  # noqa: E501
        :rtype: RateCurrency
        """
        cls.sanity_check(kwargs)
        cls._en = None
        cls._code = None
        cls._symbol = None
        cls._iso_decimals = None
        if 'en' in kwargs:
            cls.en = kwargs['en']
        cls.code = kwargs['code']
        cls.symbol = kwargs['symbol']
        cls.iso_decimals = kwargs['isoDecimals']

    @property
    def en(cls) -> str:
        """Gets the en of this RateCurrency.


        :return: The en of this RateCurrency.
        :rtype: str
        """
        return cls._en

    @en.setter
    def en(cls, en: str):
        """Sets the en of this RateCurrency.


        :param en: The en of this RateCurrency.
        :type en: str
        """
        if en is None:
            raise ValueError("Invalid value for `en`, must not be `None`")  # noqa: E501

        cls._en = en

    @property
    def code(cls) -> str:
        """Gets the code of this RateCurrency.


        :return: The code of this RateCurrency.
        :rtype: str
        """
        return cls._code

    @code.setter
    def code(cls, code: str):
        """Sets the code of this RateCurrency.


        :param code: The code of this RateCurrency.
        :type code: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        cls._code = code

    @property
    def symbol(cls) -> str:
        """Gets the symbol of this RateCurrency.


        :return: The symbol of this RateCurrency.
        :rtype: str
        """
        return cls._symbol

    @symbol.setter
    def symbol(cls, symbol: str):
        """Sets the symbol of this RateCurrency.


        :param symbol: The symbol of this RateCurrency.
        :type symbol: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        cls._symbol = symbol

    @property
    def iso_decimals(cls) -> int:
        """Gets the iso_decimals of this RateCurrency.


        :return: The iso_decimals of this RateCurrency.
        :rtype: int
        """
        return cls._iso_decimals

    @iso_decimals.setter
    def iso_decimals(cls, iso_decimals: int):
        """Sets the iso_decimals of this RateCurrency.


        :param iso_decimals: The iso_decimals of this RateCurrency.
        :type iso_decimals: int
        """
        if iso_decimals is None:
            raise ValueError("Invalid value for `iso_decimals`, must not be `None`")  # noqa: E501

        cls._iso_decimals = iso_decimals


class CurrencyRef(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'currency': True,
    }

    model_types = {
        'currency': dict,
    }

    attribute_map = {
        'currency': 'currency',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CurrencyRef of this CurrencyRef.  # noqa: E501
        :rtype: CurrencyRef
        """
        cls.sanity_check(kwargs)
        cls._currency = None
        cls.currency = RateCurrency(**kwargs['currency'])

    def to_dict(cls) -> Dict[str, object]:
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
        if issubclass(CurrencyRef, dict):
            for key, value in cls.items():
                result[key] = value

        return {
            k: v for k, v in result.items()
            if v is not None or k in
            cls.required and k in cls.nullable
        }

    @property
    def currency(cls) -> RateCurrency:
        """Gets the currency of this CurrencyRef.


        :return: The currency of this CurrencyRef.
        :rtype: RateCurrency
        """
        return cls._currency

    @currency.setter
    def currency(cls, currency: RateCurrency):
        """Sets the currency of this CurrencyRef.


        :param currency: The currency of this CurrencyRef.
        :type currency: RateCurrency
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        cls._currency = currency


class RatesResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'USD': True,
        'XRP': True,
        'meta': True,
    }

    model_types = {
        'USD': int,
        'XRP': float,
        'meta': dict
    }

    attribute_map = {
        'USD': 'USD',
        'XRP': 'XRP',
        'meta': '__meta',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RatesResponse of this RatesResponse.  # noqa: E501
        :rtype: RatesResponse
        """
        # cls.sanity_check(kwargs)
        cls._USD = None
        cls._XRP = None
        cls._meta = None
        cls.USD = kwargs['USD']
        cls.XRP = kwargs['XRP']
        cls.meta = CurrencyRef(**kwargs['__meta'])

    def to_dict(cls) -> Dict[str, object]:
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
        if issubclass(RatesResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return {
            k: v for k, v in result.items()
            if v is not None or k in
            cls.required and k in cls.nullable
        }

    @property
    def USD(cls) -> int:
        """Gets the USD of this RatesResponse.


        :return: The USD of this RatesResponse.
        :rtype: int
        """
        return cls._USD

    @USD.setter
    def USD(cls, USD: int):
        """Sets the USD of this RatesResponse.


        :param USD: The USD of this RatesResponse.
        :type USD: int
        """
        if USD is None:
            raise ValueError("Invalid value for `USD`, must not be `None`")  # noqa: E501

        cls._USD = USD

    @property
    def XRP(cls) -> float:
        """Gets the XRP of this RatesResponse.


        :return: The XRP of this RatesResponse.
        :rtype: float
        """
        return cls._XRP

    @XRP.setter
    def XRP(cls, XRP: float):
        """Sets the XRP of this RatesResponse.


        :param XRP: The XRP of this RatesResponse.
        :type XRP: float
        """
        if XRP is None:
            raise ValueError("Invalid value for `XRP`, must not be `None`")  # noqa: E501

        cls._XRP = XRP

    @property
    def meta(cls) -> CurrencyRef:
        """Gets the meta of this RatesResponse.


        :return: The meta of this RatesResponse.
        :rtype: CurrencyRef
        """
        return cls._meta

    @meta.setter
    def meta(cls, meta: CurrencyRef):
        """Sets the XRP of this RatesResponse.


        :param meta: The meta of this RatesResponse.
        :type meta: CurrencyRef
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        cls._meta = meta
