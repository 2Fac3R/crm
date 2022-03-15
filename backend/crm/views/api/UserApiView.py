"""User API View."""

# Django
from django.contrib.auth.models import User

# Django Rest Framework
from rest_framework import viewsets, permissions

# CRM
from crm.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
