from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Docs API",
        default_version="v1",
        description="This is an e-commerce template for buying and selling that includes product APIs and orders.",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
