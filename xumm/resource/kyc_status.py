import os
from xumm.resource import XummResource
import six
import json

from typing import List, Dict  # noqa: F401

class GetKycStatusRequest(XummResource):

    @classmethod
    def get_url(cls, id):
        """get_url."""
        return super(GetKycStatusRequest, cls).platform_url() + 'kyc-status/' + id


class PostKycStatusRequest(XummResource):

    @classmethod
    def post_url(cls):
        """post_url."""
        return super(PostKycStatusRequest, cls).platform_url() + 'kyc-status/'