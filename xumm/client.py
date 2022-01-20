#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

import requests
import textwrap
from typing import List, Dict  # noqa: F401
from requests.exceptions import ConnectionError

from xumm import (
    api_base,
    error,
)


def build_url(endpoint: str = None) -> str:
    url = api_base

    if endpoint:
        url += endpoint

    return url


def get_env() -> str:
    from xumm import env
    return env


# def get_headers() -> Dict[str, object]:
def get_headers():
    from xumm import api_key, api_secret

    if api_key is None:
        raise error.AuthenticationError(
            'No API key provided. (HINT: set your API key using '
            '"xumm.api_key = <API-KEY>"). You can generate API keys '
            'from the Xumm web interface.'
        )
    if api_secret is None:
        raise error.AuthenticationError(
            'No API secret provided. (HINT: set your API key using '
            '"xumm.api_secret = <API-SECRET>"). You can generate API keys '
            'from the Xumm web interface.'
        )

    return {
        'X-API-Key': api_key,
        'X-API-Secret': api_secret,
        'content-type': 'application/json',
        'accept': 'application/json'
    }


def get(url: str):
    try:
        res = requests.get(url, headers=get_headers())
    except Exception as e:
        handle_request_error(e)
    return handle_response(res)


def post(url: str, data: Dict[str, object]):
    try:
        res = requests.post(url, headers=get_headers(), json=data)
    except Exception as e:
        handle_request_error(e)
    return handle_response(res)


def delete(url: str):
    try:
        res = requests.delete(url, headers=get_headers())
    except Exception as e:
        handle_request_error(e)
    return handle_response(res)


def handle_response(res):
    try:
        json = res.json()
    except ValueError as e:
        handle_parse_error(e)

    if not (200 <= res.status_code < 300):
        handle_error_code(json, res.status_code, res.headers)

    return json


def handle_request_error(e: ConnectionError):
    if isinstance(e, requests.exceptions.RequestException):
        msg = 'Unexpected error communicating with Xumm.'
        err = '{}: {}'.format(type(e).__name__, str(e))
    else:
        msg = ('Unexpected error communicating with Xumm. '
               'It looks like there\'s probably a configuration '
               'issue locally.')
        err = 'A {} was raised'.format(type(e).__name__)
        if u'%s' % e:
            err += ' with error message {}'.format(e)
        else:
            err += ' with no error message'

    msg = textwrap.fill(msg) + '\n\n(Network error: {})'.format(err)
    raise error.APIConnectionError(msg)


def handle_error_code(json: Dict[str, object], status_code: int, headers: Dict[str, object]):  # noqa: E501
    if status_code == 400:
        err = json.get('error', 'Bad request')
        raise error.InvalidRequestError(err, status_code, headers)
    elif status_code == 401:
        err = json.get('error', 'Not authorized')
        raise error.AuthenticationError(err, status_code, headers)
    elif status_code == 404:
        err = json.get('error', 'Not found')
        raise error.InvalidRequestError(err, status_code, headers)
    elif status_code == 500:
        err = json.get('error', 'Internal server error')
        raise error.APIError(err, status_code, headers)
    else:
        err = json.get('error', 'Unknown status code ({})'.format(status_code))
        raise error.APIError(err, status_code, headers)


def handle_parse_error(e: ValueError, status_code: int, headers: Dict[str, object]):  # noqa: E501
    err = '{}: {}'.format(type(e).__name__, e)
    msg = 'Error parsing Xumm JSON response. \n\n{}'.format(err)
    raise error.APIError(msg, status_code, headers)
