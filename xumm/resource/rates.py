#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class RatesResource(XummResource):

    @classmethod
    def get_url(cls, id: str = None) -> str:
        """
        Gets the GET url of this RatesResource

        :param id: A string id.
        :type: str
        :return: The GET url of this RatesResource.
        :rtype: str
        """
        return '{}{}/{}'.format(
            super(RatesResource, cls).platform_url(),
            'rates',
            id.strip().upper()
        )

    def refresh_from(cls, **kwargs) -> 'RatesResource':
        return cls
