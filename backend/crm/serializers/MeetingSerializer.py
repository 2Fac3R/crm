""" Meeting Serializer."""

# Django
from crm.models import Meeting

# Django Rest Framework
from rest_framework import serializers


class MeetingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meeting
        fields = ['url', 'project', 'contact', 'title', 'description', 'date']
