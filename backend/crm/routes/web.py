"""Web urls."""

# Django
from django.urls import path

# Views
from ..views.web import HomeView as home_views


urlpatterns = [
    path('', home_views.index, name='index'),
]
