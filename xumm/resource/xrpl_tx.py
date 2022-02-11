#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class XrplTxResource(XummResource):

    @classmethod
    def get_url(cls, tx_hash: str) -> str:
        """
        Gets the GET url of this XrplTxResource

        :param tx_hash: A string contain transaction hash.
        :type: str
        :return: The GET url of this XrplTxResource.
        :rtype: str
        """
        return super(XrplTxResource, cls).platform_url() + 'xrpl-tx' + '/' + tx_hash  # noqa: E501
