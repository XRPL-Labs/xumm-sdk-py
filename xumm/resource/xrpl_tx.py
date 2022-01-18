import os
from xumm.resource import XummResource
import six
import json

from typing import List, Dict  # noqa: F401


class GetXrplTxRequest(XummResource):

    @classmethod
    def get_url(cls, id):
        """get_url."""
        return super(GetXrplTxRequest, cls).platform_url() + 'xrpl_tx' + '/' + id