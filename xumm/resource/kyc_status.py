import os
from xumm.resource import XummResource
import six

class KYCStatusResponse(XummResource):

    swagger_types = {
        'account': 'str',
        'kyc_approved': 'bool'
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
        cls._account = kwargs['account']
        cls._kyc_approved = kwargs['kycApproved']

    def to_dict(cls):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(cls.swagger_types):
            value = getattr(cls, attr)
            if isinstance(value, list):
                result[to_camel_case(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[to_camel_case(attr)] = value.to_dict()
            elif isinstance(value, dict):
                result[to_camel_case(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[to_camel_case(attr)] = value
        if issubclass(KYCStatusResponse, dict):
            for key, value in cls.items():
                result[to_camel_case(key)] = value

        return result

    @property
    def account(self) -> str:
        """Gets the account of this KYCStatusResponse.


        :return: The account of this KYCStatusResponse.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account: str):
        """Sets the account of this KYCStatusResponse.


        :param account: The account of this KYCStatusResponse.
        :type account: str
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def kyc_approved(self) -> bool:
        """Gets the kyc_approved of this KYCStatusResponse.


        :return: The kyc_approved of this KYCStatusResponse.
        :rtype: bool
        """
        return self._kyc_approved

    @kyc_approved.setter
    def kyc_approved(self, kyc_approved: bool):
        """Sets the kyc_approved of this KYCStatusResponse.


        :param kyc_approved: The kyc_approved of this KYCStatusResponse.
        :type kyc_approved: bool
        """
        if kyc_approved is None:
            raise ValueError("Invalid value for `kyc_approved`, must not be `None`")  # noqa: E501

        self._kyc_approved = kyc_approved