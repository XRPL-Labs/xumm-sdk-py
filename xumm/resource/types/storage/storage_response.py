#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource
import six

class StorageResponse(XummResource):

    required = {
        'name': True,
        'uuidv4': True
    }

    model_types = {
        'name': str,
        'uuidv4': str
    }

    attribute_map = {
        'name': 'name',
        'uuidv4': 'uuidv4'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The StorageResponse of this StorageResponse.  # noqa: E501
        :rtype: StorageResponse
        """
        cls.sanity_check(kwargs)
        cls._name = None
        cls._uuidv4 = None
        cls.name = kwargs['name']
        cls.uuidv4 = kwargs['uuidv4']
    
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
        if issubclass(StorageResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def name(cls) -> str:
        """Gets the name of this StorageResponse.


        :return: The name of this StorageResponse.
        :rtype: str
        """
        return cls._name

    @name.setter
    def name(cls, name: str):
        """Sets the name of this StorageResponse.


        :param name: The name of this StorageResponse.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        cls._name = name

    @property
    def uuidv4(cls) -> str:
        """Gets the uuidv4 of this StorageResponse.


        :return: The uuidv4 of this StorageResponse.
        :rtype: str
        """
        return cls._uuidv4

    @uuidv4.setter
    def uuidv4(cls, uuidv4: str):
        """Sets the uuidv4 of this StorageResponse.


        :param uuidv4: The uuidv4 of this StorageResponse.
        :type uuidv4: str
        """
        if uuidv4 is None:
            raise ValueError("Invalid value for `uuidv4`, must not be `None`")  # noqa: E501

        cls._uuidv4 = uuidv4