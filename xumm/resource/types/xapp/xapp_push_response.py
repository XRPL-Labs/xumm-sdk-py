#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class XappPushResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'pushed': True,
    }

    model_types = {
        'pushed': bool,
    }

    attribute_map = {
        'pushed': 'pushed',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XappPushResponse of this XappPushResponse.  # noqa: E501
        :rtype: XappPushResponse
        """
        cls.sanity_check(kwargs)
        cls._pushed = None
        cls.pushed = kwargs['pushed']

    @property
    def pushed(self) -> bool:
        """Gets the pushed of this XappPushResponse.


        :return: The pushed of this XappPushResponse.
        :rtype: bool
        """
        return self._pushed

    @pushed.setter
    def pushed(self, pushed: bool):
        """Sets the pushed of this XappPushResponse.


        :param pushed: The pushed of this XappPushResponse.
        :type pushed: bool
        """
        self._pushed = pushed
