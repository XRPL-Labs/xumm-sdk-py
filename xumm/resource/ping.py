#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class PingResource(XummResource):

    @classmethod
    def get_url(cls) -> str:
        """get_url."""
        return super(PingResource, cls).platform_url() + 'ping' + '/'

    def refresh_from(cls, **kwargs) -> 'PingResource':
        return cls
