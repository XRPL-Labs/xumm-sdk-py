#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource
import six
from typing import Union, List, Dict, Callable, Any  # noqa: F401

from .storage_response import StorageResponse

class StorageSetResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'application': 'StorageResponse',
        'stored': 'bool',
        'data': '(str, object)',
    }

    attribute_map = {
        'application': 'application',
        'stored': 'stored',
        'data': 'data',
    }
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The StorageSetResponse of this StorageSetResponse.  # noqa: E501
        :rtype: StorageSetResponse
        """
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._application = None
        cls._stored = None
        cls._data = None
        cls._application = StorageResponse(**kwargs['application'])
        cls._stored = kwargs['stored']
        cls._data = kwargs['data']

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
        if issubclass(StorageSetResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def application(self) -> StorageResponse:
        """Gets the application of this StorageSetResponse.


        :return: The application of this StorageSetResponse.
        :rtype: StorageResponse
        """
        return self._application

    @application.setter
    def application(self, application: StorageResponse):
        """Sets the application of this StorageSetResponse.


        :param application: The application of this StorageSetResponse.
        :type application: StorageResponse
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        self._application = application

    @property
    def stored(self) -> bool:
        """Gets the stored of this StorageSetResponse.


        :return: The stored of this StorageSetResponse.
        :rtype: bool
        """
        return self._stored

    @stored.setter
    def stored(self, stored: bool):
        """Sets the stored of this StorageSetResponse.


        :param stored: The stored of this StorageSetResponse.
        :type stored: bool
        """
        if stored is None:
            raise ValueError("Invalid value for `stored`, must not be `None`")  # noqa: E501

        self._stored = stored

    @property
    def data(self) -> Dict[str, object]:
        """Gets the data of this StorageSetResponse.


        :return: The data of this StorageSetResponse.
        :rtype: Dict[str, object]
        """
        return self._data

    @data.setter
    def data(self, data: Dict[str, object]):
        """Sets the data of this StorageSetResponse.


        :param data: The data of this StorageSetResponse.
        :type data: Dict[str, object]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data