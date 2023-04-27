#!/usr/bin/env python
# coding: utf-8
import logging

import xumm


class Oauth2Example:
    def __init__(self):
        logging.debug('')
        self.sdk = xumm.XummSdk('API_KEY', 'API_SECRET')
        self.logger = logging.getLogger(self.__module__)
        self.logger.setLevel(level=logging.DEBUG)

    def oauth_example(self):
        auth, state = self.sdk.oauth2.auth('http://localhost:3000')
        print(auth)
        print(state)
        # FOR TESTING NON HTTP REDIRECT URIS
        import os
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
        # FOR TESTING NON HTTP REDIRECT URIS
        response = 'http://localhost:3000/?authorization_code=gAAAAABjgAd2TCQb7Fj1VACAaCRHl_dUsMlsSsrgYY-rDnoUG4KsvN9XXrO3U5_IfynzSZ2lyGvznGY8JsusHTo2fsWQD5jWwUxfoQlclVYsbPyWZO6jOxB5YXKFdg4HOlezpiCfvVDPEd5b7LJVlEb9kuDyhirucfb3OGJrsJPIMtqYwOMgReeIgnCm3vudDLV4CHZLr9RY&code=gAAAAABjgAd2TCQb7Fj1VACAaCRHl_dUsMlsSsrgYY-rDnoUG4KsvN9XXrO3U5_IfynzSZ2lyGvznGY8JsusHTo2fsWQD5jWwUxfoQlclVYsbPyWZO6jOxB5YXKFdg4HOlezpiCfvVDPEd5b7LJVlEb9kuDyhirucfb3OGJrsJPIMtqYwOMgReeIgnCm3vudDLV4CHZLr9RY&state=NCnOPAxGX3ZIb27vAyWqPT9PzDrTR6'
        oauth2_config = self.sdk.oauth2.token('http://localhost:3000', response)
        print(oauth2_config)


if __name__ == "__main__":
    Oauth2Example().oauth_example()
