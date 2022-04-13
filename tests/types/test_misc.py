import pytest
from testing_config import BaseTestConfig

from xumm.resource.types import (
    ReturnUrl,
    Options,
)

class TestMiscTypes(BaseTestConfig):

    def test_return_url(cls):
        print('should set return url')

        dict = cls.json_fixtures['webhook']['payloadResponse']['return_url']
        cls.assertEqual(ReturnUrl(**dict).to_dict(), dict)
    
    def test_return_url_fail(cls):
        print('should fail to set return url')

        dict = {}
        with pytest.raises(ValueError, match=r'Invalid value for `app`, must not be `None`'):
            ReturnUrl(**dict)
            cls.fail("ReturnUrl: raised Exception unexpectedly!")

    def test_return_options(cls):
        print('should set options')

        dict = {
          'submit': True,
          'multisign': True,
          'expire': 0,
          'signers': ['test'],
          'return_url': {
            'app': 'string',
            'web': 'string'
          }
        }
        cls.assertEqual(Options(**dict).to_dict(), dict)
    
    def test_options_fail(cls):
        print('should fail to set options')

        dict = {
          'submit': None,  # FAILS
          'multisign': True,
          'expire': 0,
          'signers': None,
          'return_url': {
            'app': 'string',
            'web': 'string'
          }
        }
        with pytest.raises(ValueError, match=r'Invalid value for `submit`, must not be `None`'):
            Options(**dict)
            cls.fail("Options: raised Exception unexpectedly!")