"""Meeting Serializer."""

# Django Rest Framework
from rest_framework import serializers

# CRM
from crm.models import Meeting


class MeetingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meeting
        fields = ['id', 'url', 'project', 'contact',
                  'title', 'description', 'date']
