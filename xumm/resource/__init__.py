#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

from typing import Union, List, Dict, Callable, Any  # noqa: F401
import pprint
import six

from xumm import client


class PrintableResource(object):

    # nullable: The key is attribute name and the
    # value is a bool.
    nullable = {}

    # required: The key is attribute name and the
    # value is a bool.
    required = {}

    # modelTypes: The key is attribute name and the
    # value is attribute type.
    model_types = {}

    # attributeMap: The key is attribute name and the
    # value is json key in definition.
    attribute_map = {}

    def sanity_check(cls, kwargs):
        """Runs a sanity check on the model"""

        for _attr, is_type in six.iteritems(cls.model_types):

            # Use the attribute map for RECEIVING json data (Camelcase)
            attr = cls.attribute_map[_attr]

            # Error if attribute not in json
            # and attribute in required
            # * 'not in' isnt correct as False may get tripped here...
            if attr not in kwargs and attr in cls.required:
                raise ValueError(
                    "Invalid value for `{}`, "
                    "must not be `None`".format(attr)
                )

            # Skip option attributes if non exists in json
            if attr not in kwargs and attr not in cls.required:
                continue

            # set value for attribute
            value = kwargs[attr]

            # Skip nullable attributes
            # if empty json, list or None
            if attr in cls.nullable and value == {} or value == [] or value is None or value == '':  # noqa: E501
                continue

            # Error if value is not instance of attribute type
            if not isinstance(value, is_type):
                raise ValueError(
                    "Invalid value for `{}`, "
                    "must be a `{}`".format(attr, is_type)
                )

            # Error if attribute is required and value is
            # None: 2x of ^^^ Delete in final
            if attr in cls.required and value is None:
                raise ValueError(
                    "Invalid value for `{}`, "
                    "must not be `None`".format(attr)
                )

    # def from_dict(self):
    #     """Returns the model properties as a dict

    #     :rtype: dict
    #     """
    #     return self.from_dict()

    def to_dict(self) -> Dict[str, object]:
        """Returns the model properties as a dict

        :rtype: dict
        """
        return self.to_dict()

    def to_str(self) -> str:
        """Returns the string representation of the model

        :rtype: str
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other) -> bool:
        """Returns true if both objects are equal"""
        return self.__dict__ == other.__dict__

    def __ne__(self, other) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other


class XummResource(PrintableResource):

    @classmethod
    def platform_url(cls) -> str:
        return client.build_url() + 'platform' + '/'

    def __init__(cls, *args, **kwargs) -> 'XummResource':
        cls.refresh_from(**kwargs)

    def refresh_from(cls, **kwargs):
        raise NotImplementedError
