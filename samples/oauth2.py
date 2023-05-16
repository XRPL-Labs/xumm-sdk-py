#!/usr/bin/env python
# coding: utf-8
import logging

import xumm
from xumm.util import parse_oauth2_response


class Oauth2Example:
    def __init__(self):
        logging.debug('')
        self.sdk = xumm.XummSdk('API_KEY', 'API_SECRET')
        self.logger = logging.getLogger(self.__module__)
        self.logger.setLevel(level=logging.DEBUG)

    def oauth_example(self):
        redirect_url: str = 'http://localhost:3000'
        auth_url, pre_state = self.sdk.oauth2.auth(redirect_url)
        print(auth_url)
        print(pre_state)

        # FOR TESTING NON HTTP REDIRECT URI
        import os
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
        # FOR TESTING NON HTTP REDIRECT URI

        # 'http://localhost:3000/?authorization_code=gAAAAABjgAd2TCQb7Fj1VACAaCRHl_dUsMlsSsrgYY-rDnoUG4KsvN9XXrO3U5_IfynzSZ2lyGvznGY8JsusHTo2fsWQD5jWwUxfoQlclVYsbPyWZO6jOxB5YXKFdg4HOlezpiCfvVDPEd5b7LJVlEb9kuDyhirucfb3OGJrsJPIMtqYwOMgReeIgnCm3vudDLV4CHZLr9RY&code=gAAAAABjgAd2TCQb7Fj1VACAaCRHl_dUsMlsSsrgYY-rDnoUG4KsvN9XXrO3U5_IfynzSZ2lyGvznGY8JsusHTo2fsWQD5jWwUxfoQlclVYsbPyWZO6jOxB5YXKFdg4HOlezpiCfvVDPEd5b7LJVlEb9kuDyhirucfb3OGJrsJPIMtqYwOMgReeIgnCm3vudDLV4CHZLr9RY&state=NCnOPAxGX3ZIb27vAyWqPT9PzDrTR6'
        response_url = input("\n\nPlease paste the response entire url here: ")
        code, post_state = parse_oauth2_response(response_url)

        # pre_state != post_state => FAIL

        oauth2_config = self.sdk.oauth2.token(redirect_url, code)
        res = self.sdk.oauth2.userinfo(oauth2_config.access_token)
        print(res.to_dict())


if __name__ == "__main__":
    Oauth2Example().oauth_example()
