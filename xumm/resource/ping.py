import os
from xumm import client
from xumm.resource import XummResource
import json
import time
import six


class PingRequest(XummResource):

    @classmethod
    def get_url(cls):
        """get_url."""
        return super(PingRequest, cls).platform_url() + 'ping' + '/'
