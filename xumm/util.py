#!/usr/bin/env python
# coding: utf-8

from typing import Dict, Tuple  # noqa: F401
import json

import requests


def read_json(path: str) -> Dict[str, object]:
    """
    Reads json from file path
    :return: Dict[str, object]
    """
    with open(path) as json_file:
        return json.load(json_file)


def write_json(data: Dict[str, object], path: str):
    """
    Writes json to file path
    :return:
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file)


def parse_oauth2_response(url: str) -> Tuple[str, str]:
    if not isinstance(url, str):
        raise ValueError('invalid url type. must be `string`')

    query = requests.utils.urlparse(url).query
    params = dict(x.split('=') for x in query.split('&'))

    if 'authorization_code' not in params:
        raise ValueError('invalid response param: `authorization_code`')

    if 'state' not in params:
        raise ValueError('invalid response param: `state`')

    return params.get('authorization_code'), params.get('state')
