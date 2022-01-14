import os
from xumm.resource import XummResource
import six
import json

class KYCStatusResponse(XummResource):

    model_types = {
        'account': 'str',
        'kyc_approved': 'bool'
    }

    attribute_map = {
        'account': 'account',
        'kyc_approved': 'kycApproved'
    }

    @classmethod
    def get_url(cls):
        """get_url."""
        return super(KYCStatusResponse, cls).platform_url() + 'kyc_status' + '/'
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The KYCStatusResponse of this KYCStatusResponse.  # noqa: E501
        :rtype: KYCStatusResponse
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
        if issubclass(KYCStatusResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def account(cls) -> str:
        """Gets the account of this KYCStatusResponse.


        :return: The account of this KYCStatusResponse.
        :rtype: str
        """
        return cls._account

    @account.setter
    def account(cls, account: str):
        """Sets the account of this KYCStatusResponse.


        :param account: The account of this KYCStatusResponse.
        :type account: str
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        cls._account = account

    @property
    def kyc_approved(cls) -> bool:
        """Gets the kyc_approved of this KYCStatusResponse.


        :return: The kyc_approved of this KYCStatusResponse.
        :rtype: bool
        """
        return cls._kyc_approved

    @kyc_approved.setter
    def kyc_approved(cls, kyc_approved: bool):
        """Sets the kyc_approved of this KYCStatusResponse.


        :param kyc_approved: The kyc_approved of this KYCStatusResponse.
        :type kyc_approved: bool
        """
        if kyc_approved is None:
            raise ValueError("Invalid value for `kyc_approved`, must not be `None`")  # noqa: E501

        cls._kyc_approved = kyc_approved