#!/usr/bin/env python
# coding: utf-8

from typing import Dict  # noqa: F401
import json


def read_json(path: str) -> Dict[str, object]:
    with open(path) as json_file:
        return json.load(json_file)


def write_json(data: Dict[str, object], path: str):
    with open(path, 'w') as json_file:
        json.dump(data, json_file)
