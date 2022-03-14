"""Organization API View"""

# Django Rest Framework
from rest_framework import viewsets

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# CRM
from crm.models import Organization
from crm.serializers import OrganizationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Organizations to be viewed or edited.
    """
    queryset = Organization.objects.all().order_by('name')
    serializer_class = OrganizationSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    ordering_fields = ['name', ]  # '__all__'
    filter_fields = ('country', 'city')
    search_fields = ('name', 'phone')
