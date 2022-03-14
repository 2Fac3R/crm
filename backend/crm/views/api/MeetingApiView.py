"""Meeting API View"""

# Django Rest Framework
from rest_framework import viewsets

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# CRM
from crm.models import Meeting
from crm.serializers import MeetingSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Meetings to be viewed or edited.
    """
    queryset = Meeting.objects.all().order_by('title')
    serializer_class = MeetingSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('title', 'date')
    filter_fields = ('project', 'contact', 'date')
    search_fields = ('title', 'description')
