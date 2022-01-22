#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class XrplTxResource(XummResource):

    @classmethod
    def get_url(cls, id: str = None) -> str:
        """
        Gets the GET url of this XrplTxResource

        :param id: A string id.
        :type: str
        :return: The GET url of this XrplTxResource.
        :rtype: str
        """
        return super(XrplTxResource, cls).platform_url() + 'xrpl_tx' + '/' + id  # noqa: E501

    def refresh_from(cls, **kwargs) -> 'XrplTxResource':
        return cls
