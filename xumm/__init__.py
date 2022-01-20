import os

from dotenv import load_dotenv
load_dotenv()

api_base = 'https://xumm.app/api/v1/'
api_key = os.environ.get('XUMM_APIKEY', None)
api_secret = os.environ.get('XUMM_APISECRET', None)
api_version = 'v1'
env = 'production'

from xumm.resource.base import (  # noqa
    XummSdk,
)
