"""Contact Serializer."""

# Django Rest Framework
from rest_framework import serializers

# CRM
from crm.models import Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'url', 'organization', 'first_name', 'last_name', 'email',
                  'phone', 'address', 'city', 'region', 'country', 'postal_code']
