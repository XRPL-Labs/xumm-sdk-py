#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource
from typing import Union, Dict

from ..misc import (
    ReturnUrl,
    Options,
    Application,
    Payload,
    Response,
    Result,
    Next,
    Refs,
)

xumm_tx_types = [
  'SignIn'
]

xrpl_tx_types = [
  'Payment',
  'OfferCreate',
  'OfferCancel',
  'EscrowFinish',
  'EscrowCreate',
  'EscrowCancel',
  'DepositPreauth',
  'CheckCreate',
  'CheckCash',
  'CheckCancel',
  'AccountSet',
  'PaymentChannelCreate',
  'PaymentChannelFund',
  'SetRegularKey',
  'SignerListSet',
  'TrustSet',
  'EnableAmendment',
  'AccountDelete',
  'SetFee'
]


# XummTransactionType: str = xumm_tx_types[int]
# XrplTransactionType: str = xrpl_tx_types[int]
XummTransactionType: str = None
XrplTransactionType: str = None


class XummJsonTransaction(XummResource):
    def refresh_from(cls, **kwargs):
        cls._kwargs = kwargs

    def init_from(
        cls,
        transaction_type: Union[
            XummTransactionType,
            XrplTransactionType
        ]
    ):
        return {**cls._kwargs, **transaction_type}


class XummCustomMeta(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    nullable = {
        'identifier': True,
        'blob': True,
        'instruction': True
    }

    required = {
        'identifier': True,
        'blob': True,
        'instruction': True
    }

    model_types = {
        'identifier': str,
        'blob': dict,
        'instruction': str
    }

    attribute_map = {
        'identifier': 'identifier',
        'blob': 'blob',
        'instruction': 'instruction'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XummCustomMeta of this XummCustomMeta.  # noqa: E501
        :rtype: XummCustomMeta
        """
        # cls.sanity_check(kwargs)
        cls._identifier = None
        cls._blob = None
        cls._instruction = None
        if 'identifier' in kwargs:
            cls.identifier = kwargs['identifier']
        if 'blob' in kwargs:
            cls.blob = kwargs['blob']
        if 'instruction' in kwargs:
            cls.instruction = kwargs['instruction']

    @property
    def identifier(cls) -> str:
        """Gets the identifier of this XummCustomMeta.


        :return: The identifier of this XummCustomMeta.
        :rtype: str
        """
        return cls._identifier

    @identifier.setter
    def identifier(cls, identifier: str):
        """Sets the identifier of this XummCustomMeta.


        :param identifier: The identifier of this XummCustomMeta.
        :type identifier: str
        """

        cls._identifier = identifier

    @property
    def blob(cls) -> Dict[str, object]:
        """Gets the blob of this XummCustomMeta.


        :return: The blob of this XummCustomMeta.
        :rtype: Dict[str, object]
        """
        return cls._blob

    @blob.setter
    def blob(cls, blob: Dict[str, object]):
        """Sets the blob of this XummCustomMeta.


        :param blob: The blob of this XummCustomMeta.
        :type blob: Dict[str, object]
        """
        # if blob is None:
        #     raise ValueError("Invalid value for `blob`, must not be `None`")  # noqa: E501

        cls._blob = blob

    @property
    def instruction(cls) -> str:
        """Gets the instruction of this XummCustomMeta.


        :return: The instruction of this XummCustomMeta.
        :rtype: str
        """
        return cls._instruction

    @instruction.setter
    def instruction(cls, instruction: str):
        """Sets the instruction of this XummCustomMeta.


        :param instruction: The instruction of this XummCustomMeta.
        :type instruction: str
        """

        cls._instruction = instruction


class XummPayloadMeta(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    nullable = {
        'opened_by_deeplink': True,
        'return_url_app': True,
        'return_url_web': True,
    }
    required = {
        'exists': True,
        'uuid': True,
        'multisign': True,
        'submit': True,
        'destination': True,
        'resolved_destination': True,
        'resolved': True,
        'signed': True,
        'cancelled': True,
        'expired': True,
        'pushed': True,
        'app_opened': True,
        'opened_by_deeplink': True,
        # 'immutable': True,
        # 'force_account': True,
        'return_url_app': True,
        'return_url_web': True,
        'is_xapp': True
    }

    model_types = {
        'exists': bool,
        'uuid': str,
        'multisign': bool,
        'submit': bool,
        'destination': str,
        'resolved_destination': str,
        'resolved': bool,
        'signed': bool,
        'cancelled': bool,
        'expired': bool,
        'pushed': bool,
        'app_opened': bool,
        'opened_by_deeplink': bool,
        'immutable': bool,
        'force_account': bool,
        'return_url_app': str,
        'return_url_web': str,
        'is_xapp': bool
    }

    attribute_map = {
        'exists': 'exists',
        'uuid': 'uuid',
        'multisign': 'multisign',
        'submit': 'submit',
        'destination': 'destination',
        'resolved_destination': 'resolved_destination',
        'resolved': 'resolved',
        'signed': 'signed',
        'cancelled': 'cancelled',
        'expired': 'expired',
        'pushed': 'pushed',
        'app_opened': 'app_opened',
        'opened_by_deeplink': 'opened_by_deeplink',
        'immutable': 'immutable',
        'force_account': 'forceAccount',
        'return_url_app': 'return_url_app',
        'return_url_web': 'return_url_web',
        'is_xapp': 'is_xapp'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XummPayloadMeta of this XummPayloadMeta.  # noqa: E501
        :rtype: XummPayloadMeta
        """
        cls.sanity_check(kwargs)
        cls._exists = None
        cls._uuid = None
        cls._multisign = None
        cls._submit = None
        cls._destination = None
        cls._resolved_destination = None
        cls._resolved = None
        cls._signed = None
        cls._cancelled = None
        cls._expired = None
        cls._pushed = None
        cls._app_opened = None
        cls._opened_by_deeplink = None
        cls._immutable = None
        cls._force_account = None
        cls._return_url_app = None
        cls._return_url_web = None
        cls._is_xapp = None
        cls.exists = kwargs['exists']
        cls.uuid = kwargs['uuid']
        cls.multisign = kwargs['multisign']
        cls.submit = kwargs['submit']
        cls.destination = kwargs['destination']
        cls.resolved_destination = kwargs['resolved_destination']
        cls.resolved = kwargs['resolved']
        cls.signed = kwargs['signed']
        cls.cancelled = kwargs['cancelled']
        cls.expired = kwargs['expired']
        cls.pushed = kwargs['pushed']
        cls.app_opened = kwargs['app_opened']
        if 'opened_by_deeplink' in kwargs:
            cls.opened_by_deeplink = kwargs['opened_by_deeplink']
        if 'immutable' in kwargs:
            cls.immutable = kwargs['immutable']
        if 'forceAccount' in kwargs:
            cls.force_account = kwargs['forceAccount']
        if 'return_url_app' in kwargs:
            cls.return_url_app = kwargs['return_url_app']
        if 'return_url_web' in kwargs:
            cls.return_url_web = kwargs['return_url_web']
        cls.is_xapp = kwargs['is_xapp']

    @property
    def exists(cls) -> bool:
        """Gets the exists of this XummPayloadMeta.


        :return: The exists of this XummPayloadMeta.
        :rtype: bool
        """
        return cls._exists

    @exists.setter
    def exists(cls, exists: bool):
        """Sets the exists of this XummPayloadMeta.


        :param exists: The exists of this XummPayloadMeta.
        :type exists: bool
        """
        if exists is None:
            raise ValueError("Invalid value for `exists`, must not be `None`")  # noqa: E501

        cls._exists = exists

    @property
    def uuid(cls) -> str:
        """Gets the uuid of this XummPayloadMeta.


        :return: The uuid of this XummPayloadMeta.
        :rtype: str
        """
        return cls._uuid

    @uuid.setter
    def uuid(cls, uuid: str):
        """Sets the uuid of this XummPayloadMeta.


        :param uuid: The uuid of this XummPayloadMeta.
        :type uuid: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        cls._uuid = uuid

    @property
    def multisign(cls) -> bool:
        """Gets the multisign of this XummPayloadMeta.


        :return: The multisign of this XummPayloadMeta.
        :rtype: bool
        """
        return cls._multisign

    @multisign.setter
    def multisign(cls, multisign: bool):
        """Sets the multisign of this XummPayloadMeta.


        :param multisign: The multisign of this XummPayloadMeta.
        :type multisign: bool
        """
        if multisign is None:
            raise ValueError("Invalid value for `multisign`, must not be `None`")  # noqa: E501

        cls._multisign = multisign

    @property
    def submit(cls) -> bool:
        """Gets the submit of this XummPayloadMeta.


        :return: The submit of this XummPayloadMeta.
        :rtype: bool
        """
        return cls._submit

    @submit.setter
    def submit(cls, submit: bool):
        """Sets the submit of this XummPayloadMeta.


        :param submit: The submit of this XummPayloadMeta.
        :type submit: bool
        """
        if submit is None:
            raise ValueError("Invalid value for `submit`, must not be `None`")  # noqa: E501

        cls._submit = submit

    @property
    def destination(cls) -> str:
        """Gets the destination of this XummPayloadMeta.


        :return: The destination of this XummPayloadMeta.
        :rtype: str
        """
        return cls._destination

    @destination.setter
    def destination(cls, destination: str):
        """Sets the destination of this XummPayloadMeta.


        :param destination: The destination of this XummPayloadMeta.
        :type destination: str
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        cls._destination = destination

    @property
    def resolved_destination(cls) -> str:
        """Gets the resolved_destination of this XummPayloadMeta.


        :return: The resolved_destination of this XummPayloadMeta.
        :rtype: str
        """
        return cls._resolved_destination

    @resolved_destination.setter
    def resolved_destination(cls, resolved_destination: str):
        """Sets the resolved_destination of this XummPayloadMeta.


        :param resolved_destination: The resolved_destination of this XummPayloadMeta.  # noqa: E501
        :type resolved_destination: str
        """
        if resolved_destination is None:
            raise ValueError("Invalid value for `resolved_destination`, must not be `None`")  # noqa: E501

        cls._resolved_destination = resolved_destination

    @property
    def resolved(cls) -> bool:
        """Gets the resolved of this XummPayloadMeta.


        :return: The resolved of this XummPayloadMeta.
        :rtype: bool
        """
        return cls._resolved

    @resolved.setter
    def resolved(cls, resolved: bool):
        """Sets the resolved of this XummPayloadMeta.


        :param resolved: The resolved of this XummPayloadMeta.
        :type resolved: bool
        """
        if resolved is None:
            raise ValueError("Invalid value for `resolved`, must not be `None`")  # noqa: E501

        cls._resolved = resolved

    @property
    def signed(cls) -> bool:
        """Gets the signed of this XummPayloadMeta.


        :return: The signed of this XummPayloadMeta.
        :rtype: bool
        """
        return cls._signed

    @signed.setter
    def signed(cls, signed: bool):
        """Sets the signed of this XummPayloadMeta.


        :param signed: The signed of this XummPayloadMeta.
        :type signed: bool
        """
        if signed is None:
            raise ValueError("Invalid value for `signed`, must not be `None`")  # noqa: E501

        cls._signed = signed

    @property
    def cancelled(cls) -> bool:
        """Gets the cancelled of this XummPayloadMeta.


        :return: The cancelled of this XummPayloadMeta.
        :rtype: bool
        """
        return cls._cancelled

    @cancelled.setter
    def cancelled(cls, cancelled: bool):
        """Sets the cancelled of this XummPayloadMeta.


        :param cancelled: The cancelled of this XummPayloadMeta.
        :type cancelled: bool
        """
        if cancelled is None:
            raise ValueError("Invalid value for `cancelled`, must not be `None`")  # noqa: E501

        cls._cancelled = cancelled

    @property
    def expired(cls) -> bool:
        """Gets the expired of this XummPayloadMeta.


        :return: The expired of this XummPayloadMeta.
        :rtype: bool
        """
        return cls._expired

    @expired.setter
    def expired(cls, expired: bool):
        """Sets the expired of this XummPayloadMeta.


        :param expired: The expired of this XummPayloadMeta.
        :type expired: bool
        """
        if expired is None:
            raise ValueError("Invalid value for `expired`, must not be `None`")  # noqa: E501

        cls._expired = expired

    @property
    def pushed(cls) -> bool:
        """Gets the pushed of this XummPayloadMeta.


        :return: The pushed of this XummPayloadMeta.
        :rtype: bool
        """
        return cls._pushed

    @pushed.setter
    def pushed(cls, pushed: bool):
        """Sets the pushed of this XummPayloadMeta.


        :param pushed: The pushed of this XummPayloadMeta.
        :type pushed: bool
        """
        if pushed is None:
            raise ValueError("Invalid value for `pushed`, must not be `None`")  # noqa: E501

        cls._pushed = pushed

    @property
    def app_opened(cls) -> bool:
        """Gets the app_opened of this XummPayloadMeta.


        :return: The app_opened of this XummPayloadMeta.
        :rtype: bool
        """
        return cls._app_opened

    @app_opened.setter
    def app_opened(cls, app_opened: bool):
        """Sets the app_opened of this XummPayloadMeta.


        :param app_opened: The app_opened of this XummPayloadMeta.
        :type app_opened: bool
        """
        if app_opened is None:
            raise ValueError("Invalid value for `app_opened`, must not be `None`")  # noqa: E501

        cls._app_opened = app_opened

    @property
    def opened_by_deeplink(cls) -> bool:
        """Gets the opened_by_deeplink of this XummPayloadMeta.


        :return: The opened_by_deeplink of this XummPayloadMeta.
        :rtype: bool
        """
        return cls._opened_by_deeplink

    @opened_by_deeplink.setter
    def opened_by_deeplink(cls, opened_by_deeplink: bool):
        """Sets the opened_by_deeplink of this XummPayloadMeta.


        :param opened_by_deeplink: The opened_by_deeplink of this XummPayloadMeta.  # noqa: E501
        :type opened_by_deeplink: bool
        """
        # if opened_by_deeplink is None:
        #     raise ValueError("Invalid value for `opened_by_deeplink`, must not be `None`")  # noqa: E501

        cls._opened_by_deeplink = opened_by_deeplink

    @property
    def immutable(cls) -> bool:
        """Gets the immutable of this XummPayloadMeta.


        :return: The immutable of this XummPayloadMeta.
        :rtype: bool
        """
        return cls._immutable

    @immutable.setter
    def immutable(cls, immutable: bool):
        """Sets the immutable of this XummPayloadMeta.


        :param immutable: The immutable of this XummPayloadMeta.  # noqa: E501
        :type immutable: bool
        """

        cls._immutable = immutable

    @property
    def force_account(cls) -> bool:
        """Gets the force_account of this XummPayloadMeta.


        :return: The force_account of this XummPayloadMeta.
        :rtype: bool
        """
        return cls._force_account

    @force_account.setter
    def force_account(cls, force_account: bool):
        """Sets the force_account of this XummPayloadMeta.


        :param force_account: The force_account of this XummPayloadMeta.  # noqa: E501
        :type force_account: bool
        """

        cls._force_account = force_account

    @property
    def return_url_app(cls) -> str:
        """Gets the return_url_app of this XummPayloadMeta.


        :return: The return_url_app of this XummPayloadMeta.
        :rtype: str
        """
        return cls._return_url_app

    @return_url_app.setter
    def return_url_app(cls, return_url_app: str):
        """Sets the return_url_app of this XummPayloadMeta.


        :param return_url_app: The return_url_app of this XummPayloadMeta.
        :type return_url_app: str
        """
        # if return_url_app is None:
        #     raise ValueError("Invalid value for `return_url_app`, must not be `None`")  # noqa: E501

        cls._return_url_app = return_url_app

    @property
    def return_url_web(cls) -> str:
        """Gets the return_url_web of this XummPayloadMeta.


        :return: The return_url_web of this XummPayloadMeta.
        :rtype: str
        """
        return cls._return_url_web

    @return_url_web.setter
    def return_url_web(cls, return_url_web: str):
        """Sets the return_url_web of this XummPayloadMeta.


        :param return_url_web: The return_url_web of this XummPayloadMeta.
        :type return_url_web: str
        """
        # if return_url_web is None:
        #     raise ValueError("Invalid value for `return_url_web`, must not be `None`")  # noqa: E501

        cls._return_url_web = return_url_web

    @property
    def is_xapp(cls) -> bool:
        """Gets the is_xapp of this XummPayloadMeta.


        :return: The is_xapp of this XummPayloadMeta.
        :rtype: bool
        """
        return cls._is_xapp

    @is_xapp.setter
    def is_xapp(cls, is_xapp: bool):
        """Sets the is_xapp of this XummPayloadMeta.


        :param is_xapp: The is_xapp of this XummPayloadMeta.
        :type is_xapp: bool
        """
        if is_xapp is None:
            raise ValueError("Invalid value for `is_xapp`, must not be `None`")  # noqa: E501

        cls._is_xapp = is_xapp


# class XummJsonTransaction(XummResource):
#     """
#     Attributes:
#       model_types (dict): The key is attribute name
#                             and the value is attribute type.
#       attribute_map (dict): The key is attribute name
#                             and the value is json key in definition.
#     """
#     required = {
#         'txjson': True
#     }

#     model_types = {
#         'txjson': dict,
#     }

#     attribute_map = {
#         'txjson': 'txjson',
#     }

#     def refresh_from(cls, **kwargs):
#         """Returns the dict as a model

#         :param kwargs: A dict.
#         :type: dict
#         :return: The XummPayloadBodyBase of this XummPayloadBodyBase.  # noqa: E501
#         :rtype: XummPayloadBodyBase
#         """
#         cls.sanity_check(kwargs)
#         cls._txjson = None
#         cls.txjson = kwargs['txjson']

#     def to_dict(cls):
#         """Returns the model properties as a dict"""
#         result = {}

#         for attr, _ in six.iteritems(cls.model_types):
#             value = getattr(cls, attr)
#             attr = cls.attribute_map[attr]
#             if isinstance(value, list):
#                 result[attr] = list(map(
#                     lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
#                     value
#                 ))
#             elif hasattr(value, "to_dict"):
#                 result[attr] = value.to_dict()
#             elif isinstance(value, dict):
#                 result[attr] = dict(map(
#                     lambda item: (item[0], item[1].to_dict())
#                     if hasattr(item[1], "to_dict") else item,
#                     value.items()
#                 ))
#             else:
#                 result[attr] = value
#         if issubclass(XummJsonTransaction, dict):
#             for key, value in cls.items():
#                 result[key] = value

#         return {k: v for k, v in result.items() if v is not None}

#     @property
#     def txjson(cls) -> Dict[str, object]:
#         """Gets the txjson of this XummCustomMeta.


#         :return: The txjson of this XummCustomMeta.
#         :rtype: Dict[str, object]
#         """
#         return cls._txjson

#     @txjson.setter
#     def txjson(cls, txjson: Dict[str, object]):
#         """Sets the txjson of this XummCustomMeta.


#         :param txjson: The txjson of this XummCustomMeta.
#         :type txjson: Dict[str, object]
#         """
#         if txjson is None:
#             raise ValueError("Invalid value for `txjson`, must not be `None`")  # noqa: E501

#         cls._txjson = txjson


class XummPayloadBodyBase(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {}

    model_types = {
        'user_token': str,
        'options': dict,
        'custom_meta': dict,
    }

    attribute_map = {
        'user_token': 'user_token',
        'options': 'options',
        'custom_meta': 'custom_meta',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XummPayloadBodyBase of this XummPayloadBodyBase.  # noqa: E501
        :rtype: XummPayloadBodyBase
        """
        cls.sanity_check(kwargs)
        cls._user_token = None
        cls._options = None
        cls._custom_meta = None
        if 'user_token' in kwargs:
            cls.user_token = kwargs['_user_token']
        if 'options' in kwargs:
            cls.options = kwargs['options']
        if 'custom_meta' in kwargs:
            cls.custom_meta = kwargs['custom_meta']

    @property
    def user_token(self) -> str:
        """Gets the user_token of this XummPayloadBodyBase.


        :return: The user_token of this XummPayloadBodyBase.
        :rtype: str
        """
        return self._user_token

    @user_token.setter
    def user_token(self, user_token: str):
        """Sets the user_token of this XummPayloadBodyBase.


        :param user_token: The user_token of this XummPayloadBodyBase.
        :type user_token: str
        """

        self._user_token = user_token

    @property
    def options(self) -> Options:
        """Gets the options of this XummPayloadBodyBase.


        :return: The options of this XummPayloadBodyBase.
        :rtype: Options
        """
        return self._options

    @options.setter
    def options(self, options: Options):
        """Sets the options of this XummPayloadBodyBase.


        :param options: The options of this XummPayloadBodyBase.
        :type options: Options
        """

        self._options = options

    @property
    def custom_meta(self) -> XummCustomMeta:
        """Gets the custom_meta of this XummPayloadBodyBase.


        :return: The custom_meta of this XummPayloadBodyBase.
        :rtype: XummCustomMeta
        """
        return self._custom_meta

    @custom_meta.setter
    def custom_meta(self, custom_meta: XummCustomMeta):
        """Sets the custom_meta of this XummPayloadBodyBase.


        :param custom_meta: The custom_meta of this XummPayloadBodyBase.
        :type custom_meta: XummCustomMeta
        """

        self._custom_meta = custom_meta


class XummPostPayloadBodyJson(XummPayloadBodyBase):
    def __init__(cls, txjson: XummJsonTransaction = None):
        cls._txjson = None
        cls.txjson = txjson

    @property
    def txjson(self) -> XummJsonTransaction:
        """Gets the txjson of this XummPostPayloadBodyJson.


        :return: The txjson of this XummPostPayloadBodyJson.
        :rtype: XummJsonTransaction
        """
        return self._txjson

    @txjson.setter
    def txjson(self, txjson: XummJsonTransaction):
        """Sets the txjson of this XummPostPayloadBodyJson.


        :param txjson: The txjson of this XummPostPayloadBodyJson.
        :type txjson: TxJson
        """
        if txjson is None:
            raise ValueError("Invalid value for `txjson`, must not be `None`")  # noqa: E501

        self._txjson = txjson


class XummPostPayloadBodyBlob(XummPayloadBodyBase):
    def __init__(cls, txblob: str = None):
        cls._txblob = None
        cls.txblob = txblob

    @property
    def txblob(self) -> str:
        """Gets the txblob of this XummPostPayloadBodyBlob.


        :return: The txblob of this XummPostPayloadBodyBlob.
        :rtype: str
        """
        return self._txblob

    @txblob.setter
    def txblob(self, txblob: str):
        """Sets the txblob of this XummPostPayloadBodyBlob.


        :param txblob: The txblob of this XummPostPayloadBodyBlob.
        :type txblob: srt
        """
        if txblob is None:
            raise ValueError("Invalid value for `txblob`, must not be `None`")  # noqa: E501

        self._txblob = txblob

# export type CreatePayload = XummPostPayloadBodyJson | XummPostPayloadBodyBlob
# class CreatePayload(XummPayloadBodyBase):


class XummPostPayloadResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'uuid': True,
        'next': True,
        'refs': True,
        'pushed': True
    }

    model_types = {
        'uuid': str,
        'next': dict,
        'refs': dict,
        'pushed': bool
    }

    attribute_map = {
        'uuid': 'uuid',
        'next': 'next',
        'refs': 'refs',
        'pushed': 'pushed'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XummPostPayloadResponse of this XummPostPayloadResponse.  # noqa: E501
        :rtype: XummPostPayloadResponse
        """
        cls.sanity_check(kwargs)
        cls._uuid = None
        cls._next = None
        cls._refs = None
        cls._pushed = None
        cls.uuid = kwargs['uuid']
        cls.next = Next(**kwargs['next'])
        cls.refs = Refs(**kwargs['refs'])
        cls.pushed = kwargs['pushed']

    @property
    def uuid(cls) -> str:
        """Gets the uuid of this XummPostPayloadResponse.


        :return: The uuid of this XummPostPayloadResponse.
        :rtype: str
        """
        return cls._uuid

    @uuid.setter
    def uuid(cls, uuid: str):
        """Sets the uuid of this XummPostPayloadResponse.


        :param uuid: The uuid of this XummPostPayloadResponse.
        :type uuid: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        cls._uuid = uuid

    @property
    def next(cls) -> Next:
        """Gets the next of this XummPostPayloadResponse.


        :return: The next of this XummPostPayloadResponse.
        :rtype: Next
        """
        return cls._next

    @next.setter
    def next(cls, next: Next):
        """Sets the next of this XummPostPayloadResponse.


        :param next: The next of this XummPostPayloadResponse.
        :type next: Next
        """
        if next is None:
            raise ValueError("Invalid value for `next`, must not be `None`")  # noqa: E501

        cls._next = next

    @property
    def refs(cls) -> Refs:
        """Gets the refs of this XummPostPayloadResponse.


        :return: The refs of this XummPostPayloadResponse.
        :rtype: Refs
        """
        return cls._refs

    @refs.setter
    def refs(cls, refs: Refs):
        """Sets the refs of this XummPostPayloadResponse.


        :param refs: The refs of this XummPostPayloadResponse.
        :type refs: Refs
        """
        if refs is None:
            raise ValueError("Invalid value for `refs`, must not be `None`")  # noqa: E501

        cls._refs = refs

    @property
    def pushed(cls) -> bool:
        """Gets the pushed of this XummPostPayloadResponse.


        :return: The pushed of this XummPostPayloadResponse.
        :rtype: bool
        """
        return cls._pushed

    @pushed.setter
    def pushed(cls, pushed: bool):
        """Sets the pushed of this XummPostPayloadResponse.


        :param pushed: The pushed of this XummPostPayloadResponse.
        :type pushed: bool
        """
        if pushed is None:
            raise ValueError("Invalid value for `pushed`, must not be `None`")  # noqa: E501

        cls._pushed = pushed


class XummGetPayloadResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'meta': True,
        'application': True,
        'payload': True,
        'response': True,
        'custom_meta': True
    }

    model_types = {
        'meta': dict,
        'application': dict,
        'payload': dict,
        'response': dict,
        'custom_meta': dict
    }

    attribute_map = {
        'meta': 'meta',
        'application': 'application',
        'payload': 'payload',
        'response': 'response',
        'custom_meta': 'custom_meta'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XummGetPayloadResponse of this XummGetPayloadResponse.  # noqa: E501
        :rtype: XummGetPayloadResponse
        """
        cls.sanity_check(kwargs)
        cls._meta = None
        cls._application = None
        cls._payload = None
        cls._response = None
        cls._custom_meta = None
        cls.meta = XummPayloadMeta(**kwargs['meta'])
        cls.application = Application(**kwargs['application'])
        cls.payload = Payload(**kwargs['payload'])
        cls.response = Response(**kwargs['response'])
        cls.custom_meta = XummCustomMeta(**kwargs['custom_meta'])

    @property
    def meta(cls) -> XummPayloadMeta:
        """Gets the meta of this XummGetPayloadResponse.


        :return: The meta of this XummGetPayloadResponse.
        :rtype: XummPayloadMeta
        """
        return cls._meta

    @meta.setter
    def meta(cls, meta: XummPayloadMeta):
        """Sets the meta of this XummGetPayloadResponse.


        :param meta: The meta of this XummGetPayloadResponse.
        :type meta: XummPayloadMeta
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        cls._meta = meta

    @property
    def application(cls) -> Application:
        """Gets the application of this XummGetPayloadResponse.


        :return: The application of this XummGetPayloadResponse.
        :rtype: Application
        """
        return cls._application

    @application.setter
    def application(cls, application: Application):
        """Sets the application of this XummGetPayloadResponse.


        :param application: The application of this XummGetPayloadResponse.
        :type application: Application
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        cls._application = application

    @property
    def payload(cls) -> Payload:
        """Gets the payload of this XummGetPayloadResponse.


        :return: The payload of this XummGetPayloadResponse.
        :rtype: Payload
        """
        return cls._payload

    @payload.setter
    def payload(cls, payload: Payload):
        """Sets the payload of this XummGetPayloadResponse.


        :param payload: The payload of this XummGetPayloadResponse.
        :type payload: Payload
        """
        if payload is None:
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        cls._payload = payload

    @property
    def response(cls) -> Response:
        """Gets the response of this XummGetPayloadResponse.


        :return: The response of this XummGetPayloadResponse.
        :rtype: Response
        """
        return cls._response

    @response.setter
    def response(cls, response: Response):
        """Sets the response of this XummGetPayloadResponse.


        :param response: The response of this XummGetPayloadResponse.
        :type response: Response
        """
        if response is None:
            raise ValueError("Invalid value for `response`, must not be `None`")  # noqa: E501

        cls._response = response

    @property
    def custom_meta(cls) -> XummCustomMeta:
        """Gets the custom_meta of this XummGetPayloadResponse.


        :return: The custom_meta of this XummGetPayloadResponse.
        :rtype: XummCustomMeta
        """
        return cls._custom_meta

    @custom_meta.setter
    def custom_meta(cls, custom_meta: XummCustomMeta):
        """Sets the custom_meta of this XummGetPayloadResponse.


        :param custom_meta: The custom_meta of this XummGetPayloadResponse.
        :type custom_meta: XummCustomMeta
        """
        if custom_meta is None:
            raise ValueError("Invalid value for `custom_meta`, must not be `None`")  # noqa: E501

        cls._custom_meta = custom_meta


class XummDeletePayloadResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'result': True,
        'meta': True,
        'custom_meta': True
    }

    model_types = {
        'result': dict,
        'meta': dict,
        'custom_meta': dict
    }

    attribute_map = {
        'result': 'result',
        'meta': 'meta',
        'custom_meta': 'custom_meta'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XummDeletePayloadResponse of this XummDeletePayloadResponse.  # noqa: E501
        :rtype: XummDeletePayloadResponse
        """
        cls.sanity_check(kwargs)
        cls._result = None
        cls._meta = None
        cls._custom_meta = None
        cls.result = Result(**kwargs['result'])
        cls.meta = XummPayloadMeta(**kwargs['meta'])
        cls.custom_meta = XummCustomMeta(**kwargs['custom_meta'])

    @property
    def result(cls) -> Result:
        """Gets the result of this XummDeletePayloadResponse.


        :return: The result of this XummDeletePayloadResponse.
        :rtype: Result
        """
        return cls._result

    @result.setter
    def result(cls, result: Result):
        """Sets the result of this XummDeletePayloadResponse.


        :param result: The result of this XummDeletePayloadResponse.
        :type result: Result
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        cls._result = result

    @property
    def meta(cls) -> XummPayloadMeta:
        """Gets the meta of this XummDeletePayloadResponse.


        :return: The meta of this XummDeletePayloadResponse.
        :rtype: XummPayloadMeta
        """
        return cls._meta

    @meta.setter
    def meta(cls, meta: XummPayloadMeta):
        """Sets the meta of this XummDeletePayloadResponse.


        :param meta: The meta of this XummDeletePayloadResponse.
        :type meta: XummPayloadMeta
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        cls._meta = meta

    @property
    def custom_meta(cls) -> XummCustomMeta:
        """Gets the custom_meta of this XummDeletePayloadResponse.


        :return: The custom_meta of this XummDeletePayloadResponse.
        :rtype: XummCustomMeta
        """
        return cls._custom_meta

    @custom_meta.setter
    def custom_meta(cls, custom_meta: XummCustomMeta):
        """Sets the custom_meta of this XummDeletePayloadResponse.


        :param custom_meta: The custom_meta of this XummDeletePayloadResponse.
        :type custom_meta: XummCustomMeta
        """
        if custom_meta is None:
            raise ValueError("Invalid value for `custom_meta`, must not be `None`")  # noqa: E501

        cls._custom_meta = custom_meta


class WebhookMeta(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'url': True,
        'application_uuidv4': True,
        'payload_uuidv4': True
    }

    model_types = {
        'url': str,
        'application_uuidv4': str,
        'payload_uuidv4': str
    }

    attribute_map = {
        'url': 'url',
        'application_uuidv4': 'application_uuidv4',
        'payload_uuidv4': 'payload_uuidv4'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The WebhookMeta of this WebhookMeta.  # noqa: E501
        :rtype: WebhookMeta
        """
        cls.sanity_check(kwargs)
        cls._url = None
        cls._application_uuidv4 = None
        cls._payload_uuidv4 = None
        cls.url = kwargs['url']
        cls.application_uuidv4 = kwargs['application_uuidv4']
        cls.payload_uuidv4 = kwargs['payload_uuidv4']

    @property
    def url(cls) -> str:
        """Gets the url of this WebhookMeta.


        :return: The url of this WebhookMeta.
        :rtype: str
        """
        return cls._url

    @url.setter
    def url(cls, url: str):
        """Sets the url of this WebhookMeta.


        :param url: The url of this WebhookMeta.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        cls._url = url

    @property
    def application_uuidv4(cls) -> str:
        """Gets the application_uuidv4 of this WebhookMeta.


        :return: The application_uuidv4 of this WebhookMeta.
        :rtype: str
        """
        return cls._application_uuidv4

    @application_uuidv4.setter
    def application_uuidv4(cls, application_uuidv4: str):
        """Sets the application_uuidv4 of this WebhookMeta.


        :param application_uuidv4: The application_uuidv4 of this WebhookMeta.
        :type application_uuidv4: str
        """
        if application_uuidv4 is None:
            raise ValueError("Invalid value for `application_uuidv4`, must not be `None`")  # noqa: E501

        cls._application_uuidv4 = application_uuidv4

    @property
    def payload_uuidv4(cls) -> str:
        """Gets the payload_uuidv4 of this WebhookMeta.


        :return: The payload_uuidv4 of this WebhookMeta.
        :rtype: str
        """
        return cls._payload_uuidv4

    @payload_uuidv4.setter
    def payload_uuidv4(cls, payload_uuidv4: str):
        """Sets the payload_uuidv4 of this WebhookMeta.


        :param payload_uuidv4: The payload_uuidv4 of this WebhookMeta.
        :type payload_uuidv4: str
        """
        if payload_uuidv4 is None:
            raise ValueError("Invalid value for `payload_uuidv4`, must not be `None`")  # noqa: E501

        cls._payload_uuidv4 = payload_uuidv4


class WebhookResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    nullable = {}

    required = {
        'payload_uuidv4': True,
        'reference_call_uuidv4': True,
        'signed': True,
        'user_token': True,
        'return_url': True,
    }

    model_types = {
        'payload_uuidv4': str,
        'reference_call_uuidv4': str,
        'signed': bool,
        'user_token': str,
        'return_url': dict,
    }

    attribute_map = {
        'payload_uuidv4': 'payload_uuidv4',
        'reference_call_uuidv4': 'reference_call_uuidv4',
        'signed': 'signed',
        'user_token': 'user_token',
        'return_url': 'return_url',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The WebhookResponse of this WebhookResponse.  # noqa: E501
        :rtype: WebhookResponse
        """
        cls.sanity_check(kwargs)
        cls._payload_uuidv4 = None
        cls._reference_call_uuidv4 = None
        cls._signed = None
        cls._user_token = None
        cls._return_url = None
        cls.payload_uuidv4 = kwargs['payload_uuidv4']
        cls.reference_call_uuidv4 = kwargs['reference_call_uuidv4']
        cls.signed = kwargs['signed']
        cls.user_token = kwargs['user_token']
        cls.return_url = ReturnUrl(**kwargs['return_url'])
        return cls

    @property
    def payload_uuidv4(cls) -> str:
        """Gets the payload_uuidv4 of this WebhookResponse.


        :return: The payload_uuidv4 of this WebhookResponse.
        :rtype: str
        """
        return cls._payload_uuidv4

    @payload_uuidv4.setter
    def payload_uuidv4(cls, payload_uuidv4: str):
        """Sets the payload_uuidv4 of this WebhookResponse.


        :param payload_uuidv4: The payload_uuidv4 of this WebhookResponse.
        :type payload_uuidv4: str
        """
        # if payload_uuidv4 is None:
        #     raise ValueError("Invalid value for `payload_uuidv4`, must not be `None`")  # noqa: E501

        cls._payload_uuidv4 = payload_uuidv4

    @property
    def reference_call_uuidv4(cls) -> str:
        """Gets the reference_call_uuidv4 of this WebhookResponse.


        :return: The reference_call_uuidv4 of this WebhookResponse.
        :rtype: str
        """
        return cls._reference_call_uuidv4

    @reference_call_uuidv4.setter
    def reference_call_uuidv4(cls, reference_call_uuidv4: str):
        """Sets the reference_call_uuidv4 of this WebhookResponse.


        :param reference_call_uuidv4: The reference_call_uuidv4 of this WebhookResponse.  # noqa: E501
        :type reference_call_uuidv4: str
        """

        cls._txid = reference_call_uuidv4

    @property
    def signed(cls) -> bool:
        """Gets the signed of this WebhookResponse.


        :return: The signed of this WebhookResponse.
        :rtype: bool
        """
        return cls._signed

    @signed.setter
    def signed(cls, signed: bool):
        """Sets the signed of this WebhookResponse.


        :param signed: The signed of this WebhookResponse.
        :type signed: bool
        """

        cls._signed = signed

    @property
    def user_token(cls) -> str:
        """Gets the user_token of this WebhookResponse.


        :return: The user_token of this WebhookResponse.
        :rtype: str
        """
        return cls._user_token

    @user_token.setter
    def user_token(cls, user_token: str):
        """Sets the dispatched_to of this WebhookResponse.


        :param user_token: The user_token of this WebhookResponse.
        :type user_token: str
        """

        cls._user_token = user_token

    @property
    def return_url(cls) -> ReturnUrl:
        """Gets the return_url of this WebhookResponse.


        :return: The return_url of this WebhookResponse.
        :rtype: str
        """
        return cls._return_url

    @return_url.setter
    def return_url(cls, return_url: ReturnUrl):
        """Sets the dispatched_to of this WebhookResponse.


        :param return_url: The return_url of this WebhookResponse.
        :type return_url: str
        """

        cls._return_url = return_url


class UserToken(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'user_token': True,
        'token_issued': True,
        'token_expiration': True
    }

    model_types = {
        'user_token': str,
        'token_issued': int,
        'token_expiration': int
    }

    attribute_map = {
        'user_token': 'user_token',
        'token_issued': 'token_issued',
        'token_expiration': 'token_expiration'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The UserToken of this UserToken.  # noqa: E501
        :rtype: UserToken
        """
        cls.sanity_check(kwargs)
        cls._user_token = None
        cls._token_issued = None
        cls._token_expiration = None
        cls.user_token = kwargs['user_token']
        cls.token_issued = kwargs['token_issued']
        cls.token_expiration = kwargs['token_expiration']

    @property
    def user_token(cls) -> str:
        """Gets the user_token of this UserToken.


        :return: The user_token of this UserToken.
        :rtype: str
        """
        return cls._user_token

    @user_token.setter
    def user_token(cls, user_token: str):
        """Sets the user_token of this UserToken.


        :param user_token: The user_token of this UserToken.
        :type user_token: str
        """
        if user_token is None:
            raise ValueError("Invalid value for `user_token`, must not be `None`")  # noqa: E501

        cls._user_token = user_token

    @property
    def token_issued(cls) -> int:
        """Gets the token_issued of this UserToken.


        :return: The token_issued of this UserToken.
        :rtype: int
        """
        return cls._user_token

    @token_issued.setter
    def token_issued(cls, token_issued: int):
        """Sets the token_issued of this UserToken.


        :param token_issued: The token_issued of this UserToken.
        :type token_issued: int
        """
        if token_issued is None:
            raise ValueError("Invalid value for `token_issued`, must not be `None`")  # noqa: E501

        cls._token_issued = token_issued

    @property
    def token_expiration(cls) -> int:
        """Gets the token_expiration of this UserToken.


        :return: The token_expiration of this UserToken.
        :rtype: int
        """
        return cls._token_expiration

    @token_expiration.setter
    def token_expiration(cls, token_expiration: int):
        """Sets the token_expiration of this UserToken.


        :param token_expiration: The token_expiration of this UserToken.
        :type token_expiration: int
        """
        if token_expiration is None:
            raise ValueError("Invalid value for `token_expiration`, must not be `None`")  # noqa: E501

        cls._token_expiration = token_expiration


class XummWebhookBody(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'meta': True,
        'custom_meta': True,
        'payload_response': True,
        'user_token': True
    }

    model_types = {
        'meta': dict,
        'custom_meta': dict,
        'payload_response': dict,
        'user_token': dict
    }

    attribute_map = {
        'meta': 'meta',
        'custom_meta': 'custom_meta',
        'payload_response': 'payloadResponse',
        'user_token': 'user_token'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XummWebhookBody of this XummWebhookBody.  # noqa: E501
        :rtype: XummWebhookBody
        """
        cls.sanity_check(kwargs)
        cls._meta = None
        cls._custom_meta = None
        cls._payload_response = None
        cls._user_token = None
        cls.meta = WebhookMeta(**kwargs['meta'])
        cls.custom_meta = XummCustomMeta(**kwargs['custom_meta'])
        cls.payload_response = WebhookResponse(**kwargs['payloadResponse'])
        cls.user_token = UserToken(**kwargs['user_token'])

    @property
    def meta(cls) -> WebhookMeta:
        """Gets the meta of this XummWebhookBody.


        :return: The meta of this XummWebhookBody.
        :rtype: WebhookMeta
        """
        return cls._meta

    @meta.setter
    def meta(cls, meta: WebhookMeta):
        """Sets the meta of this XummWebhookBody.


        :param meta: The meta of this XummWebhookBody.
        :type meta: WebhookMeta
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        cls._meta = meta

    @property
    def custom_meta(cls) -> XummCustomMeta:
        """Gets the custom_meta of this XummWebhookBody.


        :return: The custom_meta of this XummWebhookBody.
        :rtype: XummCustomMeta
        """
        return cls._custom_meta

    @custom_meta.setter
    def custom_meta(cls, custom_meta: XummCustomMeta):
        """Sets the custom_meta of this XummWebhookBody.


        :param custom_meta: The custom_meta of this XummWebhookBody.
        :type custom_meta: XummCustomMeta
        """
        if custom_meta is None:
            raise ValueError("Invalid value for `custom_meta`, must not be `None`")  # noqa: E501

        cls._custom_meta = custom_meta

    @property
    def payload_response(cls) -> WebhookResponse:
        """Gets the payload_response of this XummWebhookBody.


        :return: The payload_response of this XummWebhookBody.
        :rtype: WebhookResponse
        """
        return cls._payload_response

    @payload_response.setter
    def payload_response(cls, payload_response: WebhookResponse):
        """Sets the payload_response of this XummWebhookBody.


        :param payload_response: The payload_response of this XummWebhookBody.
        :type payload_response: WebhookResponse
        """

        cls._payload_response = payload_response

    @property
    def user_token(cls) -> UserToken:
        """Gets the user_token of this XummWebhookBody.


        :return: The user_token of this XummWebhookBody.
        :rtype: UserToken
        """
        return cls._user_token

    @user_token.setter
    def user_token(cls, user_token: UserToken):
        """Sets the user_token of this XummWebhookBody.


        :param user_token: The user_token of this XummWebhookBody.
        :type user_token: UserToken
        """
        if user_token is None:
            raise ValueError("Invalid value for `user_token`, must not be `None`")  # noqa: E501

        cls._user_token = user_token
