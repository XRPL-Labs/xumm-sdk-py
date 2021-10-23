class XummError(Exception):
    def __init__(self, error, status_code=None, headers=None):
        super(XummError, self).__init__(error)

        self.error = error
        self.status_code = status_code
        self.headers = headers

    def __unicode__(self):
        return self.error


class APIError(XummError):
    pass


class APIConnectionError(XummError):
    pass


class InvalidRequestError(XummError):
    pass


class AuthenticationError(XummError):
    pass
