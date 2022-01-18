from xumm.resource import XummResource
import six
from typing import Union, List, Dict, Callable, Any  # noqa: F401


class KycStatusResponse(XummResource):

    model_types = {
        'kyc_status': 'str',
        'possible_statuses': 'dict(str, object)'
    }

    attribute_map = {
        'kyc_status': 'kycStatus',
        'possible_statuses': 'possibleStatuses'
    }
        

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The KycStatusResponse of this KycStatusResponse.  # noqa: E501
        :rtype: KycStatusResponse
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
        if issubclass(KycStatusResponse, dict):
            for key, value in cls.items():
                result[key] = value

        return {k: v for k, v in result.items() if v is not None}

    @property
    def kyc_status(cls) -> str:
        """Gets the kyc_status of this KycStatusResponse.


        :return: The kyc_status of this KycStatusResponse.
        :rtype: str
        """
        return cls._kyc_status

    @kyc_status.setter
    def kyc_status(cls, kyc_status: str):
        """Sets the kyc_status of this KycStatusResponse.


        :param kyc_status: The kyc_status of this KycStatusResponse.
        :type kyc_status: str
        """
        if kyc_status is None:
            raise ValueError("Invalid value for `kyc_status`, must not be `None`")  # noqa: E501

        cls._kyc_status = kyc_status

    @property
    def possible_statuses(cls) -> Dict[str, object]:
        """Gets the possible_statuses of this KycStatusResponse.


        :return: The possible_statuses of this KycStatusResponse.
        :rtype: bool
        """
        return cls._possible_statuses

    @possible_statuses.setter
    def possible_statuses(cls, possible_statuses: Dict[str, object]):
        """Sets the possible_statuses of this KycStatusResponse.


        :param possible_statuses: The possible_statuses of this KycStatusResponse.
        :type possible_statuses: bool
        """
        if possible_statuses is None:
            raise ValueError("Invalid value for `possible_statuses`, must not be `None`")  # noqa: E501

        cls._possible_statuses = possible_statuses