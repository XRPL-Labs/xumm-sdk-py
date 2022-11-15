#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class XappUserAccountInfo(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'account': True,
        'name': True,
        'domain': True,
        'blocked': True,
        'source': True,
        'kyc_approved': True,
        'pro_subscription': True,
    }

    model_types = {
        'account': str,
        'name': str,
        'domain': str,
        'blocked': bool,
        'source': str,
        'kyc_approved': bool,
        'pro_subscription': bool,
    }

    attribute_map = {
        'account': 'account',
        'name': 'name',
        'domain': 'domain',
        'blocked': 'blocked',
        'source': 'source',
        'kyc_approved': 'kycApproved',
        'pro_subscription': 'proSubscription',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XappUserAccountInfo of this XappUserAccountInfo.  # noqa: E501
        :rtype: XappUserAccountInfo
        """
        cls.sanity_check(kwargs)
        cls._account = None
        cls._name = None
        cls._domain = None
        cls._blocked = None
        cls._source = None
        cls._kyc_approved = None
        cls._pro_subscription = None
        cls.account = kwargs['account']
        cls.name = kwargs['name']
        cls.domain = kwargs['domain']
        cls.blocked = kwargs['blocked']
        cls.source = kwargs['source']
        cls.kyc_approved = kwargs['kycApproved']
        cls.pro_subscription = kwargs['proSubscription']

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
    def blocked(self) -> str:
        """Gets the blocked of this XappUserAccountInfo.


        :return: The blocked of this XappUserAccountInfo.
        :rtype: str
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked: str):
        """Sets the blocked of this XappUserAccountInfo.


        :param blocked: The blocked of this XappUserAccountInfo.
        :type blocked: str
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
    def kyc_approved(self) -> str:
        """Gets the kyc_approved of this XappUserAccountInfo.


        :return: The kyc_approved of this XappUserAccountInfo.
        :rtype: str
        """
        return self._kyc_approved

    @kyc_approved.setter
    def kyc_approved(self, kyc_approved: str):
        """Sets the kyc_approved of this XappUserAccountInfo.


        :param kyc_approved: The kyc_approved of this XappUserAccountInfo.
        :type kyc_approved: str
        """
        self._kyc_approved = kyc_approved

    @property
    def pro_subscription(self) -> str:
        """Gets the pro_subscription of this XappUserAccountInfo.


        :return: The pro_subscription of this XappUserAccountInfo.
        :rtype: str
        """
        return self._pro_subscription

    @pro_subscription.setter
    def pro_subscription(self, pro_subscription: str):
        """Sets the pro_subscription of this XappUserAccountInfo.


        :param pro_subscription: The pro_subscription of this XappUserAccountInfo.  # noqa: E501
        :type pro_subscription: str
        """
        self._pro_subscription = pro_subscription


class XappUserDevice(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'currency': True,
    }

    model_types = {
        'currency': str,
    }

    attribute_map = {
        'currency': 'currency',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XappUserDevice of this XappUserDevice.  # noqa: E501
        :rtype: XappUserDevice
        """
        cls.sanity_check(kwargs)
        cls._currency = None
        cls.currency = kwargs['currency']

    @property
    def currency(self) -> str:
        """Gets the currency of this XappUserDevice.


        :return: The currency of this XappUserDevice.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        """Sets the currency of this XappUserDevice.


        :param currency: The currency of this XappUserDevice.
        :type currency: str
        """
        self._currency = currency


class XappOriginData(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'txid': True,
    }

    model_types = {
        'txid': str,
    }

    attribute_map = {
        'txid': 'txid',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XappOriginData of this XappOriginData.  # noqa: E501
        :rtype: XappOriginData
        """
        cls.sanity_check(kwargs)
        cls._txid = None
        cls.txid = kwargs['txid']

    @property
    def txid(self) -> str:
        """Gets the txid of this XappOriginData.


        :return: The txid of this XappOriginData.
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid: str):
        """Sets the txid of this XappOriginData.


        :param txid: The txid of this XappOriginData.
        :type txid: str
        """
        self._txid = txid


class XappOrigin(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'type': True,
        'data': True,
    }

    model_types = {
        'type': str,
        'data': dict,
    }

    attribute_map = {
        'type': 'type',
        'data': 'data',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XappOrigin of this XappOrigin.  # noqa: E501
        :rtype: XappOrigin
        """
        cls.sanity_check(kwargs)
        cls._type = None
        cls._data = None
        cls.type = kwargs['type']
        cls.data = XappOriginData(kwargs['data'])

    @property
    def type(self) -> str:
        """Gets the type of this XappOrigin.


        :return: The type of this XappOrigin.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this XappOrigin.


        :param type: The type of this XappOrigin.
        :type type: str
        """
        self._type = type

    @property
    def data(self) -> XappOriginData:
        """Gets the data of this XappOrigin.


        :return: The data of this XappOrigin.
        :rtype: XappOriginData
        """
        return self._data

    @data.setter
    def data(self, data: XappOriginData):
        """Sets the data of this XappOrigin.


        :param data: The data of this XappOrigin.
        :type data: XappOriginData
        """
        self._data = data


class XappOttResponse(XummResource):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    required = {
        'locale': True,
        'version': True,
        'account': True,
        'accountaccess': True,
        'accounttype': True,
        'style': True,
        # 'origin': True,
        # 'user': True,
        # 'user_device': True,
        # 'account_info': True,
    }

    model_types = {
        'locale': str,
        'version': str,
        'account': str,
        'accountaccess': str,
        'accounttype': str,
        'style': str,
        'origin': dict,
        'user': str,
        'user_device': dict,
        'account_info': dict,
    }

    attribute_map = {
        'locale': 'locale',
        'version': 'version',
        'account': 'account',
        'accountaccess': 'accountaccess',
        'accounttype': 'accounttype',
        'style': 'style',
        'origin': 'origin',
        'user': 'user',
        'user_device': 'user_device',
        'account_info': 'account_info',
    }

    def refresh_from(cls, **kwargs):
        """Returns the dict as a model

        :param kwargs: A dict.
        :type: dict
        :return: The XappOttResponse of this XappOttResponse.  # noqa: E501
        :rtype: XappOttResponse
        """
        cls.sanity_check(kwargs)
        cls._locale = None
        cls._version = None
        cls._account = None
        cls._accountaccess = None
        cls._accounttype = None
        cls._style = None
        cls._origin = None
        cls._user = None
        cls._user_device = None
        cls._account_info = None
        cls.locale = kwargs['locale']
        cls.version = kwargs['version']
        cls.account = kwargs['account']
        cls.accountaccess = kwargs['accountaccess']
        cls.accounttype = kwargs['accounttype']
        cls.style = kwargs['style']
        if 'origin' in kwargs:
            cls.origin = XappOrigin(kwargs['origin'])
        if 'user' in kwargs:
            cls.user = kwargs['user']
        if 'user_device' in kwargs:
            cls.user_device = XappUserDevice(kwargs['user_device'])
        if 'account_info' in kwargs:
            cls.account_info = XappUserAccountInfo(**kwargs['application'])

    @property
    def locale(self) -> str:
        """Gets the locale of this XappOttResponse.


        :return: The locale of this XappOttResponse.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale: str):
        """Sets the locale of this XappOttResponse.


        :param locale: The locale of this XappOttResponse.
        :type locale: str
        """

        self._locale = locale

    @property
    def version(self) -> str:
        """Gets the version of this XappOttResponse.


        :return: The version of this XappOttResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this XappOttResponse.


        :param version: The version of this XappOttResponse.
        :type version: str
        """

        self._version = version

    @property
    def account(self) -> str:
        """Gets the account of this XappOttResponse.


        :return: The account of this XappOttResponse.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account: str):
        """Sets the account of this XappOttResponse.


        :param account: The account of this XappOttResponse.
        :type account: str
        """

        self._account = account

    @property
    def accountaccess(self) -> str:
        """Gets the accountaccess of this XappOttResponse.


        :return: The accountaccess of this XappOttResponse.
        :rtype: str
        """
        return self._accountaccess

    @accountaccess.setter
    def accountaccess(self, accountaccess: str):
        """Sets the accountaccess of this XappOttResponse.


        :param accountaccess: The accountaccess of this XappOttResponse.
        :type accountaccess: str
        """

        self._accountaccess = accountaccess

    @property
    def accounttype(self) -> str:
        """Gets the accounttype of this XappOttResponse.


        :return: The accounttype of this XappOttResponse.
        :rtype: str
        """
        return self._accounttype

    @accounttype.setter
    def accounttype(self, accounttype: str):
        """Sets the accounttype of this XappOttResponse.


        :param accounttype: The accounttype of this XappOttResponse.
        :type accounttype: str
        """

        self._accounttype = accounttype

    @property
    def style(self) -> str:
        """Gets the style of this XappOttResponse.


        :return: The style of this XappOttResponse.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style: str):
        """Sets the style of this XappOttResponse.


        :param style: The style of this XappOttResponse.
        :type style: str
        """

        self._style = style

    @property
    def origin(self) -> XappOrigin:
        """Gets the origin of this XappOttResponse.


        :return: The origin of this XappOttResponse.
        :rtype: XappOrigin
        """
        return self._origin

    @origin.setter
    def origin(self, origin: XappOrigin):
        """Sets the origin of this XappOttResponse.


        :param origin: The origin of this XappOttResponse.
        :type origin: XappOrigin
        """

        self._origin = origin

    @property
    def user(self) -> str:
        """Gets the user of this XappOttResponse.


        :return: The user of this XappOttResponse.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user: str):
        """Sets the user of this XappOttResponse.


        :param user: The user of this XappOttResponse.
        :type user: str
        """

        self._user = user

    @property
    def user_device(self) -> XappUserDevice:
        """Gets the user_device of this XappOttResponse.


        :return: The user_device of this XappOttResponse.
        :rtype: XappUserDevice
        """
        return self._user_device

    @user_device.setter
    def user_device(self, user_device: XappUserDevice):
        """Sets the user_device of this XappOttResponse.


        :param user_device: The user_device of this XappOttResponse.
        :type user: XappUserDevice
        """

        self._user_device = user_device

    @property
    def account_info(self) -> XappUserAccountInfo:
        """Gets the account_info of this XappOttResponse.


        :return: The account_info of this XappOttResponse.
        :rtype: XappUserAccountInfo
        """
        return self._account_info

    @account_info.setter
    def account_info(self, account_info: XappUserAccountInfo):
        """Sets the account_info of this XappOttResponse.


        :param account_info: The account_info of this XappOttResponse.
        :type account_info: XappUserAccountInfo
        """
        self._account_info = account_info
