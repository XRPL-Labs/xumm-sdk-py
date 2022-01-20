#!/usr/bin/env python
# coding: utf-8

from typing import Dict  # noqa: F401


class RPCError(Exception):
    def __init__(
        cls,
        error: str,
        status_code: int = None,
        headers: Dict[str, object] = None
    ):
        super(RPCError, cls).__init__(error)

        cls.error = error
        cls.status_code = status_code
        cls.headers = headers

    def __unicode__(cls):
        return cls.error


class APIError(RPCError):
    pass


class APIConnectionError(RPCError):
    pass


class InvalidRequestError(RPCError):
    pass


class AuthenticationError(RPCError):
    pass


class WSError(Exception):
    def __init__(self, message, data):
        super(WSError, self).__init__(message)

        self.message = message
        self.data = data

    def __str__(self):
        result = '[(' + self.message
        if self.data:
            result += ', ' + str(self.data)

        result += ')]'
        return result


class UnexpectedError(WSError):
    pass


class ConnectionError(WSError):
    pass


class NotConnectedError(ConnectionError):
    pass


class DisconnectedError(ConnectionError):
    pass


class TimeoutError(ConnectionError):
    pass


class ResponseFormatError(ConnectionError):
    pass
