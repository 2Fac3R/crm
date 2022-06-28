"""CRM URLs Configuration."""

# Django
from django.urls import path, re_path, include

# Django Rest Framework
from rest_framework import routers

# API
from .conf.api import schema_view
from .views.api import UserApiView as user_views
from .views.api import GroupApiView as group_views
from .views.api import OrganizationApiView as organization_views
from .views.api import ProjectApiView as project_views
from .views.api import ContactApiView as contact_views
from .views.api import MeetingApiView as meeting_views

# JWT - JSON Web Token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


# API Routing
router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='user')
router.register(r'groups', group_views.GroupViewSet, basename='group')
router.register(r'organizations',
                organization_views.OrganizationViewSet, basename='organization')
router.register(r'projects',
                project_views.ProjectViewSet, basename='project')
router.register(r'contacts',
                contact_views.ContactViewSet, basename='contact')
router.register(r'meetings',
                meeting_views.MeetingViewSet, basename='meeting')

# Routes
urlpatterns = [
    # api/v1/
    path('', include(router.urls)),
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
    # JWT - JSON Web Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
