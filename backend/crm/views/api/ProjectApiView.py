"""Project API View"""

# Django Rest Framework
from rest_framework import viewsets

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# CRM
from crm.models import Project
from crm.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Projects to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    ordering_fields = ['name', ]
    filter_fields = ['organization', ]
    search_fields = ('name', 'description')
