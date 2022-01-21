#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource
import six
from typing import Union, List, Dict, Callable, Any  # noqa: F401


class BalanceChange(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'counterparty': True,
        'currency': True,
        'value': True,
    }

    model_types = {
        'counterparty': str,
        'currency': str,
        'value': str
    }

    attribute_map = {
        'counterparty': 'counterparty',
        'currency': 'currency',
        'value': 'value'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The BalanceChange of this BalanceChange.  # noqa: E501
        :rtype: BalanceChange
        """
        cls.sanity_check(kwargs)
        cls._counterparty = None
        cls._currency = None
        cls._value = None
        cls.counterparty = kwargs['counterparty']
        cls.currency = kwargs['currency']
        cls.value = kwargs['value']

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
        if issubclass(BalanceChange, dict):
            for key, value in cls.items():
                key = cls.attribute_map[key]
                result[key] = value

        return {
            k: v for k, v in result.items()
            if v is not None or k in
            cls.required and k in cls.nullable
        }

    @property
    def counterparty(cls) -> str:
        """Gets the counterparty of this BalanceChange.


        :return: The counterparty of this BalanceChange.
        :rtype: str
        """
        return cls._counterparty

    @counterparty.setter
    def counterparty(cls, counterparty: str):
        """Sets the counterparty of this BalanceChange.


        :param counterparty: The counterparty of this BalanceChange.
        :type counterparty: str
        """

        cls._counterparty = counterparty

    @property
    def currency(cls) -> str:
        """Gets the currency of this BalanceChange.


        :return: The currency of this BalanceChange.
        :rtype: str
        """
        return cls._currency

    @currency.setter
    def currency(cls, currency: str):
        """Sets the currency of this BalanceChange.


        :param currency: The currency of this BalanceChange.
        :type currency: str
        """

        cls._currency = currency

    @property
    def value(cls) -> str:
        """Gets the value of this BalanceChange.


        :return: The value of this BalanceChange.
        :rtype: str
        """
        return cls._value

    @value.setter
    def value(cls, value: str):
        """Sets the value of this BalanceChange.


        :param value: The value of this BalanceChange.
        :type value: str
        """

        cls._value = value


class XrplTransaction(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'txid': True,
        'node': True,
        'transaction': True,
    }

    model_types = {
        'txid': str,
        'balance_changes': dict,
        'node': str,
        'transaction': dict
    }

    attribute_map = {
        'txid': 'txid',
        'balance_changes': 'balanceChanges',
        'node': 'node',
        'transaction': 'transaction'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XrplTransaction of this XrplTransaction.  # noqa: E501
        :rtype: XrplTransaction
        """
        cls.sanity_check(kwargs)
        cls._txid = None
        cls._balance_changes = None
        cls._node = None
        cls._transaction = None
        cls.txid = kwargs['txid']
        cls.balance_changes = {k: [BalanceChange(**b).to_dict() for b in v] for k, v in kwargs['balanceChanges'].items()}  # noqa: E501
        cls.node = kwargs['node']
        cls.transaction = kwargs['transaction']

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
        if issubclass(XrplTransaction, dict):
            for key, value in cls.items():
                result[key] = value

        return {
            k: v for k, v in result.items()
            if v is not None or k in
            cls.required and k in cls.nullable
        }

    @property
    def txid(cls) -> str:
        """Gets the txid of this XrplTransaction.


        :return: The txid of this XrplTransaction.
        :rtype: str
        """
        return cls._txid

    @txid.setter
    def txid(cls, txid: str):
        """Sets the txid of this XrplTransaction.


        :param txid: The txid of this XrplTransaction.
        :type txid: str
        """
        if txid is None:
            raise ValueError("Invalid value for `txid`, must not be `None`")  # noqa: E501

        cls._txid = txid

    @property
    def balance_changes(cls) -> Dict[str, BalanceChange]:
        """Gets the balance_changes of this XrplTransaction.


        :return: The balance_changes of this XrplTransaction.
        :rtype: Dict[str, BalanceChange]
        """
        return cls._balance_changes

    @balance_changes.setter
    def balance_changes(cls, balance_changes: Dict[str, BalanceChange]):
        """Sets the balance_changes of this XrplTransaction.


        :param balance_changes: The balance_changes of this XrplTransaction.
        :type balance_changes: Dict[str, BalanceChange]
        """
        if balance_changes is None:
            raise ValueError("Invalid value for `balance_changes`, must not be `None`")  # noqa: E501

        cls._balance_changes = balance_changes

    @property
    def node(cls) -> str:
        """Gets the node of this XrplTransaction.


        :return: The node of this XrplTransaction.
        :rtype: str
        """
        return cls._node

    @node.setter
    def node(cls, node: str):
        """Sets the node of this XrplTransaction.


        :param node: The node of this XrplTransaction.
        :type node: str
        """
        if node is None:
            raise ValueError("Invalid value for `node`, must not be `None`")  # noqa: E501

        cls._node = node

    @property
    def transaction(cls) -> Dict[str, Any]:
        """Gets the transaction of this XrplTransaction.


        :return: The transaction of this XrplTransaction.
        :rtype: Dict[str, Any]
        """
        return cls._transaction

    @transaction.setter
    def transaction(cls, transaction: Dict[str, Any]):
        """Sets the transaction of this XrplTransaction.


        :param transaction: The transaction of this XrplTransaction.
        :type transaction: Dict[str, Any]
        """
        if transaction is None:
            raise ValueError("Invalid value for `transaction`, must not be `None`")  # noqa: E501

        cls._transaction = transaction
