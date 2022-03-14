""" Contact Serializer."""

# Django
from crm.models import Contact

# Django Rest Framework
from rest_framework import serializers


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['url', 'organization', 'first_name', 'last_name', 'email',
                  'phone', 'address', 'city', 'region', 'country', 'postal_code']
