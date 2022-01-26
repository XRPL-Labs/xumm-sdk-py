#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class KycStatusResource(XummResource):

    @classmethod
    def get_url(cls, id: str = None) -> str:
        """
        Gets the GET url of this KycStatusResource

        :param id: A string id.
        :type: str
        :return: The GET url of this KycStatusResource.
        :rtype: str
        """
        return super(KycStatusResource, cls).platform_url() + 'kyc-status/' + id  # noqa: E501

    @classmethod
    def post_url(cls) -> str:
        """
        Gets the POST url of this KycStatusResource

        :return: The POST url of this KycStatusResource.
        :rtype: str
        """
        return super(KycStatusResource, cls).platform_url() + 'kyc-status/'

