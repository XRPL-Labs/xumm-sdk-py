import os
from typing import Dict  # noqa: F401

class CachedProperty(object):
    """
    A property that is only computed once per instance and then replaces
    itself with an ordinary attribute. Deleting the attribute resets the
    property.

    Taken from https://github.com/bottlepy/bottle/blob/master/bottle.py
    """

    # TODO: allow refresh

    def __init__(self, func):
        self.__doc__ = getattr(func, '__doc__')
        self.func = func

    def __get__(self, obj, cls):
        if obj is None:
            return self

        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value

cached_property = CachedProperty

import json

def read_json(path: str) -> Dict[str, object]:
    with open(path) as json_file:
        return json.load(json_file)

def write_json(data: Dict[str, object], path: str):
    with open(path, 'w') as json_file:
        json.dump(data, json_file)