import os
from xumm.resource import XummResource
import six
import json

from typing import List, Dict  # noqa: F401


class StorageApplication(XummResource):

    model_types = {
        'name': 'str',
        'uuidv4': 'str'
    }

    attribute_map = {
        'name': 'name',
        'uuidv4': 'uuidv4'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The StorageApplication of this StorageApplication.  # noqa: E501
        :rtype: StorageApplication
        """
        cls._name = None
        cls._uuidv4 = None

        cls._name = kwargs['name']
        cls._uuidv4 = kwargs['uuidv4']
    
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
        if issubclass(StorageApplication, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def name(cls) -> str:
        """Gets the name of this StorageApplication.


        :return: The name of this StorageApplication.
        :rtype: str
        """
        return cls._name

    @name.setter
    def name(cls, name: str):
        """Sets the name of this StorageApplication.


        :param name: The name of this StorageApplication.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        cls._name = name

    @property
    def uuidv4(cls) -> str:
        """Gets the uuidv4 of this StorageApplication.


        :return: The uuidv4 of this StorageApplication.
        :rtype: str
        """
        return cls._uuidv4

    @uuidv4.setter
    def uuidv4(cls, uuidv4: str):
        """Sets the uuidv4 of this StorageApplication.


        :param uuidv4: The uuidv4 of this StorageApplication.
        :type uuidv4: str
        """
        if uuidv4 is None:
            raise ValueError("Invalid value for `uuidv4`, must not be `None`")  # noqa: E501

        cls._uuidv4 = uuidv4

class SetStorageResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'application': 'StorageApplication',
        'stored': 'bool',
        'data': '(str, object)',
    }

    attribute_map = {
        'application': 'application',
        'stored': 'stored',
        'data': 'data',
    }

    @classmethod
    def post_url(cls):
        """post_url."""
        return super(SetStorageResponse, cls).platform_url() + 'storage' + '/'
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The SetStorageResponse of this SetStorageResponse.  # noqa: E501
        :rtype: SetStorageResponse
        """
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._application = None
        cls._stored = None
        cls._data = None
        cls._application = StorageApplication(**kwargs['application'])
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
        if issubclass(SetStorageResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def application(self) -> StorageApplication:
        """Gets the application of this SetStorageResponse.


        :return: The application of this SetStorageResponse.
        :rtype: StorageApplication
        """
        return self._application

    @application.setter
    def application(self, application: StorageApplication):
        """Sets the application of this SetStorageResponse.


        :param application: The application of this SetStorageResponse.
        :type application: StorageApplication
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        self._application = application

    @property
    def stored(self) -> bool:
        """Gets the stored of this SetStorageResponse.


        :return: The stored of this SetStorageResponse.
        :rtype: bool
        """
        return self._stored

    @stored.setter
    def stored(self, stored: bool):
        """Sets the stored of this SetStorageResponse.


        :param stored: The stored of this SetStorageResponse.
        :type stored: bool
        """
        if stored is None:
            raise ValueError("Invalid value for `stored`, must not be `None`")  # noqa: E501

        self._stored = stored

    @property
    def data(self) -> Dict[str, object]:
        """Gets the data of this SetStorageResponse.


        :return: The data of this SetStorageResponse.
        :rtype: Dict[str, object]
        """
        return self._data

    @data.setter
    def data(self, data: Dict[str, object]):
        """Sets the data of this SetStorageResponse.


        :param data: The data of this SetStorageResponse.
        :type data: Dict[str, object]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

class GetStorageResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'application': 'StorageApplication',
        'data': '(str, object)',
    }

    attribute_map = {
        'application': 'application',
        'data': 'data',
    }

    @classmethod
    def get_url(cls):
        """get_url."""
        return super(GetStorageResponse, cls).platform_url() + 'storage' + '/'
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The GetStorageResponse of this GetStorageResponse.  # noqa: E501
        :rtype: GetStorageResponse
        """
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._application = None
        cls._data = None
        cls._application = StorageApplication(**kwargs['application'])
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
        if issubclass(GetStorageResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def application(self) -> StorageApplication:
        """Gets the application of this GetStorageResponse.


        :return: The application of this GetStorageResponse.
        :rtype: StorageApplication
        """
        return self._application

    @application.setter
    def application(self, application: StorageApplication):
        """Sets the application of this GetStorageResponse.


        :param application: The application of this GetStorageResponse.
        :type application: StorageApplication
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        self._application = application

    @property
    def data(self) -> Dict[str, object]:
        """Gets the data of this GetStorageResponse.


        :return: The data of this GetStorageResponse.
        :rtype: Dict[str, object]
        """
        return self._data

    @data.setter
    def data(self, data: Dict[str, object]):
        """Sets the data of this GetStorageResponse.


        :param data: The data of this GetStorageResponse.
        :type data: Dict[str, object]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data


class DeleteStorageResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'application': 'StorageApplication',
        'stored': 'bool',
        'data': '(str, object)',
    }

    attribute_map = {
        'application': 'application',
        'stored': 'stored',
        'data': 'data',
    }

    @classmethod
    def delete_url(cls):
        """delete_url."""
        return super(DeleteStorageResponse, cls).platform_url() + 'storage' + '/'
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The DeleteStorageResponse of this DeleteStorageResponse.  # noqa: E501
        :rtype: DeleteStorageResponse
        """
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._application = None
        cls._stored = None
        cls._data = None
        cls._application = StorageApplication(**kwargs['application'])
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
        if issubclass(DeleteStorageResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return result
        # return {k: v for k, v in result.items() if v is not None}

    @property
    def application(self) -> StorageApplication:
        """Gets the application of this DeleteStorageResponse.


        :return: The application of this DeleteStorageResponse.
        :rtype: StorageApplication
        """
        return self._application

    @application.setter
    def application(self, application: StorageApplication):
        """Sets the application of this DeleteStorageResponse.


        :param application: The application of this DeleteStorageResponse.
        :type application: StorageApplication
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        self._application = application

    @property
    def stored(self) -> bool:
        """Gets the stored of this DeleteStorageResponse.


        :return: The stored of this DeleteStorageResponse.
        :rtype: bool
        """
        return self._stored

    @stored.setter
    def stored(self, stored: bool):
        """Sets the stored of this DeleteStorageResponse.


        :param stored: The stored of this DeleteStorageResponse.
        :type stored: bool
        """
        if stored is None:
            raise ValueError("Invalid value for `stored`, must not be `None`")  # noqa: E501

        self._stored = stored

    @property
    def data(self) -> Dict[str, object]:
        """Gets the data of this DeleteStorageResponse.


        :return: The data of this DeleteStorageResponse.
        :rtype: Dict[str, object]
        """
        return self._data

    @data.setter
    def data(self, data: Dict[str, object]):
        """Sets the data of this DeleteStorageResponse.


        :param data: The data of this DeleteStorageResponse.
        :type data: Dict[str, object]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data