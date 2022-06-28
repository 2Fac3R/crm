"""Main URLs Configuration."""

# Django
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


# Routes
urlpatterns = [
    # Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # API
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('crm.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
