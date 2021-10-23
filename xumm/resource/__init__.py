from __future__ import unicode_literals
from xumm import client


class PrintableResource(object):

    def __unicode__(cls):
        return '<xumm::{} {}>'.format(cls.__class__.__name__, cls.id)

    def __str__(cls):
        return str(cls.encode('utf-8'))

    def __repr__(cls):
        attrs = [
            '\'{}\': {}'.format(key, repr(getattr(cls, key)))
            for key
            in cls.__dict__
        ]

        return '\n{{\n\t{}\n}}'.format('\n\t'.join(attrs))


class XummResource(PrintableResource):

    @classmethod
    def list_url(cls):
        return client.build_url() + 'payload' + '/'

    @classmethod
    def get_url(cls, id):
        return client.build_url() + 'payload' + '/' + id + '/'

    @classmethod
    def retrieve_url(cls, instance_id):
        return cls.list_url() + instance_id + '/'

    def __init__(cls, **kwargs):
        cls.refresh_from(**kwargs)

    def refresh_from(cls, **kwargs):
        raise NotImplementedError

    @property
    def instance_url(cls):
        return cls.__class__.retrieve_url(cls.id)
