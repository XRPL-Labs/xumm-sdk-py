import os
from xumm.resource import XummResource
import six
import json

from typing import List, Dict  # noqa: F401

class Refs(XummResource):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
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
        if issubclass(Refs, dict):
            for key, value in cls.items():
                result[key] = value

        return result
    
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
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
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
        if issubclass(Next, dict):
            for key, value in cls.items():
                result[key] = value

        return result

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
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
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
        if issubclass(PostPayloadResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return result

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
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
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
        if issubclass(CustomMeta, dict):
            for key, value in cls.items():
                result[key] = value

        return result

    @property
    def identifier(self) -> str:
        """Gets the identifier of this CustomMeta.


        :return: The identifier of this CustomMeta.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: str):
        """Sets the identifier of this CustomMeta.


        :param identifier: The identifier of this CustomMeta.
        :type identifier: str
        """

        self._identifier = identifier

    @property
    def blob(self) -> Dict[str, object]:
        """Gets the blob of this CustomMeta.


        :return: The blob of this CustomMeta.
        :rtype: Dict[str, object]
        """
        return self._blob

    @blob.setter
    def blob(self, blob: Dict[str, object]):
        """Sets the blob of this CustomMeta.


        :param blob: The blob of this CustomMeta.
        :type blob: Dict[str, object]
        """
        if blob is None:
            raise ValueError("Invalid value for `blob`, must not be `None`")  # noqa: E501

        self._blob = blob

    @property
    def instruction(self) -> str:
        """Gets the instruction of this CustomMeta.


        :return: The instruction of this CustomMeta.
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction: str):
        """Sets the instruction of this CustomMeta.


        :param instruction: The instruction of this CustomMeta.
        :type instruction: str
        """

        self._instruction = instruction

class Meta(XummResource):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
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
        cls.opened_by_deeplink = kwargs['opened_by_deeplink']
        cls.return_url_app = kwargs['return_url_app']
        cls.return_url_web = kwargs['return_url_web']
        cls.is_xapp = kwargs['is_xapp']

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
        if issubclass(Meta, dict):
            for key, value in cls.items():
                result[key] = value

        return result

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
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
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
        if issubclass(Result, dict):
            for key, value in cls.items():
                result[key] = value

        return result

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
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
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
        print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._result = Result(**kwargs['result'])
        cls._meta = Meta(**kwargs['meta'])
        cls._custom_meta = CustomMeta(**kwargs['custom_meta'])

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
        if issubclass(DeletePayloadResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return result

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
