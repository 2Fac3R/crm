"""CRM URLs Configuration."""

# Django
from django.urls import path, include

# Routes
from .routes.web import urlpatterns as web
from .routes.api import urlpatterns as api


urlpatterns = [
    # WEB
    path('', include(web)),
    # API
    path('api/', include(api)),
]
