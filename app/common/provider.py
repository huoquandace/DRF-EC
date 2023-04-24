import json
from abc import ABC

from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response


class JsonBaseSerializer(ABC):
    """Base JsonSerial"""

    def to_json(self):
        """convert sang json"""
        return json.dumps(self)

    def to_dict(self):
        """convert sang dict"""
        return self.__dict__


class CleanCodeMessage(JsonBaseSerializer):
    def __init__(self, code, text):
        self.code = code
        self.text = text


class CleanCodeResponseObject(Response):
    """Class Response"""

    def __init__(
        self,
        data={},
        message=CleanCodeMessage("", ""),
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
        error={},
    ):
        if message.code:
            data_content = {
                "status": "NG",
                "code": message.code,
                "message": message.text,
                "error": error,
            }
        else:
            data_content = {"status": "OK", "result": data}

        super(CleanCodeResponseObject, self).__init__(
            data=data_content,
            status=status,
            template_name=template_name,
            headers=headers,
            exception=exception,
            content_type=content_type,
        )
