#!/usr/bin/env python
# coding: utf-8

from xumm.resource import XummResource


class CuratedAssetsResource(XummResource):

    @classmethod
    def get_url(cls) -> str:
        """
        Gets the GET url of this KycStatusResource

        :return: The GET url of this KycStatusResource.
        :rtype: str
        """
        return super(CuratedAssetsResource, cls).platform_url() + 'curated-assets'  # noqa: E501
