#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource

class XrplTxResource(XummResource):

    @classmethod
    def get_url(cls, id):
        """get_url."""
        return super(XrplTxResource, cls).platform_url() + 'xrpl_tx' + '/' + id

    def refresh_from(cls, **kwargs):
        return cls