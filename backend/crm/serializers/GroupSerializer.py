"""Group Serializer."""

# Django
from django.contrib.auth.models import Group

# Django Rest Framework
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
