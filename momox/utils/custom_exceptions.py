from ninja.errors import HttpError
from django.utils.translation import gettext_lazy as _


class APIException(HttpError):
    """
    Subclasses should provide `.status_code` and `.message` properties.
    """
    status_code = 500
    message = _('A server error occurred.')

    def __init__(self, message=None, status_code=None):
        message = message or self.message
        status_code = status_code or self.status_code
        super().__init__(status_code, message=message)


class ModelNotFoundException(APIException):
    status_code = 400
    message = 'Model not found'


class EntityDoesNotExist(Exception):
    pass

