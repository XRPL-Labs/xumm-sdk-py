#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class XappEventResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'pushed': True,
        'uuid': True,
    }

    model_types = {
        'pushed': bool,
        'uuid': str,
    }

    attribute_map = {
        'pushed': 'pushed',
        'uuid': 'uuid',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XappEventResponse of this XappEventResponse.  # noqa: E501
        :rtype: XappEventResponse
        """
        cls.sanity_check(kwargs)
        cls._pushed = None
        cls._uuid = None
        cls.pushed = kwargs['pushed']
        cls.uuid = kwargs['uuid']

    @property
    def pushed(self) -> bool:
        """Gets the pushed of this XappEventResponse.


        :return: The pushed of this XappEventResponse.
        :rtype: bool
        """
        return self._pushed

    @pushed.setter
    def pushed(self, pushed: bool):
        """Sets the pushed of this XappEventResponse.


        :param pushed: The pushed of this XappEventResponse.
        :type pushed: bool
        """
        self._pushed = pushed

    @property
    def uuid(self) -> str:
        """Gets the uuid of this XappEventResponse.


        :return: The uuid of this XappEventResponse.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this XappEventResponse.


        :param uuid: The uuid of this XappEventResponse.
        :type uuid: str
        """
        self._uuid = uuid
