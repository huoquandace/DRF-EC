from rest_framework.renderers import JSONRenderer as BaseJSONRenderer

from app.common.provider import CleanCodeMessage, CleanCodeResponseObject


class JSONRenderer(BaseJSONRenderer):
    """Xử lý các response trước khi trả lại cho người dùng"""

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """Xử lý cá response được chủ động return"""
        # status_code = renderer_context['response'].status_code
        if type(renderer_context["response"]) is CleanCodeResponseObject:
            return super(JSONRenderer, self).render(
                data, accepted_media_type, renderer_context
            )
        # Map các response được handle bởi django rest VD: ModelViewSet, ...
        renderer_context["response"] = CleanCodeResponseObject(data=data, error={})
        return self.render(data, accepted_media_type, renderer_context)
