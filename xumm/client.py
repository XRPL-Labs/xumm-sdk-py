#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

import requests
import textwrap

from socket import gethostname

from requests.exceptions import ConnectionError
from requests import Response

from typing import List, Dict, Any  # noqa: F401

from xumm import (
    api_base,
    error,
)


def build_url(endpoint: str = None) -> str:
    """
    Returns the base url + endpoint

    :param endpoint: A string endpoint.
    :type: str
    :return: str
    """
    url = api_base

    if endpoint:
        url += endpoint

    return url


def get_env() -> str:
    """
    Returns the sdk env
    :return: str
    """
    from xumm import env
    return env


def get_headers() -> Dict[str, object]:
    """
    Returns the sdk headers + Authentication
    :return: Dict[str, object]
    """
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
        'accept': 'application/json',
        'user-agent': "xumm-sdk/python ({}) requests".format(gethostname(),)
    }


def get(
    url: str,
    access_token: str = None
) -> Dict[str, object]:
    """
    Returns the sdk GET response

    :param url: A string url endpoint.
    :type: str
    :return: Dict[str, object]
    """
    try:
        headers = get_headers()
        if isinstance(access_token, str):
            headers['Authorization'] = f'Bearer {access_token}'
        res = requests.get(url, headers=headers)
    except Exception as e:
        handle_request_error(e)
    return handle_response(res)


def post(
    url: str,
    data: Dict[str, object]
) -> Dict[str, object]:
    """
    Returns the sdk POST response

    :param url: A string url endpoint.
    :type: str
    :param data: A dictionary.
    :type: Dict[str, object]
    :return: Dict[str, object]
    """
    try:
        res = requests.post(url, headers=get_headers(), json=data)
    except Exception as e:
        handle_request_error(e)
    return handle_response(res)


def delete(
    url: str
) -> Dict[str, object]:
    """
    Returns the sdk DELETE response

    :param url: A string url endpoint.
    :type: str
    :return: Dict[str, object]
    """
    try:
        res = requests.delete(url, headers=get_headers())
    except Exception as e:
        handle_request_error(e)
    return handle_response(res)


def handle_response(res: Response) -> Dict[str, object]:
    """
    Returns the sdk JSON response

    :param res: A string url endpoint.
    :type: str
    :return: Dict[str, object]
    """
    try:
        json = res.json()
    except ValueError as e:
        handle_parse_error(e)

    if not (200 <= res.status_code < 300):
        handle_error_code(json, res.status_code, res.headers)

    return json


def handle_request_error(e: ConnectionError):
    """
    Throws the sdk REQUEST error responses

    :param e: A connection error (Network | Server).
    :type: ConnectionError
    :return: throws
    """
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


def handle_error_code(
    json: Dict[str, object],
    status_code: int,
    headers: Dict[str, object]
):
    """
    Throws the sdk API error responses

    :param json: A json response object.
    :type: Dict[str, object]
    :param status_code: An integer status code.
    :type: int
    :param headers: A headers response dictionary.
    :type: Dict[str, object]
    :return: throws
    """

    # invalid response from api
    if 'error' not in json:
        raise ValueError('Error parsing Xumm JSON response: error')

    # hard error
    if isinstance(json['error'], bool):
        if 'code' not in json or 'message' not in json:
            raise ValueError('Error parsing Xumm JSON response: code/message')

        err = 'Error code {}, message: {}'.format(
            json['code'],
            json['message'],
        )
    # soft error
    elif isinstance(json['error'], dict):
        if 'code' not in json['error'] or 'reference' not in json['error']:
            raise ValueError(
                    'Error parsing Xumm JSON response: code/reference'
                )

        err = 'Error code {}, see XUMM Dev Console, reference: {}'.format(
            json['error']['code'],
            json['error']['reference'],
        )
    # this should neven happen
    else:
        err = 'Unexpected error'

    if status_code == 400:
        raise error.InvalidRequestError(err, status_code, headers)
    elif status_code == 401:
        raise error.AuthenticationError(err, status_code, headers)
    elif status_code == 404:
        raise error.InvalidRequestError(err, status_code, headers)
    elif status_code == 500:
        raise error.APIError(err, status_code, headers)
    else:
        raise error.APIError(err, status_code, headers)


def handle_parse_error(
    e: ValueError,
    status_code: int,
    headers: Dict[str, object]
):
    """
    Throws the sdk JSON error response

    :param e: A value error (JSON | KeyError).
    :type: ValueError
    :param status_code: An integer status code.
    :type: int
    :param headers: A headers response dictionary.
    :type: Dict[str, object]
    :return: throws
    """
    err = '{}: {}'.format(type(e).__name__, e)
    msg = 'Error parsing Xumm JSON response. \n\n{}'.format(err)
    raise error.APIError(msg, status_code, headers)
