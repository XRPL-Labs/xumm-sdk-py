#!/usr/bin/env python
# coding: utf-8
import logging

import xumm
from xumm.util import parse_oauth2_response


class Oauth2Example:
    def __init__(self):
        logging.debug('')
        self.sdk = xumm.XummSdk('5d44be5c-1721-4e2b-9349-b89331bcdeac', 'fcd166c7-be37-4663-9d8a-5b16a38dade0')
        self.logger = logging.getLogger(self.__module__)
        self.logger.setLevel(level=logging.DEBUG)

    def oauth_example(self):
        # redirect_url: str = 'http://localhost:3000'
        # auth_url, pre_state = self.sdk.oauth2.auth(redirect_url)
        # print(auth_url)
        # print(pre_state)

        # # FOR TESTING NON HTTP REDIRECT URI
        # import os
        # os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
        # # FOR TESTING NON HTTP REDIRECT URI

        # # 'http://localhost:3000/?authorization_code=gAAAAABjgAd2TCQb7Fj1VACAaCRHl_dUsMlsSsrgYY-rDnoUG4KsvN9XXrO3U5_IfynzSZ2lyGvznGY8JsusHTo2fsWQD5jWwUxfoQlclVYsbPyWZO6jOxB5YXKFdg4HOlezpiCfvVDPEd5b7LJVlEb9kuDyhirucfb3OGJrsJPIMtqYwOMgReeIgnCm3vudDLV4CHZLr9RY&code=gAAAAABjgAd2TCQb7Fj1VACAaCRHl_dUsMlsSsrgYY-rDnoUG4KsvN9XXrO3U5_IfynzSZ2lyGvznGY8JsusHTo2fsWQD5jWwUxfoQlclVYsbPyWZO6jOxB5YXKFdg4HOlezpiCfvVDPEd5b7LJVlEb9kuDyhirucfb3OGJrsJPIMtqYwOMgReeIgnCm3vudDLV4CHZLr9RY&state=NCnOPAxGX3ZIb27vAyWqPT9PzDrTR6'
        # response_url = input("\n\nPlease paste the response entire url here: ")
        # code, post_state = parse_oauth2_response(response_url)

        # # pre_state != post_state => FAIL

        # oauth2_config = self.sdk.oauth2.token(redirect_url, code)
        # print(oauth2_config.access_token)

        access_token: str = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiI1ZDQ0YmU1Yy0xNzIxLTRlMmItOTM0OS1iODkzMzFiY2RlYWMiLCJhdWQiOiI1ZDQ0YmU1Yy0xNzIxLTRlMmItOTM0OS1iODkzMzFiY2RlYWMiLCJzdWIiOiJyTDlNZDF6b0c3Q0wyTXJTZEt1bWE5d211Q0JQTjdBblQiLCJlbWFpbCI6IjVkNDRiZTVjLTE3MjEtNGUyYi05MzQ5LWI4OTMzMWJjZGVhYytyTDlNZDF6b0c3Q0wyTXJTZEt1bWE5d211Q0JQTjdBblRAeHVtbS5tZSIsImFwcF91dWlkdjQiOiI1ZDQ0YmU1Yy0xNzIxLTRlMmItOTM0OS1iODkzMzFiY2RlYWMiLCJhcHBfbmFtZSI6IlNvbWUgVHV0b3JpYWwgQXBwIiwicGF5bG9hZF91dWlkdjQiOiI5OWI0ODY5OS1kOThhLTQ5NGEtODlmZi04MDc2M2E4ODQxOTMiLCJ1c2VydG9rZW5fdXVpZHY0IjoiN2RmMjEwZTMtNjVlNS00ZDFjLWIzODItNDc4Zjk4Y2E5ZGU2IiwibmV0d29ya190eXBlIjoiQ1VTVE9NIiwibmV0d29ya19lbmRwb2ludCI6IndzczovL2hvb2tzLXRlc3RuZXQtdjMueHJwbC1sYWJzLmNvbSIsImlhdCI6MTY4NDI3MDI5NCwiZXhwIjoxNjg0MzU2Njk0LCJpc3MiOiJodHRwczovL29hdXRoMi54dW1tLmFwcCJ9.FOjP3fA0Ln3dDxNgbj7ECnekzR8t4RJP5D9WZLZHK_7wVEu0T6crl2h_LaiPyHjEn-MP9jf05QLlKcwwE8o99EEjmR4GEMMbigDCRgL4CW0kJujWVBf-sIH5ePuNy0X5W1AUlPlziCNGtAbxKp0CD9dwom8T0fFQqz-pgRe_UJzXk-hJ-KlfOXoDsqW34Y2jTWvSTyUzW03ssAp0FQlYWiNQRbnhPRrRdvvcyKONm2NB7p7h2i-xZZThlxAqTB2v2PXew0R1D0eBuQqYULuP2yCcsP-espmRwRbmnGlyvavXasfOURvhPic1XCws8i7toqCj4aU85kxFNOdFZLQStjajI-f0oV7ksXsLtL6dhFj1uqAqWAAznRYR3wv9Bklh8LNOnTb7eldkUhPUyNw5r_L2Wj17nqpr8rN40HjeInsB1uHCtqtYY1WFA2wg2bQ3jd7IQ8KM8ZVxqmAeiywIYFWvYpayBSFZZJ6dTjofGg_KBrwbwqzuHmYEfKy6fl1D'
        res = self.sdk.oauth2.userinfo(access_token)
        print(res.to_dict())

if __name__ == "__main__":
    Oauth2Example().oauth_example()
