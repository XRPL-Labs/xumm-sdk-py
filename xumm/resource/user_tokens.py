#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class UserTokensResource(XummResource):

    @classmethod
    def post_url(cls) -> str:
        """
        Gets the POST url of this UserTokensResource

        :param id: A string id.
        :type: str
        :return: The POST url of this UserTokensResource.
        :rtype: str
        """
        return super(UserTokensResource, cls).platform_url() + 'user-tokens' + '/'  # noqa: E501
