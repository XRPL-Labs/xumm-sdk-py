#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class PingResource(XummResource):

    @classmethod
    def get_url(cls) -> str:
        """
        Gets the GET url of this PingResource

        :param id: A string id.
        :type: str
        :return: The GET url of this PingResource.
        :rtype: str
        """
        return super(PingResource, cls).platform_url() + 'ping' + '/'
