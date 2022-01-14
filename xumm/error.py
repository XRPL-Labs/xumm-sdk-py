from typing import Dict  # noqa: F401

class XummError(Exception):
    def __init__(
        cls, 
        error: str, 
        status_code: int=None, 
        headers: Dict[str, object]=None
    ):
        super(XummError, cls).__init__(error)

        cls.error = error
        cls.status_code = status_code
        cls.headers = headers

    def __unicode__(cls):
        return cls.error


class APIError(XummError):
    pass


class APIConnectionError(XummError):
    pass


class InvalidRequestError(XummError):
    pass


class AuthenticationError(XummError):
    pass
