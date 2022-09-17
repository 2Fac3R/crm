"""API Configuration."""

# Django Rest Framework
from rest_framework import permissions

# drf-yasg - Yet another Swagger generator
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="CRM API",
        default_version='v1',
        description="API Documentation",
        terms_of_service="#",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)