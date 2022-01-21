#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class KycStatusResource(XummResource):

    @classmethod
    def get_url(cls, id: str = None) -> str:
        """get_url."""
        return super(KycStatusResource, cls).platform_url() + 'kyc-status/' + id  # noqa: E501

    @classmethod
    def post_url(cls) -> str:
        """post_url."""
        return super(KycStatusResource, cls).platform_url() + 'kyc-status/'

    def refresh_from(cls, **kwargs) -> 'KycStatusResource':
        return cls
