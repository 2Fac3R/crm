"""Backend URL Configuration."""

# Django
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# Django Rest Framework
from rest_framework import routers
from rest_framework import permissions

# drf-yasg - Yet another Swagger generator
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# CRM
from crm.views.api import UserApiView as user_views
from crm.views.api import GroupApiView as group_views
from crm.views.api import OrganizationApiView as organization_views
from crm.views.api import ProjectApiView as project_views

# Routing
router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='user')
router.register(r'groups', group_views.GroupViewSet, basename='group')
router.register(r'organizations',
                organization_views.OrganizationViewSet, basename='organization')
router.register(r'projects',
                project_views.ProjectViewSet, basename='project')

# API Conf
schema_view = get_schema_view(
    openapi.Info(
        title="Userlab API",
        default_version='v1',
        description="API Documentation",
        terms_of_service="127.0.0.1/#",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Routes
urlpatterns = [
    # Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # API
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # API Documentation
    re_path(
        'swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
