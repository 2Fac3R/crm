"""Main URLs Configuration."""

# Django
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


# Routes
urlpatterns = [
    # CRM
    path('crm/', include('crm.urls')),
    # Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
