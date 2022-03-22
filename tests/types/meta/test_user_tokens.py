#!/usr/bin/env python
# coding: utf-8

import pytest
from testing_config import BaseTestConfig

from xumm.resource.types import (
    UserTokenValidity,
    UserTokenResponse,
)

class TestUserTokens(BaseTestConfig):

    def test_user_token_validity(cls):
        print('should set user token validity')

        dict = cls.json_fixtures['userTokens']['tokens'][0]
        cls.assertEqual(UserTokenValidity(**dict).to_dict(), dict)

    def test_user_token_validity_fail(cls):
        print('should fail to set user token validity')

        dict = {
            "user_token": "00000001-1111-2222-af2f-f794874a80b0",
            "active": True,
            "token_issued": '0', # FAILS
            "token_expiration": 3600
        }

        with pytest.raises(ValueError, match=r"Invalid value: 0 for `token_issued`, must be a `<class 'int'>` found: <class 'str'>"):
            UserTokenValidity(**dict)
            cls.fail("UserTokenValidity: raised Exception unexpectedly!")

    def test_user_token_response(cls):
        print('should set user token response')

        dict = cls.json_fixtures['userTokens']
        cls.assertEqual(UserTokenResponse(**dict).to_dict(), dict)

    def test_user_token_response_fail(cls):
        print('should fail to set user token response')

        dict = {
            "tokens": [{
                "user_token": "00000001-1111-2222-af2f-f794874a80b0",
                "active": True,
                "token_issued": '0', # FAILS
                "token_expiration": 3600
            }]
        }

        with pytest.raises(ValueError, match=r"Invalid value: 0 for `token_issued`, must be a `<class 'int'>` found: <class 'str'>"):
            UserTokenResponse(**dict)
            cls.fail("UserTokenResponse: raised Exception unexpectedly!")