import os
from xumm.resource import XummResource
import six
import json

from typing import List, Dict  # noqa: F401

class GetKycResponse(XummResource):

    model_types = {
        'account': 'str',
        'kyc_approved': 'bool'
    }

    attribute_map = {
        'account': 'account',
        'kyc_approved': 'kycApproved'
    }

    @classmethod
    def get_url(cls, id):
        """get_url."""
        return super(GetKycResponse, cls).platform_url() + 'kyc-status/' + id
        
    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The GetKycResponse of this GetKycResponse.  # noqa: E501
        :rtype: GetKycResponse
        """
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._account = None
        cls._kyc_approved = None
        cls._account = kwargs['account']
        cls._kyc_approved = kwargs['kycApproved']

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
        if issubclass(GetKycResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def account(cls) -> str:
        """Gets the account of this GetKycResponse.


        :return: The account of this GetKycResponse.
        :rtype: str
        """
        return cls._account

    @account.setter
    def account(cls, account: str):
        """Sets the account of this GetKycResponse.


        :param account: The account of this GetKycResponse.
        :type account: str
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        cls._account = account

    @property
    def kyc_approved(cls) -> bool:
        """Gets the kyc_approved of this GetKycResponse.


        :return: The kyc_approved of this GetKycResponse.
        :rtype: bool
        """
        return cls._kyc_approved

    @kyc_approved.setter
    def kyc_approved(cls, kyc_approved: bool):
        """Sets the kyc_approved of this GetKycResponse.


        :param kyc_approved: The kyc_approved of this GetKycResponse.
        :type kyc_approved: bool
        """
        if kyc_approved is None:
            raise ValueError("Invalid value for `kyc_approved`, must not be `None`")  # noqa: E501

        cls._kyc_approved = kyc_approved

class PostKycResponse(XummResource):

    model_types = {
        'kyc_status': 'str',
        'possible_statuses': 'dict(str, object)'
    }

    attribute_map = {
        'kyc_status': 'kycStatus',
        'possible_statuses': 'possibleStatuses'
    }

    @classmethod
    def post_url(cls):
        """post_url."""
        return super(PostKycResponse, cls).platform_url() + 'kyc-status/'
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The PostKycResponse of this PostKycResponse.  # noqa: E501
        :rtype: PostKycResponse
        """
        # print(json.dumps(kwargs, indent=4, sort_keys=True))
        cls._kyc_status = None
        cls._possible_statuses = None
        cls._kyc_status = kwargs['kycStatus']
        cls._possible_statuses = kwargs['possibleStatuses']

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
        if issubclass(PostKycResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def kyc_status(cls) -> str:
        """Gets the kyc_status of this PostKycResponse.


        :return: The kyc_status of this PostKycResponse.
        :rtype: str
        """
        return cls._kyc_status

    @kyc_status.setter
    def kyc_status(cls, kyc_status: str):
        """Sets the kyc_status of this PostKycResponse.


        :param kyc_status: The kyc_status of this PostKycResponse.
        :type kyc_status: str
        """
        if kyc_status is None:
            raise ValueError("Invalid value for `kyc_status`, must not be `None`")  # noqa: E501

        cls._kyc_status = kyc_status

    @property
    def possible_statuses(cls) -> Dict[str, object]:
        """Gets the possible_statuses of this PostKycResponse.


        :return: The possible_statuses of this PostKycResponse.
        :rtype: bool
        """
        return cls._possible_statuses

    @possible_statuses.setter
    def possible_statuses(cls, possible_statuses: Dict[str, object]):
        """Sets the possible_statuses of this PostKycResponse.


        :param possible_statuses: The possible_statuses of this PostKycResponse.
        :type possible_statuses: bool
        """
        if possible_statuses is None:
            raise ValueError("Invalid value for `possible_statuses`, must not be `None`")  # noqa: E501

        cls._possible_statuses = possible_statuses