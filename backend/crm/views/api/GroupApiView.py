"""Group API View"""

# Django
from django.contrib.auth.models import Group

# Django Rest Framework
from rest_framework import viewsets, permissions

# CRM
from crm.serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]
