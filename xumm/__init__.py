import os

api_base = 'https://xumm.app/api/v1/'
api_key = os.environ.get('XUMM_APIKEY', None)
api_secret = os.environ.get('XUMM_APISECRET', None)
api_version = 'v1'
env = 'production'
debug = True if os.environ.get('DEBUG') == 'xumm-sdk*' else False  # noqa: E501

from xumm.resource.base import (  # noqa
    XummSdk,
)
