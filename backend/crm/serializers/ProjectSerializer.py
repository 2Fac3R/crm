"""Project Serializer."""

# Django Rest Framework
from rest_framework import serializers

# CRM
from crm.models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'url', 'organization', 'name', 'description']
