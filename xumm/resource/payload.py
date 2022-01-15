import os
from xumm.resource import XummResource
import six
import json

from typing import List, Dict  # noqa: F401

class Refs(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    model_types = {
        'qr_png': 'str',
        'qr_matrix': 'str',
        'qr_uri_quality_opts': 'str',
        'websocket_status': 'str'
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
        cls._qr_png = kwargs['qr_png']
        cls._qr_matrix = kwargs['qr_matrix']
        cls._qr_uri_quality_opts = kwargs['qr_uri_quality_opts']
        cls._websocket_status = kwargs['websocket_status']
        
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
        if issubclass(Refs, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}
    
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
    def qr_uri_quality_opts(cls) -> str:
        """Gets the qr_uri_quality_opts of this Refs.


        :return: The qr_uri_quality_opts of this Refs.
        :rtype: str
        """
        return cls._qr_uri_quality_opts

    @qr_uri_quality_opts.setter
    def qr_uri_quality_opts(cls, qr_uri_quality_opts: str):
        """Sets the qr_uri_quality_opts of this Refs.


        :param qr_uri_quality_opts: The qr_uri_quality_opts of this Refs.
        :type qr_uri_quality_opts: str
        """
        if qr_uri_quality_opts is None:
            raise ValueError("Invalid value for `qr_uri_quality_opts`, must not be `None`")  # noqa: E501

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

    model_types = {
        'always': 'str'
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
        cls._always = kwargs['always']

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
        if issubclass(Next, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

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


class PostPayloadResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'uuid': 'str',
        'next': 'Next',
        'refs': 'Refs',
        'pushed': 'bool'
    }

    attribute_map = {
        'uuid': 'uuid',
        'next': 'next',
        'refs': 'refs',
        'pushed': 'pushed'
    }

    @classmethod
    def post_url(cls):
        """post_url."""
        return super(PostPayloadResponse, cls).platform_url() + 'payload' + '/'
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The PostPayloadResponse of this PostPayloadResponse.  # noqa: E501
        :rtype: PostPayloadResponse
        """
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._uuid = kwargs['uuid']
        cls._next = Next(**kwargs['next'])
        cls._refs = Refs(**kwargs['refs'])
        cls._pushed = kwargs['pushed']

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
        if issubclass(PostPayloadResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def uuid(cls) -> str:
        """Gets the uuid of this PostPayloadResponse.


        :return: The uuid of this PostPayloadResponse.
        :rtype: str
        """
        return cls._uuid

    @uuid.setter
    def uuid(cls, uuid: str):
        """Sets the uuid of this PostPayloadResponse.


        :param uuid: The uuid of this PostPayloadResponse.
        :type uuid: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        cls._uuid = uuid

    @property
    def next(cls) -> Next:
        """Gets the next of this PostPayloadResponse.


        :return: The next of this PostPayloadResponse.
        :rtype: Next
        """
        return cls._next

    @next.setter
    def next(cls, next: Next):
        """Sets the next of this PostPayloadResponse.


        :param next: The next of this PostPayloadResponse.
        :type next: Next
        """
        if next is None:
            raise ValueError("Invalid value for `next`, must not be `None`")  # noqa: E501

        cls._next = next

    @property
    def refs(cls) -> Refs:
        """Gets the refs of this PostPayloadResponse.


        :return: The refs of this PostPayloadResponse.
        :rtype: Refs
        """
        return cls._refs

    @refs.setter
    def refs(cls, refs: Refs):
        """Sets the refs of this PostPayloadResponse.


        :param refs: The refs of this PostPayloadResponse.
        :type refs: Refs
        """
        if refs is None:
            raise ValueError("Invalid value for `refs`, must not be `None`")  # noqa: E501

        cls._refs = refs

    @property
    def pushed(cls) -> bool:
        """Gets the pushed of this PostPayloadResponse.


        :return: The pushed of this PostPayloadResponse.
        :rtype: bool
        """
        return cls._pushed

    @pushed.setter
    def pushed(cls, pushed: bool):
        """Sets the pushed of this PostPayloadResponse.


        :param pushed: The pushed of this PostPayloadResponse.
        :type pushed: bool
        """
        if pushed is None:
            raise ValueError("Invalid value for `pushed`, must not be `None`")  # noqa: E501

        cls._pushed = pushed


class CustomMeta(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'identifier': 'str',
        'blob': 'dict(str, object)',
        'instruction': 'str'
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
        :return: The CustomMeta of this CustomMeta.  # noqa: E501
        :rtype: CustomMeta
        """
        if 'identifier' in kwargs:
            cls._identifier = kwargs['identifier']
        cls._blob = kwargs['blob']
        if 'instruction' in kwargs:
            cls._instruction = kwargs['instruction']

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
        if issubclass(CustomMeta, dict):
            for key, value in cls.items():
                result[key] = value

        return result
        # return {k: v for k, v in result.items() if v is not None}

    @property
    def identifier(cls) -> str:
        """Gets the identifier of this CustomMeta.


        :return: The identifier of this CustomMeta.
        :rtype: str
        """
        return cls._identifier

    @identifier.setter
    def identifier(cls, identifier: str):
        """Sets the identifier of this CustomMeta.


        :param identifier: The identifier of this CustomMeta.
        :type identifier: str
        """

        cls._identifier = identifier

    @property
    def blob(cls) -> Dict[str, object]:
        """Gets the blob of this CustomMeta.


        :return: The blob of this CustomMeta.
        :rtype: Dict[str, object]
        """
        return cls._blob

    @blob.setter
    def blob(cls, blob: Dict[str, object]):
        """Sets the blob of this CustomMeta.


        :param blob: The blob of this CustomMeta.
        :type blob: Dict[str, object]
        """
        if blob is None:
            raise ValueError("Invalid value for `blob`, must not be `None`")  # noqa: E501

        cls._blob = blob

    @property
    def instruction(cls) -> str:
        """Gets the instruction of this CustomMeta.


        :return: The instruction of this CustomMeta.
        :rtype: str
        """
        return cls._instruction

    @instruction.setter
    def instruction(cls, instruction: str):
        """Sets the instruction of this CustomMeta.


        :param instruction: The instruction of this CustomMeta.
        :type instruction: str
        """

        cls._instruction = instruction

class Meta(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'exists': 'bool',
        'uuid': 'str',
        'multisign': 'bool',
        'submit': 'bool',
        'destination': 'str',
        'resolved_destination': 'str',
        'resolved': 'bool',
        'signed': 'bool',
        'cancelled': 'bool',
        'expired': 'bool',
        'pushed': 'bool',
        'app_opened': 'bool',
        'opened_by_deeplink': 'bool',
        'return_url_app': 'str',
        'return_url_web': 'str',
        'is_xapp': 'bool'
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
        'return_url_app': 'return_url_app',
        'return_url_web': 'return_url_web',
        'is_xapp': 'is_xapp'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Meta of this Meta.  # noqa: E501
        :rtype: Meta
        """
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
        cls._return_url_app = None
        cls._return_url_web = None
        cls._is_xapp = None
        cls._exists = kwargs['exists']
        cls._uuid = kwargs['uuid']
        cls._multisign = kwargs['multisign']
        cls._submit = kwargs['submit']
        cls._destination = kwargs['destination']
        cls._resolved_destination = kwargs['resolved_destination']
        cls._resolved = kwargs['resolved']
        cls._signed = kwargs['signed']
        cls._cancelled = kwargs['cancelled']
        cls._expired = kwargs['expired']
        cls._pushed = kwargs['pushed']
        cls._app_opened = kwargs['app_opened']
        cls._opened_by_deeplink = kwargs['opened_by_deeplink']
        cls._return_url_app = kwargs['return_url_app']
        cls._return_url_web = kwargs['return_url_web']
        cls._is_xapp = kwargs['is_xapp']

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
        if issubclass(Meta, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def exists(cls) -> bool:
        """Gets the exists of this Meta.


        :return: The exists of this Meta.
        :rtype: bool
        """
        return cls._exists

    @exists.setter
    def exists(cls, exists: bool):
        """Sets the exists of this Meta.


        :param exists: The exists of this Meta.
        :type exists: bool
        """
        if exists is None:
            raise ValueError("Invalid value for `exists`, must not be `None`")  # noqa: E501

        cls._exists = exists

    @property
    def uuid(cls) -> str:
        """Gets the uuid of this Meta.


        :return: The uuid of this Meta.
        :rtype: str
        """
        return cls._uuid

    @uuid.setter
    def uuid(cls, uuid: str):
        """Sets the uuid of this Meta.


        :param uuid: The uuid of this Meta.
        :type uuid: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        cls._uuid = uuid

    @property
    def multisign(cls) -> bool:
        """Gets the multisign of this Meta.


        :return: The multisign of this Meta.
        :rtype: bool
        """
        return cls._multisign

    @multisign.setter
    def multisign(cls, multisign: bool):
        """Sets the multisign of this Meta.


        :param multisign: The multisign of this Meta.
        :type multisign: bool
        """
        if multisign is None:
            raise ValueError("Invalid value for `multisign`, must not be `None`")  # noqa: E501

        cls._multisign = multisign

    @property
    def submit(cls) -> bool:
        """Gets the submit of this Meta.


        :return: The submit of this Meta.
        :rtype: bool
        """
        return cls._submit

    @submit.setter
    def submit(cls, submit: bool):
        """Sets the submit of this Meta.


        :param submit: The submit of this Meta.
        :type submit: bool
        """
        if submit is None:
            raise ValueError("Invalid value for `submit`, must not be `None`")  # noqa: E501

        cls._submit = submit

    @property
    def destination(cls) -> str:
        """Gets the destination of this Meta.


        :return: The destination of this Meta.
        :rtype: str
        """
        return cls._destination

    @destination.setter
    def destination(cls, destination: str):
        """Sets the destination of this Meta.


        :param destination: The destination of this Meta.
        :type destination: str
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        cls._destination = destination

    @property
    def resolved_destination(cls) -> str:
        """Gets the resolved_destination of this Meta.


        :return: The resolved_destination of this Meta.
        :rtype: str
        """
        return cls._resolved_destination

    @resolved_destination.setter
    def resolved_destination(cls, resolved_destination: str):
        """Sets the resolved_destination of this Meta.


        :param resolved_destination: The resolved_destination of this Meta.
        :type resolved_destination: str
        """
        if resolved_destination is None:
            raise ValueError("Invalid value for `resolved_destination`, must not be `None`")  # noqa: E501

        cls._resolved_destination = resolved_destination

    @property
    def resolved(cls) -> bool:
        """Gets the resolved of this Meta.


        :return: The resolved of this Meta.
        :rtype: bool
        """
        return cls._resolved

    @resolved.setter
    def resolved(cls, resolved: bool):
        """Sets the resolved of this Meta.


        :param resolved: The resolved of this Meta.
        :type resolved: bool
        """
        if resolved is None:
            raise ValueError("Invalid value for `resolved`, must not be `None`")  # noqa: E501

        cls._resolved = resolved

    @property
    def signed(cls) -> bool:
        """Gets the signed of this Meta.


        :return: The signed of this Meta.
        :rtype: bool
        """
        return cls._signed

    @signed.setter
    def signed(cls, signed: bool):
        """Sets the signed of this Meta.


        :param signed: The signed of this Meta.
        :type signed: bool
        """
        if signed is None:
            raise ValueError("Invalid value for `signed`, must not be `None`")  # noqa: E501

        cls._signed = signed

    @property
    def cancelled(cls) -> bool:
        """Gets the cancelled of this Meta.


        :return: The cancelled of this Meta.
        :rtype: bool
        """
        return cls._cancelled

    @cancelled.setter
    def cancelled(cls, cancelled: bool):
        """Sets the cancelled of this Meta.


        :param cancelled: The cancelled of this Meta.
        :type cancelled: bool
        """
        if cancelled is None:
            raise ValueError("Invalid value for `cancelled`, must not be `None`")  # noqa: E501

        cls._cancelled = cancelled

    @property
    def expired(cls) -> bool:
        """Gets the expired of this Meta.


        :return: The expired of this Meta.
        :rtype: bool
        """
        return cls._expired

    @expired.setter
    def expired(cls, expired: bool):
        """Sets the expired of this Meta.


        :param expired: The expired of this Meta.
        :type expired: bool
        """
        if expired is None:
            raise ValueError("Invalid value for `expired`, must not be `None`")  # noqa: E501

        cls._expired = expired

    @property
    def pushed(cls) -> bool:
        """Gets the pushed of this Meta.


        :return: The pushed of this Meta.
        :rtype: bool
        """
        return cls._pushed

    @pushed.setter
    def pushed(cls, pushed: bool):
        """Sets the pushed of this Meta.


        :param pushed: The pushed of this Meta.
        :type pushed: bool
        """
        if pushed is None:
            raise ValueError("Invalid value for `pushed`, must not be `None`")  # noqa: E501

        cls._pushed = pushed

    @property
    def app_opened(cls) -> bool:
        """Gets the app_opened of this Meta.


        :return: The app_opened of this Meta.
        :rtype: bool
        """
        return cls._app_opened

    @app_opened.setter
    def app_opened(cls, app_opened: bool):
        """Sets the app_opened of this Meta.


        :param app_opened: The app_opened of this Meta.
        :type app_opened: bool
        """
        if app_opened is None:
            raise ValueError("Invalid value for `app_opened`, must not be `None`")  # noqa: E501

        cls._app_opened = app_opened

    @property
    def opened_by_deeplink(cls) -> bool:
        """Gets the opened_by_deeplink of this Meta.


        :return: The opened_by_deeplink of this Meta.
        :rtype: bool
        """
        return cls._opened_by_deeplink

    @opened_by_deeplink.setter
    def opened_by_deeplink(cls, opened_by_deeplink: bool):
        """Sets the opened_by_deeplink of this Meta.


        :param opened_by_deeplink: The opened_by_deeplink of this Meta.
        :type opened_by_deeplink: bool
        """
        if opened_by_deeplink is None:
            raise ValueError("Invalid value for `opened_by_deeplink`, must not be `None`")  # noqa: E501

        cls._opened_by_deeplink = opened_by_deeplink

    @property
    def return_url_app(cls) -> str:
        """Gets the return_url_app of this Meta.


        :return: The return_url_app of this Meta.
        :rtype: str
        """
        return cls._return_url_app

    @return_url_app.setter
    def return_url_app(cls, return_url_app: str):
        """Sets the return_url_app of this Meta.


        :param return_url_app: The return_url_app of this Meta.
        :type return_url_app: str
        """
        if return_url_app is None:
            raise ValueError("Invalid value for `return_url_app`, must not be `None`")  # noqa: E501

        cls._return_url_app = return_url_app

    @property
    def return_url_web(cls) -> str:
        """Gets the return_url_web of this Meta.


        :return: The return_url_web of this Meta.
        :rtype: str
        """
        return cls._return_url_web

    @return_url_web.setter
    def return_url_web(cls, return_url_web: str):
        """Sets the return_url_web of this Meta.


        :param return_url_web: The return_url_web of this Meta.
        :type return_url_web: str
        """
        if return_url_web is None:
            raise ValueError("Invalid value for `return_url_web`, must not be `None`")  # noqa: E501

        cls._return_url_web = return_url_web

    @property
    def is_xapp(cls) -> bool:
        """Gets the is_xapp of this Meta.


        :return: The is_xapp of this Meta.
        :rtype: bool
        """
        return cls._is_xapp

    @is_xapp.setter
    def is_xapp(cls, is_xapp: bool):
        """Sets the is_xapp of this Meta.


        :param is_xapp: The is_xapp of this Meta.
        :type is_xapp: bool
        """
        if is_xapp is None:
            raise ValueError("Invalid value for `is_xapp`, must not be `None`")  # noqa: E501

        cls._is_xapp = is_xapp

class Result(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'cancelled': 'bool',
        'reason': 'str'
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
        cls._cancelled = kwargs['cancelled']
        cls._reason = kwargs['reason']

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
        if issubclass(Result, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

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
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        cls._reason = reason

class DeletePayloadResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'result': 'Result',
        'meta': 'Meta',
        'custom_meta': 'CustomMeta'
    }

    attribute_map = {
        'result': 'result',
        'meta': 'meta',
        'custom_meta': 'custom_meta'
    }

    @classmethod
    def delete_url(cls, id):
        """delete_url."""
        return super(DeletePayloadResponse, cls).platform_url() + 'payload' + '/' + id
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The DeletePayloadResponse of this DeletePayloadResponse.  # noqa: E501
        :rtype: DeletePayloadResponse
        """
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._result = Result(**kwargs['result'])
        cls._meta = Meta(**kwargs['meta'])
        cls._custom_meta = CustomMeta(**kwargs['custom_meta'])

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
        if issubclass(DeletePayloadResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def result(cls) -> Result:
        """Gets the result of this PayloadDeleteResponse.


        :return: The result of this PayloadDeleteResponse.
        :rtype: Result
        """
        return cls._result

    @result.setter
    def result(cls, result: Result):
        """Sets the result of this PayloadDeleteResponse.


        :param result: The result of this PayloadDeleteResponse.
        :type result: Result
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        cls._result = result

    @property
    def meta(cls) -> Meta:
        """Gets the meta of this PayloadDeleteResponse.


        :return: The meta of this PayloadDeleteResponse.
        :rtype: Meta
        """
        return cls._meta

    @meta.setter
    def meta(cls, meta: Meta):
        """Sets the meta of this PayloadDeleteResponse.


        :param meta: The meta of this PayloadDeleteResponse.
        :type meta: Meta
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        cls._meta = meta

    @property
    def custom_meta(cls) -> CustomMeta:
        """Gets the custom_meta of this PayloadDeleteResponse.


        :return: The custom_meta of this PayloadDeleteResponse.
        :rtype: CustomMeta
        """
        return cls._custom_meta

    @custom_meta.setter
    def custom_meta(cls, custom_meta: CustomMeta):
        """Sets the custom_meta of this PayloadDeleteResponse.


        :param custom_meta: The custom_meta of this PayloadDeleteResponse.
        :type custom_meta: CustomMeta
        """
        if custom_meta is None:
            raise ValueError("Invalid value for `custom_meta`, must not be `None`")  # noqa: E501

        cls._custom_meta = custom_meta


class Response(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'hex': 'str',
        'txid': 'str',
        'resolved_at': 'str',
        'dispatched_to': 'str',
        'dispatched_result': 'str',
        'dispatched_nodetype': 'str',
        'multisign_account': 'str',
        'account': 'str'
    }

    attribute_map = {
        'hex': 'hex',
        'txid': 'txid',
        'resolved_at': 'resolved_at',
        'dispatched_to': 'dispatched_to',
        'dispatched_result': 'dispatched_result',
        'dispatched_nodetype': 'dispatched_nodetype',
        'multisign_account': 'multisign_account',
        'account': 'account'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The Response of this Response.  # noqa: E501
        :rtype: Response
        """
        cls._hex = None
        cls._txid = None
        cls._resolved_at = None
        cls._dispatched_to = None
        cls._dispatched_result = None
        cls._dispatched_nodetype = None
        cls._multisign_account = None
        cls._account = None
        cls.hex = kwargs['hex']
        cls.txid = kwargs['txid']
        cls.resolved_at = kwargs['resolved_at']
        cls.dispatched_to = kwargs['dispatched_to']
        cls.dispatched_result = kwargs['dispatched_result']
        cls.dispatched_nodetype = kwargs['dispatched_nodetype']
        cls.multisign_account = kwargs['multisign_account']
        cls.account = kwargs['account']

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
        if issubclass(Response, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

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
        if hex is None:
            raise ValueError("Invalid value for `hex`, must not be `None`")  # noqa: E501

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
        if txid is None:
            raise ValueError("Invalid value for `txid`, must not be `None`")  # noqa: E501

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
        if resolved_at is None:
            raise ValueError("Invalid value for `resolved_at`, must not be `None`")  # noqa: E501

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
        if dispatched_to is None:
            raise ValueError("Invalid value for `dispatched_to`, must not be `None`")  # noqa: E501

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
        if dispatched_result is None:
            raise ValueError("Invalid value for `dispatched_result`, must not be `None`")  # noqa: E501

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
        if dispatched_nodetype is None:
            raise ValueError("Invalid value for `dispatched_nodetype`, must not be `None`")  # noqa: E501

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
        if multisign_account is None:
            raise ValueError("Invalid value for `multisign_account`, must not be `None`")  # noqa: E501

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
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        cls._account = account

class RequestJson(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'transaction_type': 'str',
        'sign_in': 'bool'
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
        cls._transaction_type = None
        cls._sign_in = None
        cls.transaction_type = kwargs['transaction_type']
        cls.sign_in = kwargs['sign_in']

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
        if issubclass(RequestJson, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

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
    model_types = {
        'tx_type': 'str',
        'tx_destination': 'str',
        'tx_destination_tag': 'str',
        'request_json': 'RequestJson',
        'origintype': 'str',
        'signmethod': 'str',
        'created_at': 'str',
        'expires_at': 'str',
        'expires_in_seconds': 'int'
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
        if issubclass(Payload, dict):
            for key, value in cls.items():
                result[key] = value

        return result
        # return {k: v for k, v in result.items() if v is not None}

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
        if origintype is None:
            raise ValueError("Invalid value for `origintype`, must not be `None`")  # noqa: E501

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
        if signmethod is None:
            raise ValueError("Invalid value for `signmethod`, must not be `None`")  # noqa: E501

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

    model_types = {
        'name': 'str',
        'description': 'str',
        'uuidv4': 'str',
        'disabled': 'int',
        'icon_url': 'str',
        'issued_user_token': 'str'
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
        if issubclass(Application, dict):
            for key, value in cls.items():
                result[key] = value

        return result
        # return {k: v for k, v in result.items() if v is not None}

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


class GetPayloadResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'meta': 'Meta',
        'application': 'Application',
        'payload': 'Payload',
        'response': 'Response',
        'custom_meta': 'CustomMeta'
    }

    attribute_map = {
        'meta': 'meta',
        'application': 'application',
        'payload': 'payload',
        'response': 'response',
        'custom_meta': 'custom_meta'
    }

    @classmethod
    def get_url(cls, id):
        """get_url."""
        return super(GetPayloadResponse, cls).platform_url() + 'payload' + '/' + id
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The GetPayloadResponse of this GetPayloadResponse.  # noqa: E501
        :rtype: GetPayloadResponse
        """
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._meta = None
        cls._application = None
        cls._payload = None
        cls._response = None
        cls._custom_meta = None
        cls._meta = Meta(**kwargs['meta'])
        cls._application = Application(**kwargs['application'])
        cls._payload = Payload(**kwargs['payload'])
        cls._response = Response(**kwargs['response'])
        cls._custom_meta = CustomMeta(**kwargs['custom_meta'])

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
        if issubclass(GetPayloadResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def meta(cls) -> Meta:
        """Gets the meta of this GetPayloadResponse.


        :return: The meta of this GetPayloadResponse.
        :rtype: Meta
        """
        return cls._meta

    @meta.setter
    def meta(cls, meta: Meta):
        """Sets the meta of this GetPayloadResponse.


        :param meta: The meta of this GetPayloadResponse.
        :type meta: Meta
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        cls._meta = meta

    @property
    def application(cls) -> Application:
        """Gets the application of this GetPayloadResponse.


        :return: The application of this GetPayloadResponse.
        :rtype: Application
        """
        return cls._application

    @application.setter
    def application(cls, application: Application):
        """Sets the application of this GetPayloadResponse.


        :param application: The application of this GetPayloadResponse.
        :type application: Application
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        cls._application = application

    @property
    def payload(cls) -> Payload:
        """Gets the payload of this GetPayloadResponse.


        :return: The payload of this GetPayloadResponse.
        :rtype: Payload
        """
        return cls._payload

    @payload.setter
    def payload(cls, payload: Payload):
        """Sets the payload of this GetPayloadResponse.


        :param payload: The payload of this GetPayloadResponse.
        :type payload: Payload
        """
        if payload is None:
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        cls._payload = payload

    @property
    def response(cls) -> Response:
        """Gets the response of this GetPayloadResponse.


        :return: The response of this GetPayloadResponse.
        :rtype: Response
        """
        return cls._response

    @response.setter
    def response(cls, response: Response):
        """Sets the response of this GetPayloadResponse.


        :param response: The response of this GetPayloadResponse.
        :type response: Response
        """
        if response is None:
            raise ValueError("Invalid value for `response`, must not be `None`")  # noqa: E501

        cls._response = response

    @property
    def custom_meta(cls) -> CustomMeta:
        """Gets the custom_meta of this GetPayloadResponse.


        :return: The custom_meta of this GetPayloadResponse.
        :rtype: CustomMeta
        """
        return cls._custom_meta

    @custom_meta.setter
    def custom_meta(cls, custom_meta: CustomMeta):
        """Sets the custom_meta of this GetPayloadResponse.


        :param custom_meta: The custom_meta of this GetPayloadResponse.
        :type custom_meta: CustomMeta
        """
        if custom_meta is None:
            raise ValueError("Invalid value for `custom_meta`, must not be `None`")  # noqa: E501

        cls._custom_meta = custom_meta

from typing import Callable, Any
from websocket import WebSocketApp

class PayloadSubscription(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'payload': 'Payload',
        'resolve': 'Callable[[Any], Any]',
        'resolved': 'Callable[[Any], Any]',
        'websocket': 'Response',
    }

    attribute_map = {
        'payload': 'payload',
        'resolve': 'resolve',
        'resolved': 'resolved',
        'websocket': 'websocket',
    }
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The GetPayloadResponse of this GetPayloadResponse.  # noqa: E501
        :rtype: GetPayloadResponse
        """
        # print(kwargs)
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._payload = None
        cls._payload = GetPayloadResponse(**kwargs['payload'])
        cls._resolve = None
        cls._resolve = kwargs['resolve']
        cls._resolved = None
        cls._resolved = kwargs['resolved']
        cls._websocket = None
        cls._websocket = kwargs['websocket']

    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.model_types):
            value = getattr(cls, attr)
            attr = cls.attribute_map[attr]
            if attr == 'websocket' or attr == 'resolve':
                result[attr] = value
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
        if issubclass(GetPayloadResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return result
        # return {k: v for k, v in result.items() if v is not None}

    @property
    def payload(cls) -> Payload:
        """Gets the payload of this PayloadSubscription.


        :return: The payload of this PayloadSubscription.
        :rtype: Payload
        """
        return cls._payload

    @payload.setter
    def payload(cls, payload: Payload):
        """Sets the payload of this PayloadSubscription.


        :param payload: The payload of this PayloadSubscription.
        :type meta: Payload
        """
        if payload is None:
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        cls._payload = payload

    @property
    def resolve(cls) -> Callable[[Any], Any]:
        """Gets the resolve of this PayloadSubscription.


        :return: The resolve of this PayloadSubscription.
        :rtype: Callable
        """
        return cls._resolve

    @resolve.setter
    def resolve(cls, resolve: Callable[[Any], Any]):
        """Sets the resolve of this PayloadSubscription.


        :param resolve: The resolve of this PayloadSubscription.
        :type meta: Callable
        """
        if resolve is None:
            raise ValueError("Invalid value for `resolve`, must not be `None`")  # noqa: E501

        cls._resolve = resolve
        
    @property
    def resolved(cls) -> Callable[[Any], Any]:
        """Gets the resolved of this PayloadSubscription.


        :return: The resolved of this PayloadSubscription.
        :rtype: Callable
        """
        return cls._resolved

    @resolve.setter
    def resolve(cls, resolved: Callable[[Any], Any]):
        """Sets the resolved of this PayloadSubscription.


        :param resolved: The resolved of this PayloadSubscription.
        :type meta: Payload
        """
        if resolved is None:
            raise ValueError("Invalid value for `resolve`, must not be `None`")  # noqa: E501

        cls._resolved = resolved

    @property
    def websocket(cls) -> WebSocketApp:
        """Gets the websocket of this PayloadSubscription.


        :return: The websocket of this PayloadSubscription.
        :rtype: Payload
        """
        return cls._websocket

    @websocket.setter
    def websocket(cls, websocket: WebSocketApp):
        """Sets the websocket of this PayloadSubscription.


        :param websocket: The websocket of this PayloadSubscription.
        :type meta: Payload
        """
        if websocket is None:
            raise ValueError("Invalid value for `websocket`, must not be `None`")  # noqa: E501

        cls._websocket = websocket

class PayloadAndSubscription(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'created': 'PostPayloadResponse',
        'payload': 'GetPayloadResponse',
        'resolve': 'Callable[[Any], Any]',
        'resolved': 'Callable[[Any], Any]',
        'websocket': 'Response',
    }

    attribute_map = {
        'payload': 'payload',
        'resolve': 'resolve',
        'resolved': 'resolved',
        'websocket': 'websocket',
    }
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The PayloadAndSubscription of this PayloadAndSubscription.  # noqa: E501
        :rtype: PayloadAndSubscription
        """
        # print(kwargs)
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._payload = None
        cls._payload = GetPayloadResponse(**kwargs['payload'])
        cls._resolve = None
        cls._resolve = kwargs['resolve']
        cls._resolved = None
        cls._resolved = kwargs['resolved']
        cls._websocket = None
        cls._websocket = kwargs['websocket']

    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.model_types):
            value = getattr(cls, attr)
            attr = cls.attribute_map[attr]
            if attr == 'websocket' or attr == 'resolve':
                result[attr] = value
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
        if issubclass(GetPayloadResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return result
        # return {k: v for k, v in result.items() if v is not None}

    @property
    def created(cls) -> PostPayloadResponse:
        """Gets the created of this PayloadAndSubscription.


        :return: The created of this PayloadAndSubscription.
        :rtype: PostPayloadResponse
        """
        return cls._created

    @created.setter
    def created(cls, created: PostPayloadResponse):
        """Sets the created of this PayloadAndSubscription.


        :param created: The created of this PayloadAndSubscription.
        :type meta: PostPayloadResponse
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        cls._created = created

    @property
    def payload(cls) -> GetPayloadResponse:
        """Gets the payload of this PayloadAndSubscription.


        :return: The payload of this PayloadAndSubscription.
        :rtype: GetPayloadResponse
        """
        return cls._payload

    @payload.setter
    def payload(cls, payload: GetPayloadResponse):
        """Sets the payload of this PayloadAndSubscription.


        :param payload: The payload of this PayloadAndSubscription.
        :type meta: GetPayloadResponse
        """
        if payload is None:
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        cls._payload = payload

    @property
    def resolve(cls) -> Callable[[Any], Any]:
        """Gets the resolve of this PayloadAndSubscription.


        :return: The resolve of this PayloadAndSubscription.
        :rtype: Callable
        """
        return cls._resolve

    @resolve.setter
    def resolve(cls, resolve: Callable[[Any], Any]):
        """Sets the resolve of this PayloadAndSubscription.


        :param resolve: The resolve of this PayloadAndSubscription.
        :type meta: Callable
        """
        if resolve is None:
            raise ValueError("Invalid value for `resolve`, must not be `None`")  # noqa: E501

        cls._resolve = resolve
        
    @property
    def resolved(cls) -> Callable[[Any], Any]:
        """Gets the resolved of this PayloadAndSubscription.


        :return: The resolved of this PayloadAndSubscription.
        :rtype: Callable
        """
        return cls._resolved

    @resolve.setter
    def resolve(cls, resolved: Callable[[Any], Any]):
        """Sets the resolved of this PayloadAndSubscription.


        :param resolved: The resolved of this PayloadAndSubscription.
        :type meta: Payload
        """
        if resolved is None:
            raise ValueError("Invalid value for `resolve`, must not be `None`")  # noqa: E501

        cls._resolved = resolved

    @property
    def websocket(cls) -> WebSocketApp:
        """Gets the websocket of this PayloadAndSubscription.


        :return: The websocket of this PayloadAndSubscription.
        :rtype: Payload
        """
        return cls._websocket

    @websocket.setter
    def websocket(cls, websocket: WebSocketApp):
        """Sets the websocket of this PayloadAndSubscription.


        :param websocket: The websocket of this PayloadAndSubscription.
        :type meta: Payload
        """
        if websocket is None:
            raise ValueError("Invalid value for `websocket`, must not be `None`")  # noqa: E501

        cls._websocket = websocket