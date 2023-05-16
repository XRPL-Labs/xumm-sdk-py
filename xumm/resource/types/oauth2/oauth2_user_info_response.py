#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class OAuth2UserInfoResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'sub': True,
        'email': True,
        'picture': True,
        'account': True,
        'name': True,
        'domain': True,
        'blocked': True,
        'source': True,
        'force_dtag': True,
        'kyc_approved': True,
        'pro_subscription': True,
        'network_type': True,
        'network_endpoint': True,
    }

    model_types = {
        'sub': str,
        'email': str,
        'picture': str,
        'account': str,
        'name': str,
        'domain': str,
        'blocked': bool,
        'source': str,
        'force_dtag': bool,
        'kyc_approved': bool,
        'pro_subscription': bool,
        'network_type': str,
        'network_endpoint': str,
    }

    attribute_map = {
        'sub': 'sub',
        'email': 'email',
        'picture': 'picture',
        'account': 'account',
        'name': 'name',
        'domain': 'domain',
        'blocked': 'blocked',
        'source': 'source',
        'force_dtag': 'force_dtag',
        'kyc_approved': 'kycApproved',
        'pro_subscription': 'proSubscription',
        'network_type': 'networkType',
        'network_endpoint': 'networkEndpoint',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XappUserAccountInfo of this XappUserAccountInfo.  # noqa: E501
        :rtype: XappUserAccountInfo
        """
        cls.sanity_check(kwargs)
        cls._sub = None
        cls._email = None
        cls._picture = None
        cls._account = None
        cls._name = None
        cls._domain = None
        cls._blocked = None
        cls._source = None
        cls._force_dtag = None
        cls._kyc_approved = None
        cls._pro_subscription = None
        cls._network_type = None
        cls._network_endpoint = None
        cls.sub = kwargs['sub']
        cls.email = kwargs['email']
        cls.picture = kwargs['picture']
        cls.account = kwargs['account']
        cls.name = kwargs['name']
        cls.domain = kwargs['domain']
        cls.blocked = kwargs['blocked']
        cls.source = kwargs['source']
        cls.force_dtag = kwargs['force_dtag']
        cls.kyc_approved = kwargs['kycApproved']
        cls.pro_subscription = kwargs['proSubscription']
        cls.network_type = kwargs['networkType']
        cls.network_endpoint = kwargs['networkEndpoint']

    @property
    def sub(self) -> str:
        """Gets the sub of this XappUserAccountInfo.


        :return: The sub of this XappUserAccountInfo.
        :rtype: str
        """
        return self._sub

    @sub.setter
    def sub(self, sub: str):
        """Sets the sub of this XappUserAccountInfo.


        :param sub: The sub of this XappUserAccountInfo.
        :type sub: str
        """
        self._sub = sub

    @property
    def email(self) -> str:
        """Gets the email of this XappUserAccountInfo.


        :return: The email of this XappUserAccountInfo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this XappUserAccountInfo.


        :param email: The email of this XappUserAccountInfo.
        :type email: str
        """
        self._email = email

    @property
    def picture(self) -> str:
        """Gets the picture of this XappUserAccountInfo.


        :return: The picture of this XappUserAccountInfo.
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture: str):
        """Sets the picture of this XappUserAccountInfo.


        :param picture: The picture of this XappUserAccountInfo.
        :type picture: str
        """
        self._picture = picture

    @property
    def account(self) -> str:
        """Gets the account of this XappUserAccountInfo.


        :return: The account of this XappUserAccountInfo.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account: str):
        """Sets the account of this XappUserAccountInfo.


        :param account: The account of this XappUserAccountInfo.
        :type account: str
        """
        self._account = account

    @property
    def name(self) -> str:
        """Gets the name of this XappUserAccountInfo.


        :return: The name of this XappUserAccountInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this XappUserAccountInfo.


        :param name: The name of this XappUserAccountInfo.
        :type name: str
        """
        self._name = name

    @property
    def domain(self) -> str:
        """Gets the domain of this XappUserAccountInfo.


        :return: The domain of this XappUserAccountInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain: str):
        """Sets the domain of this XappUserAccountInfo.


        :param domain: The domain of this XappUserAccountInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def blocked(self) -> bool:
        """Gets the blocked of this XappUserAccountInfo.


        :return: The blocked of this XappUserAccountInfo.
        :rtype: bool
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked: bool):
        """Sets the blocked of this XappUserAccountInfo.


        :param blocked: The blocked of this XappUserAccountInfo.
        :type blocked: bool
        """
        self._blocked = blocked

    @property
    def source(self) -> str:
        """Gets the source of this XappUserAccountInfo.


        :return: The source of this XappUserAccountInfo.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str):
        """Sets the source of this XappUserAccountInfo.


        :param source: The source of this XappUserAccountInfo.
        :type source: str
        """
        self._source = source

    @property
    def force_dtag(self) -> bool:
        """Gets the force_dtag of this XappUserAccountInfo.


        :return: The force_dtag of this XappUserAccountInfo.
        :rtype: bool
        """
        return self._force_dtag

    @force_dtag.setter
    def force_dtag(self, force_dtag: bool):
        """Sets the force_dtag of this XappUserAccountInfo.


        :param force_dtag: The force_dtag of this XappUserAccountInfo.
        :type force_dtag: bool
        """
        self._force_dtag = force_dtag

    @property
    def kyc_approved(self) -> bool:
        """Gets the kyc_approved of this XappUserAccountInfo.


        :return: The kyc_approved of this XappUserAccountInfo.
        :rtype: bool
        """
        return self._kyc_approved

    @kyc_approved.setter
    def kyc_approved(self, kyc_approved: bool):
        """Sets the kyc_approved of this XappUserAccountInfo.


        :param kyc_approved: The kyc_approved of this XappUserAccountInfo.
        :type kyc_approved: bool
        """
        self._kyc_approved = kyc_approved

    @property
    def pro_subscription(self) -> bool:
        """Gets the pro_subscription of this XappUserAccountInfo.


        :return: The pro_subscription of this XappUserAccountInfo.
        :rtype: bool
        """
        return self._pro_subscription

    @pro_subscription.setter
    def pro_subscription(self, pro_subscription: bool):
        """Sets the pro_subscription of this XappUserAccountInfo.


        :param pro_subscription: The pro_subscription of this XappUserAccountInfo.  # noqa: E501
        :type pro_subscription: bool
        """
        self._pro_subscription = pro_subscription

    @property
    def network_type(self) -> str:
        """Gets the network_type of this XappUserAccountInfo.


        :return: The network_type of this XappUserAccountInfo.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type: str):
        """Sets the network_type of this XappUserAccountInfo.


        :param network_type: The network_type of this XappUserAccountInfo.  # noqa: E501
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def network_endpoint(self) -> str:
        """Gets the network_endpoint of this XappUserAccountInfo.


        :return: The network_endpoint of this XappUserAccountInfo.
        :rtype: str
        """
        return self._network_endpoint

    @network_endpoint.setter
    def network_endpoint(self, network_endpoint: str):
        """Sets the network_endpoint of this XappUserAccountInfo.


        :param network_endpoint: The network_endpoint of this XappUserAccountInfo.  # noqa: E501
        :type network_endpoint: str
        """
        self._network_endpoint = network_endpoint
