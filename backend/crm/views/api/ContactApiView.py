"""Contact API View"""

# Django Rest Framework
from rest_framework import viewsets

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# CRM
from crm.models import Contact
from crm.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Contacts to be viewed or edited.
    """
    queryset = Contact.objects.all().order_by('last_name')
    serializer_class = ContactSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('first_name', 'last_name')
    filter_fields = ('organization', 'country', 'city')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
