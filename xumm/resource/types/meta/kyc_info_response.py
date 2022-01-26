#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class KycInfoResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'account': True,
        'kyc_approved': True,
    }

    model_types = {
        'account': str,
        'kyc_approved': bool
    }

    attribute_map = {
        'account': 'account',
        'kyc_approved': 'kycApproved'
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The KycInfoResponse of this KycInfoResponse.  # noqa: E501
        :rtype: KycInfoResponse
        """
        cls.sanity_check(kwargs)
        cls._account = None
        cls._kyc_approved = None
        cls.account = kwargs['account']
        cls.kyc_approved = kwargs['kycApproved']

    @property
    def account(cls) -> str:
        """Gets the account of this KycInfoResponse.


        :return: The account of this KycInfoResponse.
        :rtype: str
        """
        return cls._account

    @account.setter
    def account(cls, account: str):
        """Sets the account of this KycInfoResponse.


        :param account: The account of this KycInfoResponse.
        :type account: str
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        cls._account = account

    @property
    def kyc_approved(cls) -> bool:
        """Gets the kyc_approved of this KycInfoResponse.


        :return: The kyc_approved of this KycInfoResponse.
        :rtype: bool
        """
        return cls._kyc_approved

    @kyc_approved.setter
    def kyc_approved(cls, kyc_approved: bool):
        """Sets the kyc_approved of this KycInfoResponse.


        :param kyc_approved: The kyc_approved of this KycInfoResponse.
        :type kyc_approved: bool
        """
        if kyc_approved is None:
            raise ValueError("Invalid value for `kyc_approved`, must not be `None`")  # noqa: E501

        cls._kyc_approved = kyc_approved
