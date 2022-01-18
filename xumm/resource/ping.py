from xumm.resource import XummResource

class PingResource(XummResource):

    @classmethod
    def get_url(cls):
        """get_url."""
        return super(PingResource, cls).platform_url() + 'ping' + '/'

    def refresh_from(cls, **kwargs):
        return cls