#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class XrplTxResource(XummResource):

    @classmethod
    def get_url(cls, id: str = None) -> str:
        """get_url."""
        return super(XrplTxResource, cls).platform_url() + 'xrpl_tx' + '/' + id  # noqa: E501

    def refresh_from(cls, **kwargs) -> 'XrplTxResource':
        return cls
