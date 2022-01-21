#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class CuratedAssetsResource(XummResource):

    @classmethod
    def get_url(cls) -> str:
        """get_url."""
        return super(CuratedAssetsResource, cls).platform_url() + 'curated_assets' + '/'  # noqa: E501

    def refresh_from(cls, **kwargs) -> 'CuratedAssetsResource':
        return cls
