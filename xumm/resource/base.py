import os
from protocols.xumm import client
from protocols.xumm.resource import XummResource
from protocols.xumm.util import (
    cached_property,
)
from basedir import basedir
import json
import time


class Payload(XummResource):

    @classmethod
    def get(cls, id):
        res = client.get(Payload.get_url(id))
        return Payload(**res)

    @classmethod
    def submit(cls, payload):
        res = client.post(cls.list_url(), payload)
        return res

    def refresh_from(cls, **kwargs):
        # print('XUMM ACCOUNT: {}'.format(json.dumps(kwargs, indent=4, sort_keys=True)))
        cls.application = kwargs['application']
        cls.custom_meta = kwargs['custom_meta']
        cls.meta = kwargs['meta']
        cls.payload = kwargs['payload']
        cls.response = kwargs['response']

    def to_any_object(cls):
        return {
            'application': cls.application,
            'custom_meta': cls.custom_meta,
            'meta': cls.meta,
            'payload': cls.payload,
            'response': cls.response,
        }


    def __unicode__(cls):
        return '<{} {}>'.format(cls.__class__.__name__, cls.id)
