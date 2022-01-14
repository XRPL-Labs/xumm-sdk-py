from __future__ import unicode_literals
from xumm import client


class PrintableResource(object):

    def to_dict(cls):
        return cls.to_dict()

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
    def platform_url(cls):
        return client.build_url() + 'platform' + '/'

    def __init__(cls, **kwargs):
        cls.refresh_from(**kwargs)

    def refresh_from(cls, **kwargs):
        raise NotImplementedError
