# Django
from django.urls import reverse
from django.contrib.auth.models import User

# Django Rest Framework
from rest_framework.test import APITestCase
from rest_framework import status


class UserTestCase(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="admin", password="pass")
        self.user = User.objects.create_user(username="test", password="test")
        self.url = reverse('user-list')

    def test_auth_credentials_not_provided(self):
        """Authentication credentials were not provided."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_do_not_have_permissions_to_perform_action(self):
        """You do not have permission to perform this action."""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_can_access(self):
        """A superuser can access."""
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
