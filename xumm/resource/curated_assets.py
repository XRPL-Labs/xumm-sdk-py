#!/usr/bin/env python
# coding: utf-8
from xumm import client, error
from xumm.resource import XummResource

class CuratedAssetsResource(XummResource):

    @classmethod
    def get_url(cls):
        """get_url."""
        return super(CuratedAssetsResource, cls).platform_url() + 'curated_assets' + '/'

    def refresh_from(cls, **kwargs):
        return cls