"""Organization Serializer."""

# Django Rest Framework
from rest_framework import serializers

# CRM
from crm.models import Organization


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'url', 'name', 'email', 'phone',
                  'address', 'city', 'region', 'country', 'postal_code']
