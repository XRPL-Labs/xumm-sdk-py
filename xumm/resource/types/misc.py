#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource
import six
from typing import Union, List, Dict, Callable, Any  # noqa: F401


class ReturnUrl(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'app': True,
        'web': True
    }

    model_types = {
        'app': str,
        'web': str
    }

    attribute_map = {
        'app': 'app',
        'web': 'web'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The ReturnUrl of this ReturnUrl.  # noqa: E501
        :rtype: ReturnUrl
        """
        cls.sanity_check(kwargs)
        cls._app = None
        cls._web = None
        if 'app' in kwargs:
            cls.app = kwargs['app']
        if 'web' in kwargs:
            cls.web = kwargs['web']

    def to_dict(cls) -> Dict[str, object]:
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
        if issubclass(Options, dict):
            for key, value in cls.items():
                result[key] = value

        return {
            k: v for k, v in result.items()
            if v is not None or k in
            cls.required and k in cls.nullable
        }

    @property
    def app(self) -> str:
        """Gets the app of this ReturnUrl.


        :return: The app of this ReturnUrl.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app: str):
        """Sets the app of this ReturnUrl.


        :param app: The app of this ReturnUrl.
        :type app: str
        """

        self._app = app

    @property
    def web(self) -> str:
        """Gets the web of this ReturnUrl.


        :return: The web of this ReturnUrl.
        :rtype: str
        """
        return self._web

    @web.setter
    def web(self, web: str):
        """Sets the web of this ReturnUrl.


        :param web: The web of this ReturnUrl.
        :type web: str
        """

        self._web = web


class Options(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'submit': True,
        'expire': True,
        'return_url': True
    }

    model_types = {
        'submit': bool,
        'expire': int,
        'return_url': dict
    }

    attribute_map = {
        'submit': 'submit',
        'expire': 'expire',
        'return_url': 'return_url'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Options of this Options.  # noqa: E501
        :rtype: Options
        """
        cls._submit = None
        cls._expire = None
        cls._return_url = None
        cls.submit = kwargs['submit']
        cls.expire = kwargs['expire']
        cls.return_url = kwargs['return_url']

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
        if issubclass(Options, dict):
            for key, value in cls.items():
                result[key] = value

        return {
            k: v for k, v in result.items()
            if v is not None or k in
            cls.required and k in cls.nullable
        }

    @property
    def submit(self) -> bool:
        """Gets the submit of this Options.


        :return: The submit of this Options.
        :rtype: bool
        """
        return self._submit

    @submit.setter
    def submit(self, submit: bool):
        """Sets the submit of this Options.


        :param submit: The submit of this Options.
        :type submit: bool
        """
        if submit is None:
            raise ValueError("Invalid value for `submit`, must not be `None`")  # noqa: E501

        self._submit = submit

    @property
    def expire(self) -> int:
        """Gets the expire of this Options.


        :return: The expire of this Options.
        :rtype: int
        """
        return self._expire

    @expire.setter
    def expire(self, expire: int):
        """Sets the expire of this Options.


        :param expire: The expire of this Options.
        :type expire: int
        """
        if expire is None:
            raise ValueError("Invalid value for `expire`, must not be `None`")  # noqa: E501

        self._expire = expire

    @property
    def return_url(self) -> ReturnUrl:
        """Gets the return_url of this Options.


        :return: The return_url of this Options.
        :rtype: ReturnUrl
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url: ReturnUrl):
        """Sets the return_url of this Options.


        :param return_url: The return_url of this Options.
        :type return_url: ReturnUrl
        """
        if return_url is None:
            raise ValueError("Invalid value for `return_url`, must not be `None`")  # noqa: E501

        self._return_url = return_url


class Response(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    nullable = {
        'hex': True,
        'txid': True,
        'resolved_at': True,
        'dispatched_to': True,
        'dispatched_result': True,
        'dispatched_nodetype': True,
        'multisign_account': True,
        'account': True,
    }

    required = {
        'hex': True,
        'txid': True,
        'resolved_at': True,
        'dispatched_to': True,
        'dispatched_result': True,
        'dispatched_nodetype': True,
        'multisign_account': True,
        'account': True,
        # 'approved_with': True,
    }

    model_types = {
        'hex': str,
        'txid': str,
        'resolved_at': str,
        'dispatched_to': str,
        'dispatched_result': str,
        'dispatched_nodetype': str,
        'multisign_account': str,
        'account': str,
        'approved_with': str,
    }

    attribute_map = {
        'hex': 'hex',
        'txid': 'txid',
        'resolved_at': 'resolved_at',
        'dispatched_to': 'dispatched_to',
        'dispatched_result': 'dispatched_result',
        'dispatched_nodetype': 'dispatched_nodetype',
        'multisign_account': 'multisign_account',
        'account': 'account',
        'approved_with': 'approved_with',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Response of this Response.  # noqa: E501
        :rtype: Response
        """
        cls.sanity_check(kwargs)
        cls._hex = None
        cls._txid = None
        cls._resolved_at = None
        cls._dispatched_to = None
        cls._dispatched_result = None
        cls._dispatched_nodetype = None
        cls._multisign_account = None
        cls._account = None
        cls._approved_with = None
        if 'hex' in kwargs:
            cls.hex = kwargs['hex']
        if 'txid' in kwargs:
            cls.txid = kwargs['txid']
        if 'resolved_at' in kwargs:
            cls.resolved_at = kwargs['resolved_at']
        if 'dispatched_to' in kwargs:
            cls.dispatched_to = kwargs['dispatched_to']
        if 'dispatched_result' in kwargs:
            cls.dispatched_result = kwargs['dispatched_result']
        if 'dispatched_nodetype' in kwargs:
            cls.dispatched_nodetype = kwargs['dispatched_nodetype']
        if 'multisign_account' in kwargs:
            cls.multisign_account = kwargs['multisign_account']
        if 'account' in kwargs:
            cls.account = kwargs['account']
        if 'approved_with' in kwargs:
            cls.approved_with = kwargs['approved_with']
        return cls

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
        if issubclass(Response, dict):
            for key, value in cls.items():
                result[key] = value

        return {
            k: v for k, v in result.items()
            if v is not None or k in
            cls.required and k in cls.nullable
        }

    @property
    def hex(cls) -> str:
        """Gets the hex of this Response.


        :return: The hex of this Response.
        :rtype: str
        """
        return cls._hex

    @hex.setter
    def hex(cls, hex: str):
        """Sets the hex of this Response.


        :param hex: The hex of this Response.
        :type hex: str
        """
        # if hex is None:
        #     raise ValueError("Invalid value for `hex`, must not be `None`")  # noqa: E501

        cls._hex = hex

    @property
    def txid(cls) -> str:
        """Gets the txid of this Response.


        :return: The txid of this Response.
        :rtype: str
        """
        return cls._txid

    @txid.setter
    def txid(cls, txid: str):
        """Sets the txid of this Response.


        :param txid: The txid of this Response.
        :type txid: str
        """
        # if txid is None:
        #     raise ValueError("Invalid value for `txid`, must not be `None`")  # noqa: E501

        cls._txid = txid

    @property
    def resolved_at(cls) -> str:
        """Gets the resolved_at of this Response.


        :return: The resolved_at of this Response.
        :rtype: str
        """
        return cls._resolved_at

    @resolved_at.setter
    def resolved_at(cls, resolved_at: str):
        """Sets the resolved_at of this Response.


        :param resolved_at: The resolved_at of this Response.
        :type resolved_at: str
        """
        # if resolved_at is None:
        #     raise ValueError("Invalid value for `resolved_at`, must not be `None`")  # noqa: E501

        cls._resolved_at = resolved_at

    @property
    def dispatched_to(cls) -> str:
        """Gets the dispatched_to of this Response.


        :return: The dispatched_to of this Response.
        :rtype: str
        """
        return cls._dispatched_to

    @dispatched_to.setter
    def dispatched_to(cls, dispatched_to: str):
        """Sets the dispatched_to of this Response.


        :param dispatched_to: The dispatched_to of this Response.
        :type dispatched_to: str
        """
        # if dispatched_to is None:
        #     raise ValueError("Invalid value for `dispatched_to`, must not be `None`")  # noqa: E501

        cls._dispatched_to = dispatched_to

    @property
    def dispatched_result(cls) -> str:
        """Gets the dispatched_result of this Response.


        :return: The dispatched_result of this Response.
        :rtype: str
        """
        return cls._dispatched_result

    @dispatched_result.setter
    def dispatched_result(cls, dispatched_result: str):
        """Sets the dispatched_result of this Response.


        :param dispatched_result: The dispatched_result of this Response.
        :type dispatched_result: str
        """
        # if dispatched_result is None:
        #     raise ValueError("Invalid value for `dispatched_result`, must not be `None`")  # noqa: E501

        cls._dispatched_result = dispatched_result

    @property
    def dispatched_nodetype(cls) -> str:
        """Gets the dispatched_nodetype of this Response.


        :return: The dispatched_nodetype of this Response.
        :rtype: str
        """
        return cls._dispatched_nodetype

    @dispatched_nodetype.setter
    def dispatched_nodetype(cls, dispatched_nodetype: str):
        """Sets the dispatched_nodetype of this Response.


        :param dispatched_nodetype: The dispatched_nodetype of this Response.
        :type dispatched_nodetype: str
        """
        # if dispatched_nodetype is None:
        #     raise ValueError("Invalid value for `dispatched_nodetype`, must not be `None`")  # noqa: E501

        cls._dispatched_nodetype = dispatched_nodetype

    @property
    def multisign_account(cls) -> str:
        """Gets the multisign_account of this Response.


        :return: The multisign_account of this Response.
        :rtype: str
        """
        return cls._multisign_account

    @multisign_account.setter
    def multisign_account(cls, multisign_account: str):
        """Sets the multisign_account of this Response.


        :param multisign_account: The multisign_account of this Response.
        :type multisign_account: str
        """
        # if multisign_account is None:
        #     raise ValueError("Invalid value for `multisign_account`, must not be `None`")  # noqa: E501

        cls._multisign_account = multisign_account

    @property
    def account(cls) -> str:
        """Gets the account of this Response.


        :return: The account of this Response.
        :rtype: str
        """
        return cls._account

    @account.setter
    def account(cls, account: str):
        """Sets the account of this Response.


        :param account: The account of this Response.
        :type account: str
        """
        # if account is None:
        #     raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        cls._account = account

    @property
    def approved_with(self) -> str:
        """Gets the approved_with of this Response.


        :return: The approved_with of this Response.
        :rtype: str
        """
        return self._approved_with

    @approved_with.setter
    def approved_with(self, approved_with: str):
        """Sets the approved_with of this Response.


        :param approved_with: The approved_with of this Response.
        :type approved_with: str
        """
        allowed_values = ["PIN", "BIOMETRIC", "PASSPHRASE", "OTHER"]  # noqa: E501
        if approved_with and approved_with not in allowed_values:
            raise ValueError(
                "Invalid value for `approved_with` ({0}), must be one of {1}"
                .format(approved_with, allowed_values)
            )

        self._approved_with = approved_with


class RequestJson(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'transaction_type': True,
        'sign_in': True
    }
    model_types = {
        'transaction_type': str,
        'sign_in': bool
    }

    attribute_map = {
        'transaction_type': 'TransactionType',
        'sign_in': 'SignIn'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The RequestJson of this RequestJson.  # noqa: E501
        :rtype: RequestJson
        """
        cls.sanity_check(kwargs)
        cls._transaction_type = None
        cls._sign_in = None
        cls.transaction_type = kwargs['transaction_type']
        cls.sign_in = kwargs['sign_in']

    def to_dict(cls) -> Dict[str, object]:
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
        if issubclass(RequestJson, dict):
            for key, value in cls.items():
                result[key] = value

        return {
            k: v for k, v in result.items()
            if v is not None or k in
            cls.required and k in cls.nullable
        }

    @property
    def transaction_type(cls) -> str:
        """Gets the transaction_type of this RequestJson.


        :return: The transaction_type of this RequestJson.
        :rtype: str
        """
        return cls._transaction_type

    @transaction_type.setter
    def transaction_type(cls, transaction_type: str):
        """Sets the transaction_type of this RequestJson.


        :param transaction_type: The transaction_type of this RequestJson.
        :type transaction_type: str
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        cls._transaction_type = transaction_type

    @property
    def sign_in(cls) -> bool:
        """Gets the sign_in of this RequestJson.


        :return: The sign_in of this RequestJson.
        :rtype: bool
        """
        return cls._sign_in

    @sign_in.setter
    def sign_in(cls, sign_in: bool):
        """Sets the sign_in of this RequestJson.


        :param sign_in: The sign_in of this RequestJson.
        :type sign_in: bool
        """
        if sign_in is None:
            raise ValueError("Invalid value for `sign_in`, must not be `None`")  # noqa: E501

        cls._sign_in = sign_in


class Payload(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    nullable = {
        'tx_destination_tag': True,
        'origintype': True,
        'signmethod': True,
    }
    required = {
        'tx_type': True,
        'tx_destination': True,
        'tx_destination_tag': True,
        'request_json': True,
        'origintype': True,
        'signmethod': True,
        'created_at': True,
        'expires_at': True,
        'expires_in_seconds': True
    }

    model_types = {
        'tx_type': str,
        'tx_destination': str,
        'tx_destination_tag': str,
        'request_json': dict,
        'origintype': str,
        'signmethod': str,
        'created_at': str,
        'expires_at': str,
        'expires_in_seconds': int
    }

    attribute_map = {
        'tx_type': 'tx_type',
        'tx_destination': 'tx_destination',
        'tx_destination_tag': 'tx_destination_tag',
        'request_json': 'request_json',
        'origintype': 'origintype',
        'signmethod': 'signmethod',
        'created_at': 'created_at',
        'expires_at': 'expires_at',
        'expires_in_seconds': 'expires_in_seconds'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Payload of this Payload.  # noqa: E501
        :rtype: Payload
        """
        cls.sanity_check(kwargs)
        cls._tx_type = None
        cls._tx_destination = None
        cls._tx_destination_tag = None
        cls._request_json = None
        cls._origintype = None
        cls._signmethod = None
        cls._created_at = None
        cls._expires_at = None
        cls._expires_in_seconds = None
        cls.tx_type = kwargs['tx_type']
        cls.tx_destination = kwargs['tx_destination']
        cls.tx_destination_tag = kwargs['tx_destination_tag']
        cls.request_json = kwargs['request_json']
        cls.origintype = kwargs['origintype']
        cls.signmethod = kwargs['signmethod']
        cls.created_at = kwargs['created_at']
        cls.expires_at = kwargs['expires_at']
        cls.expires_in_seconds = kwargs['expires_in_seconds']

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
        if issubclass(Payload, dict):
            for key, value in cls.items():
                result[key] = value

        return {
            k: v for k, v in result.items()
            if v is not None or k in
            cls.required and k in cls.nullable
        }

    @property
    def tx_type(cls) -> str:
        """Gets the tx_type of this Payload.


        :return: The tx_type of this Payload.
        :rtype: str
        """
        return cls._tx_type

    @tx_type.setter
    def tx_type(cls, tx_type: str):
        """Sets the tx_type of this Payload.


        :param tx_type: The tx_type of this Payload.
        :type tx_type: str
        """
        if tx_type is None:
            raise ValueError("Invalid value for `tx_type`, must not be `None`")  # noqa: E501

        cls._tx_type = tx_type

    @property
    def tx_destination(cls) -> str:
        """Gets the tx_destination of this Payload.


        :return: The tx_destination of this Payload.
        :rtype: str
        """
        return cls._tx_destination

    @tx_destination.setter
    def tx_destination(cls, tx_destination: str):
        """Sets the tx_destination of this Payload.


        :param tx_destination: The tx_destination of this Payload.
        :type tx_destination: str
        """
        if tx_destination is None:
            raise ValueError("Invalid value for `tx_destination`, must not be `None`")  # noqa: E501

        cls._tx_destination = tx_destination

    @property
    def tx_destination_tag(cls) -> str:
        """Gets the tx_destination_tag of this Payload.


        :return: The tx_destination_tag of this Payload.
        :rtype: str
        """
        return cls._tx_destination_tag

    @tx_destination_tag.setter
    def tx_destination_tag(cls, tx_destination_tag: str):
        """Sets the tx_destination_tag of this Payload.


        :param tx_destination_tag: The tx_destination_tag of this Payload.
        :type tx_destination_tag: str
        """

        cls._tx_destination_tag = tx_destination_tag

    @property
    def request_json(cls) -> RequestJson:
        """Gets the request_json of this Payload.


        :return: The request_json of this Payload.
        :rtype: RequestJson
        """
        return cls._request_json

    @request_json.setter
    def request_json(cls, request_json: RequestJson):
        """Sets the request_json of this Payload.


        :param request_json: The request_json of this Payload.
        :type request_json: RequestJson
        """
        if request_json is None:
            raise ValueError("Invalid value for `request_json`, must not be `None`")  # noqa: E501

        cls._request_json = request_json

    @property
    def origintype(cls) -> str:
        """Gets the origintype of this Payload.


        :return: The origintype of this Payload.
        :rtype: str
        """
        return cls._origintype

    @origintype.setter
    def origintype(cls, origintype: str):
        """Sets the origintype of this Payload.


        :param origintype: The origintype of this Payload.
        :type origintype: str
        """
        # if origintype is None:
        #     raise ValueError("Invalid value for `origintype`, must not be `None`")  # noqa: E501

        cls._origintype = origintype

    @property
    def signmethod(cls) -> str:
        """Gets the signmethod of this Payload.


        :return: The signmethod of this Payload.
        :rtype: str
        """
        return cls._signmethod

    @signmethod.setter
    def signmethod(cls, signmethod: str):
        """Sets the signmethod of this Payload.


        :param signmethod: The signmethod of this Payload.
        :type signmethod: str
        """
        # if signmethod is None:
        #     raise ValueError("Invalid value for `signmethod`, must not be `None`")  # noqa: E501

        cls._signmethod = signmethod

    @property
    def created_at(cls) -> str:
        """Gets the created_at of this Payload.


        :return: The created_at of this Payload.
        :rtype: str
        """
        return cls._created_at

    @created_at.setter
    def created_at(cls, created_at: str):
        """Sets the created_at of this Payload.


        :param created_at: The created_at of this Payload.
        :type created_at: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        cls._created_at = created_at

    @property
    def expires_at(cls) -> str:
        """Gets the expires_at of this Payload.


        :return: The expires_at of this Payload.
        :rtype: str
        """
        return cls._expires_at

    @expires_at.setter
    def expires_at(cls, expires_at: str):
        """Sets the expires_at of this Payload.


        :param expires_at: The expires_at of this Payload.
        :type expires_at: str
        """
        if expires_at is None:
            raise ValueError("Invalid value for `expires_at`, must not be `None`")  # noqa: E501

        cls._expires_at = expires_at

    @property
    def expires_in_seconds(cls) -> int:
        """Gets the expires_in_seconds of this Payload.


        :return: The expires_in_seconds of this Payload.
        :rtype: int
        """
        return cls._expires_in_seconds

    @expires_in_seconds.setter
    def expires_in_seconds(cls, expires_in_seconds: int):
        """Sets the expires_in_seconds of this Payload.


        :param expires_in_seconds: The expires_in_seconds of this Payload.
        :type expires_in_seconds: int
        """
        if expires_in_seconds is None:
            raise ValueError("Invalid value for `expires_in_seconds`, must not be `None`")  # noqa: E501

        cls._expires_in_seconds = expires_in_seconds


class Application(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    nullable = {
        'issued_user_token': True
    }

    required = {
        'name': True,
        'description': True,
        'uuidv4': True,
        'disabled': True,
        'icon_url': True,
        'issued_user_token': True
    }

    model_types = {
        'name': str,
        'description': str,
        'uuidv4': str,
        'disabled': int,
        'icon_url': str,
        'issued_user_token': str
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'uuidv4': 'uuidv4',
        'disabled': 'disabled',
        'icon_url': 'icon_url',
        'issued_user_token': 'issued_user_token'
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
        cls._description = None
        cls._uuidv4 = None
        cls._disabled = None
        cls._icon_url = None
        cls._issued_user_token = None
        cls._name = kwargs['name']
        if 'description' in kwargs:
            cls._description = kwargs['description']
        cls._uuidv4 = kwargs['uuidv4']
        if 'disabled' in kwargs:
            cls._disabled = kwargs['disabled']
        if 'icon_url' in kwargs:
            cls._icon_url = kwargs['icon_url']
        if 'issued_user_token' in kwargs:
            cls._issued_user_token = kwargs['issued_user_token']

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
        if issubclass(Application, dict):
            for key, value in cls.items():
                result[key] = value

        return {
            k: v for k, v in result.items()
            if v is not None or k in
            cls.required and k in cls.nullable
        }

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

    @property
    def issued_user_token(cls) -> str:
        """Gets the issued_user_token of this Application.


        :return: The issued_user_token of this Application.
        :rtype: str
        """
        return cls._issued_user_token

    @issued_user_token.setter
    def issued_user_token(cls, issued_user_token: str):
        """Sets the issued_user_token of this Application.


        :param issued_user_token: The issued_user_token of this Application.
        :type issued_user_token: str
        """

        cls._issued_user_token = issued_user_token


class Result(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'cancelled': True,
        'reason': True
    }

    model_types = {
        'cancelled': bool,
        'reason': str
    }

    attribute_map = {
        'cancelled': 'cancelled',
        'reason': 'reason'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Result of this Result.  # noqa: E501
        :rtype: Result
        """
        cls.sanity_check(kwargs)
        cls._cancelled = None
        cls._reason = None
        cls.cancelled = kwargs['cancelled']
        cls.reason = kwargs['reason']

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
        if issubclass(Result, dict):
            for key, value in cls.items():
                result[key] = value

        return {
            k: v for k, v in result.items()
            if v is not None or k in
            cls.required and k in cls.nullable
        }

    @property
    def cancelled(cls) -> bool:
        """Gets the cancelled of this Result.


        :return: The cancelled of this Result.
        :rtype: bool
        """
        return cls._cancelled

    @cancelled.setter
    def cancelled(cls, cancelled: bool):
        """Sets the cancelled of this Result.


        :param cancelled: The cancelled of this Result.
        :type cancelled: bool
        """
        if cancelled is None:
            raise ValueError("Invalid value for `cancelled`, must not be `None`")  # noqa: E501

        cls._cancelled = cancelled

    @property
    def reason(cls) -> str:
        """Gets the reason of this Result.


        :return: The reason of this Result.
        :rtype: str
        """
        return cls._reason

    @reason.setter
    def reason(cls, reason: str):
        """Sets the reason of this Result.


        :param reason: The reason of this Result.
        :type reason: str
        """
        allowed_values = [
            "OK",
            "ALREADY_CANCELLED",
            "ALREADY_RESOLVED",
            "ALREADY_OPENED",
            "ALREADY_EXPIRED"
        ]  # noqa: E501
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"
                .format(reason, allowed_values)
            )

        cls._reason = reason


class Refs(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'qr_png': True,
        'qr_matrix': True,
        'qr_uri_quality_opts': True,
        'websocket_status': True
    }

    model_types = {
        'qr_png': str,
        'qr_matrix': str,
        'qr_uri_quality_opts': list,
        'websocket_status': str
    }

    attribute_map = {
        'qr_png': 'qr_png',
        'qr_matrix': 'qr_matrix',
        'qr_uri_quality_opts': 'qr_uri_quality_opts',
        'websocket_status': 'websocket_status'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Refs of this Refs.  # noqa: E501
        :rtype: Refs
        """
        cls.sanity_check(kwargs)
        cls._qr_png = None
        cls._qr_matrix = None
        cls._qr_uri_quality_opts = None
        cls._websocket_status = None
        cls.qr_png = kwargs['qr_png']
        cls.qr_matrix = kwargs['qr_matrix']
        cls.qr_uri_quality_opts = kwargs['qr_uri_quality_opts']
        cls.websocket_status = kwargs['websocket_status']

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
        if issubclass(Refs, dict):
            for key, value in cls.items():
                result[key] = value

        return {
            k: v for k, v in result.items()
            if v is not None or k in
            cls.required and k in cls.nullable
        }

    @property
    def qr_png(cls) -> str:
        """Gets the qr_png of this Refs.


        :return: The qr_png of this Refs.
        :rtype: str
        """
        return cls._qr_png

    @qr_png.setter
    def qr_png(cls, qr_png: str):
        """Sets the qr_png of this Refs.


        :param qr_png: The qr_png of this Refs.
        :type qr_png: str
        """
        if qr_png is None:
            raise ValueError("Invalid value for `qr_png`, must not be `None`")  # noqa: E501

        cls._qr_png = qr_png

    @property
    def qr_matrix(cls) -> str:
        """Gets the qr_matrix of this Refs.


        :return: The qr_matrix of this Refs.
        :rtype: str
        """
        return cls._qr_matrix

    @qr_matrix.setter
    def qr_matrix(cls, qr_matrix: str):
        """Sets the qr_matrix of this Refs.


        :param qr_matrix: The qr_matrix of this Refs.
        :type qr_matrix: str
        """
        if qr_matrix is None:
            raise ValueError("Invalid value for `qr_matrix`, must not be `None`")  # noqa: E501

        cls._qr_matrix = qr_matrix

    @property
    def qr_uri_quality_opts(cls) -> list:
        """Gets the qr_uri_quality_opts of this Refs.


        :return: The qr_uri_quality_opts of this Refs.
        :rtype: list
        """
        return cls._qr_uri_quality_opts

    @qr_uri_quality_opts.setter
    def qr_uri_quality_opts(cls, qr_uri_quality_opts: list):
        """Sets the qr_uri_quality_opts of this Refs.


        :param qr_uri_quality_opts: The qr_uri_quality_opts of this Refs.
        :type qr_uri_quality_opts: list
        """
        allowed_values = ["m", "q", "h"]  # noqa: E501
        if qr_uri_quality_opts != allowed_values:
            raise ValueError(
                "Invalid values for `qr_uri_quality_opts` ({0}), must be exacty {1}"  # noqa: E501
                .format(qr_uri_quality_opts, allowed_values)
            )

        cls._qr_uri_quality_opts = qr_uri_quality_opts

    @property
    def websocket_status(cls) -> str:
        """Gets the websocket_status of this Refs.


        :return: The websocket_status of this Refs.
        :rtype: str
        """
        return cls._websocket_status

    @websocket_status.setter
    def websocket_status(cls, websocket_status: str):
        """Sets the websocket_status of this Refs.


        :param websocket_status: The websocket_status of this Refs.
        :type websocket_status: str
        """
        if websocket_status is None:
            raise ValueError("Invalid value for `websocket_status`, must not be `None`")  # noqa: E501

        cls._websocket_status = websocket_status


class Next(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'always': True
    }

    model_types = {
        'always': str
    }

    attribute_map = {
        'always': 'always'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Next of this Next.  # noqa: E501
        :rtype: Next
        """
        cls.sanity_check(kwargs)
        cls._always = None
        cls.always = kwargs['always']

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
        if issubclass(Next, dict):
            for key, value in cls.items():
                result[key] = value

        return {
            k: v for k, v in result.items()
            if v is not None or k in
            cls.required and k in cls.nullable
        }

    @property
    def always(cls) -> str:
        """Gets the always of this Next.


        :return: The always of this Next.
        :rtype: str
        """
        return cls._always

    @always.setter
    def always(cls, always: str):
        """Sets the always of this Next.


        :param always: The always of this Next.
        :type always: str
        """
        if always is None:
            raise ValueError("Invalid value for `always`, must not be `None`")  # noqa: E501

        cls._always = always
