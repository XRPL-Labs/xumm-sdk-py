import os
from xumm.resource import XummResource
import six
import json

from typing import List, Dict  # noqa: F401

class TxMeta(XummResource):

    swagger_types = {
        'transaction_index': 'int',
        'transaction_result': 'str',
        'delivered_amount': 'str'
    }

    attribute_map = {
        'transaction_index': 'TransactionIndex',
        'transaction_result': 'TransactionResult',
        'delivered_amount': 'delivered_amount'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The TxMeta of this TxMeta.  # noqa: E501
        :rtype: TxMeta
        """
        cls._transaction_index = kwargs['TransactionIndex']
        cls._transaction_result = kwargs['TransactionResult']
        cls._delivered_amount = kwargs['delivered_amount']
    
    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.swagger_types):
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
        if issubclass(TxMeta, dict):
            for key, value in cls.items():
                result[key] = value

        return result

    @property
    def transaction_index(self) -> int:
        """Gets the transaction_index of this TxMeta.


        :return: The transaction_index of this TxMeta.
        :rtype: int
        """
        return self._transaction_index

    @transaction_index.setter
    def transaction_index(self, transaction_index: int):
        """Sets the transaction_index of this TxMeta.


        :param transaction_index: The transaction_index of this TxMeta.
        :type transaction_index: int
        """
        if transaction_index is None:
            raise ValueError("Invalid value for `transaction_index`, must not be `None`")  # noqa: E501

        self._transaction_index = transaction_index

    @property
    def transaction_result(self) -> str:
        """Gets the transaction_result of this TxMeta.


        :return: The transaction_result of this TxMeta.
        :rtype: str
        """
        return self._transaction_result

    @transaction_result.setter
    def transaction_result(self, transaction_result: str):
        """Sets the transaction_result of this TxMeta.


        :param transaction_result: The transaction_result of this TxMeta.
        :type transaction_result: str
        """
        if transaction_result is None:
            raise ValueError("Invalid value for `transaction_result`, must not be `None`")  # noqa: E501

        self._transaction_result = transaction_result

    @property
    def delivered_amount(self) -> str:
        """Gets the delivered_amount of this TxMeta.


        :return: The delivered_amount of this TxMeta.
        :rtype: str
        """
        return self._delivered_amount

    @delivered_amount.setter
    def delivered_amount(self, delivered_amount: str):
        """Sets the delivered_amount of this TxMeta.


        :param delivered_amount: The delivered_amount of this TxMeta.
        :type delivered_amount: str
        """
        if delivered_amount is None:
            raise ValueError("Invalid value for `delivered_amount`, must not be `None`")  # noqa: E501

        self._delivered_amount = delivered_amount

class Transaction(XummResource):

    swagger_types = {
        'account': 'str',
        'amount': 'str',
        'destination': 'str',
        'fee': 'str',
        'flags': 'int',
        'sequence': 'int',
        'signing_pub_key': 'str',
        'transaction_type': 'str',
        'meta': 'TxMeta',
        'validated': 'bool'
    }

    attribute_map = {
        'account': 'Account',
        'amount': 'Amount',
        'destination': 'Destination',
        'fee': 'Fee',
        'flags': 'Flags',
        'sequence': 'Sequence',
        'signing_pub_key': 'SigningPubKey',
        'transaction_type': 'TransactionType',
        'meta': 'meta',
        'validated': 'validated'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Transaction of this Transaction.  # noqa: E501
        :rtype: Transaction
        """
        cls.account = kwargs['Account']
        cls.amount = kwargs['Amount']
        cls.destination = kwargs['Destination']
        cls.fee = kwargs['Fee']
        cls.flags = kwargs['Flags']
        cls.sequence = kwargs['Sequence']
        cls.signing_pub_key = kwargs['SigningPubKey']
        cls.transaction_type = kwargs['TransactionType']
        cls.meta = TxMeta(**kwargs['meta'])
        cls.validated = kwargs['validated']
    
    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.swagger_types):
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
        if issubclass(Transaction, dict):
            for key, value in cls.items():
                result[key] = value

        return result

    @property
    def account(self) -> str:
        """Gets the account of this Transaction.


        :return: The account of this Transaction.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account: str):
        """Sets the account of this Transaction.


        :param account: The account of this Transaction.
        :type account: str
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def amount(self) -> str:
        """Gets the amount of this Transaction.


        :return: The amount of this Transaction.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount: str):
        """Sets the amount of this Transaction.


        :param amount: The amount of this Transaction.
        :type amount: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def destination(self) -> str:
        """Gets the destination of this Transaction.


        :return: The destination of this Transaction.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination: str):
        """Sets the destination of this Transaction.


        :param destination: The destination of this Transaction.
        :type destination: str
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def fee(self) -> str:
        """Gets the fee of this Transaction.


        :return: The fee of this Transaction.
        :rtype: str
        """
        return self._fee

    @fee.setter
    def fee(self, fee: str):
        """Sets the fee of this Transaction.


        :param fee: The fee of this Transaction.
        :type fee: str
        """
        if fee is None:
            raise ValueError("Invalid value for `fee`, must not be `None`")  # noqa: E501

        self._fee = fee

    @property
    def flags(self) -> int:
        """Gets the flags of this Transaction.


        :return: The flags of this Transaction.
        :rtype: int
        """
        return self._flags

    @flags.setter
    def flags(self, flags: int):
        """Sets the flags of this Transaction.


        :param flags: The flags of this Transaction.
        :type flags: int
        """
        if flags is None:
            raise ValueError("Invalid value for `flags`, must not be `None`")  # noqa: E501

        self._flags = flags

    @property
    def sequence(self) -> int:
        """Gets the sequence of this Transaction.


        :return: The sequence of this Transaction.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence: int):
        """Sets the sequence of this Transaction.


        :param sequence: The sequence of this Transaction.
        :type sequence: int
        """
        if sequence is None:
            raise ValueError("Invalid value for `sequence`, must not be `None`")  # noqa: E501

        self._sequence = sequence

    @property
    def signing_pub_key(self) -> str:
        """Gets the signing_pub_key of this Transaction.


        :return: The signing_pub_key of this Transaction.
        :rtype: str
        """
        return self._signing_pub_key

    @signing_pub_key.setter
    def signing_pub_key(self, signing_pub_key: str):
        """Sets the signing_pub_key of this Transaction.


        :param signing_pub_key: The signing_pub_key of this Transaction.
        :type signing_pub_key: str
        """
        if signing_pub_key is None:
            raise ValueError("Invalid value for `signing_pub_key`, must not be `None`")  # noqa: E501

        self._signing_pub_key = signing_pub_key

    @property
    def transaction_type(self) -> str:
        """Gets the transaction_type of this Transaction.


        :return: The transaction_type of this Transaction.
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type: str):
        """Sets the transaction_type of this Transaction.


        :param transaction_type: The transaction_type of this Transaction.
        :type transaction_type: str
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def meta(self) -> TxMeta:
        """Gets the meta of this Transaction.


        :return: The meta of this Transaction.
        :rtype: TxMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta: TxMeta):
        """Sets the meta of this Transaction.


        :param meta: The meta of this Transaction.
        :type meta: TxMeta
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        self._meta = meta

    @property
    def validated(self) -> bool:
        """Gets the validated of this Transaction.


        :return: The validated of this Transaction.
        :rtype: bool
        """
        return self._validated

    @validated.setter
    def validated(self, validated: bool):
        """Sets the validated of this Transaction.


        :param validated: The validated of this Transaction.
        :type validated: bool
        """
        if validated is None:
            raise ValueError("Invalid value for `validated`, must not be `None`")  # noqa: E501

        self._validated = validated


class BalanceChange(XummResource):

    swagger_types = {
        'counterparty': 'str',
        'currency': 'str',
        'value': 'str'
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
        cls._counterparty = kwargs['counterparty']
        cls._currency = kwargs['currency']
        cls._value = kwargs['value']

    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.swagger_types):
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

        return result

    @property
    def counterparty(self) -> str:
        """Gets the counterparty of this BalanceChange.


        :return: The counterparty of this BalanceChange.
        :rtype: str
        """
        return self._counterparty

    @counterparty.setter
    def counterparty(self, counterparty: str):
        """Sets the counterparty of this BalanceChange.


        :param counterparty: The counterparty of this BalanceChange.
        :type counterparty: str
        """

        self._counterparty = counterparty

    @property
    def currency(self) -> str:
        """Gets the currency of this BalanceChange.


        :return: The currency of this BalanceChange.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        """Sets the currency of this BalanceChange.


        :param currency: The currency of this BalanceChange.
        :type currency: str
        """

        self._currency = currency

    @property
    def value(self) -> str:
        """Gets the value of this BalanceChange.


        :return: The value of this BalanceChange.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this BalanceChange.


        :param value: The value of this BalanceChange.
        :type value: str
        """

        self._value = value

class XRPLTxResponse(XummResource):

    swagger_types = {
        'txid': 'str',
        'balance_changes': 'dict(str, BalanceChange)',
        'node': 'str',
        'transaction': 'Transaction'
    }

    attribute_map = {
        'txid': 'txid',
        'balance_changes': 'balanceChanges',
        'node': 'node',
        'transaction': 'transaction'
    }

    @classmethod
    def get_url(cls, id):
        """get_url."""
        return super(XRPLTxResponse, cls).platform_url() + 'xrpl_tx' + '/' + id
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XRPLTxResponse of this XRPLTxResponse.  # noqa: E501
        :rtype: XRPLTxResponse
        """
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._txid = kwargs['txid']
        cls._balance_changes = {k: [BalanceChange(**b) for b in v] for k, v in kwargs['balanceChanges'].items()}
        cls._node = kwargs['node']
        cls._transaction = Transaction(**kwargs['transaction'])

    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.swagger_types):
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
        if issubclass(XRPLTxResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return result

    @property
    def txid(self) -> str:
        """Gets the txid of this XRPLTxResponse.


        :return: The txid of this XRPLTxResponse.
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid: str):
        """Sets the txid of this XRPLTxResponse.


        :param txid: The txid of this XRPLTxResponse.
        :type txid: str
        """
        if txid is None:
            raise ValueError("Invalid value for `txid`, must not be `None`")  # noqa: E501

        self._txid = txid

    @property
    def balance_changes(self) -> Dict[str, BalanceChange]:
        """Gets the balance_changes of this XRPLTxResponse.


        :return: The balance_changes of this XRPLTxResponse.
        :rtype: Dict[str, BalanceChange]
        """
        return self._balance_changes

    @balance_changes.setter
    def balance_changes(self, balance_changes: Dict[str, BalanceChange]):
        """Sets the balance_changes of this XRPLTxResponse.


        :param balance_changes: The balance_changes of this XRPLTxResponse.
        :type balance_changes: Dict[str, BalanceChange]
        """
        if balance_changes is None:
            raise ValueError("Invalid value for `balance_changes`, must not be `None`")  # noqa: E501

        self._balance_changes = balance_changes

    @property
    def node(self) -> str:
        """Gets the node of this XRPLTxResponse.


        :return: The node of this XRPLTxResponse.
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node: str):
        """Sets the node of this XRPLTxResponse.


        :param node: The node of this XRPLTxResponse.
        :type node: str
        """
        if node is None:
            raise ValueError("Invalid value for `node`, must not be `None`")  # noqa: E501

        self._node = node

    @property
    def transaction(self) -> Transaction:
        """Gets the transaction of this XRPLTxResponse.


        :return: The transaction of this XRPLTxResponse.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction: Transaction):
        """Sets the transaction of this XRPLTxResponse.


        :param transaction: The transaction of this XRPLTxResponse.
        :type transaction: Transaction
        """
        if transaction is None:
            raise ValueError("Invalid value for `transaction`, must not be `None`")  # noqa: E501

        self._transaction = transaction