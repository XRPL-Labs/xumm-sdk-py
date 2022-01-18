import os
from xml.dom.minidom import AttributeList
from xumm import client
from xumm.resource import XummResource
import json
import time
import six

from typing import List, Dict  # noqa: F401

class GetCuratedAssetsRequest(XummResource):

    @classmethod
    def get_url(cls):
        """get_url."""
        return super(GetCuratedAssetsRequest, cls).platform_url() + 'curated_assets' + '/'