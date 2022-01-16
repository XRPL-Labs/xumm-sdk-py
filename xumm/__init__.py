api_base = 'https://xumm.app/api/v1/'
api_key = None
api_secret = None
api_version = 'v1'
env = 'production'

from dotenv import load_dotenv

from xumm.resource.base import (  # noqa
    XummSdk,
    XummWs,
)

load_dotenv()
