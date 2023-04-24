from functools import wraps

from common.provider import CleanCodeMessage, CleanCodeResponseObject
from django.utils.translation import gettext_lazy as _


def __to_tuple(response):
    return response if isinstance(response, tuple) else (response,)


def parse_request(serializer):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            payload = serializer(data=request.data)
            if not payload.is_valid():
                return CleanCodeResponseObject(
                    message=CleanCodeMessage("ER001", _("Validation Error")),
                    error=payload.errors,
                )

            return func(request, *args, **kwargs)

        return wrapper

    return decorator
