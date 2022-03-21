# Django
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

# Django Rest Framework
from rest_framework.test import APITestCase
from rest_framework import status

# CRM
from ..models import Organization


class OrganizationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.url = reverse('organization-list')

    def test_auth_credentials_not_provided(self):
        """Authentication credentials were not provided."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_access(self):
        """An authenticated user can access."""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_there_is_no_content(self):
        """There is no content yet."""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, [])

    def test_there_is_content(self):
        """There is content."""
        self.client.force_authenticate(user=self.user)
        org = Organization.objects.create()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, org)

    def test_create(self):
        """organizations_create."""
        self.client.force_authenticate(user=self.user)
        data = {
            "name": "string",
            "email": "user@example.com",
            "phone": "string",
            "address": "string",
            "city": "string",
            "region": "string",
            "country": "st",
            "postal_code": "string"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Organization.objects.count(), 1)
        self.assertEqual(Organization.objects.get().name, 'string')

    def test_read(self):
        """organizations_read."""
        self.client.force_authenticate(user=self.user)
        org = Organization.objects.create()
        response = self.client.get(
            reverse('organization-detail', args=(org.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, org)

    def test_update(self):
        """organizations_update."""
        self.client.force_authenticate(user=self.user)
        org = Organization.objects.create()
        data = {
            "name": "new",
            "email": "user@example.com",
            "phone": "string",
            "address": "string",
            "city": "string",
            "region": "string",
            "country": "st",
            "postal_code": "string"
        }
        response = self.client.put(
            reverse('organization-detail', args=(org.pk,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Organization.objects.count(), 1)
        self.assertEqual(Organization.objects.get().name, 'new')

    def test_partial_update(self):
        """organizations_partial_update."""
        self.client.force_authenticate(user=self.user)
        org = Organization.objects.create()
        data = {
            "country": "MX"
        }
        response = self.client.patch(
            reverse('organization-detail', args=(org.pk,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Organization.objects.count(), 1)
        self.assertEqual(Organization.objects.get().country, 'MX')

    def test_delete(self):
        """organizations_delete."""
        self.client.force_authenticate(user=self.user)
        org = Organization.objects.create()
        response = self.client.delete(
            reverse('organization-detail', args=(org.pk,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_pagination_is_fifteen(self):
        """Test pagination is exactly fifteen."""
        self.client.force_authenticate(user=self.user)
        for x in range(30):
            Organization.objects.create()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data['results']), settings.REST_FRAMEWORK['PAGE_SIZE'])
