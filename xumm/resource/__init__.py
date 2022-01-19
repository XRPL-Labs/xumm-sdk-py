from __future__ import unicode_literals
from xumm import client

import pprint

import six

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

        for attr, is_type in six.iteritems(cls.model_types):
            if attr not in kwargs and attr in cls.required:
                raise ValueError("Invalid value for `{}`, must not be `None`".format(attr))

            if attr not in kwargs and attr in cls.nullable:
                continue
            
            value = kwargs[attr]

            if attr in cls.nullable and value == {} or value == None:
                continue
                

            # validate type if required
            if not isinstance(value, is_type):
                raise ValueError("Invalid value for `{}`, must be a `{}`".format(attr, is_type))

            if attr in cls.required and value is None:
                raise ValueError("Invalid value for `{}`, must not be `None`".format(attr))

    # def from_dict(self):
    #     """Returns the model properties as a dict

    #     :rtype: dict
    #     """
    #     return self.from_dict()

    def to_dict(self):
        """Returns the model properties as a dict

        :rtype: dict
        """
        return self.to_dict()

    def to_str(self):
        """Returns the string representation of the model

        :rtype: str
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


class XummResource(PrintableResource):

    @classmethod
    def platform_url(cls):
        return client.build_url() + 'platform' + '/'

    def __init__(cls, **kwargs):
        cls.refresh_from(**kwargs)

    def refresh_from(cls, **kwargs):
        raise NotImplementedError
