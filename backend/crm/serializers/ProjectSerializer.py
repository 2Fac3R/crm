""" Project Serializer."""

# Django
from crm.models import Project

# Django Rest Framework
from rest_framework import serializers


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'url', 'organization', 'name', 'description']
