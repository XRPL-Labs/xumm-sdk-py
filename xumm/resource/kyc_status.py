#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class KycStatusResource(XummResource):

    @classmethod
    def get_url(cls, id):
        """get_url."""
        return super(KycStatusResource, cls).platform_url() + 'kyc-status/' + id

    @classmethod
    def post_url(cls):
        """post_url."""
        return super(KycStatusResource, cls).platform_url() + 'kyc-status/'

    def refresh_from(cls, **kwargs):
        return cls