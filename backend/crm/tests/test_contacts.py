# Django
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings

# Django Rest Framework
from rest_framework.test import APITestCase
from rest_framework import status

# CRM
from ..models import Organization, Contact


class ContactTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.org = Organization.objects.create()
        self.url = reverse('contact-list')

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
        contact = Contact.objects.create(organization=self.org)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, contact)

    def test_create(self):
        """contacts_create."""
        self.client.force_authenticate(user=self.user)
        data = {
            "organization": reverse('organization-detail', args=(self.org.pk,)),
            "first_name": "string",
            "last_name": "string",
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
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().first_name, 'string')

    def test_read(self):
        """contacts_read."""
        self.client.force_authenticate(user=self.user)
        contact = Contact.objects.create(organization=self.org)
        response = self.client.get(
            reverse('contact-detail', args=(contact.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, contact)

    def test_update(self):
        """contacts_update."""
        self.client.force_authenticate(user=self.user)
        contact = Contact.objects.create(organization=self.org)
        data = {
            "organization": reverse('organization-detail', args=(self.org.pk,)),
            "first_name": "new",
            "last_name": "string",
            "email": "user@example.com",
            "phone": "string",
            "address": "string",
            "city": "string",
            "region": "string",
            "country": "st",
            "postal_code": "string"
        }
        response = self.client.put(
            reverse('contact-detail', args=(contact.pk,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().first_name, 'new')

    def test_partial_update(self):
        """contacts_partial_update."""
        self.client.force_authenticate(user=self.user)
        contact = Contact.objects.create(organization=self.org)
        data = {
            "country": "MX"
        }
        response = self.client.patch(
            reverse('contact-detail', args=(contact.pk,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().country, 'MX')

    def test_delete(self):
        """contacts_delete."""
        self.client.force_authenticate(user=self.user)
        contact = Contact.objects.create(organization=self.org)
        response = self.client.delete(
            reverse('contact-detail', args=(contact.pk,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_pagination_is_fifteen(self):
        """Test pagination is exactly fifteen."""
        self.client.force_authenticate(user=self.user)
        for x in range(30):
            Contact.objects.create(organization=self.org)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data['results']), settings.REST_FRAMEWORK['PAGE_SIZE'])

    def test_search(self):
        """Test searching functionality."""
        self.client.force_authenticate(user=self.user)
        Contact.objects.create(
            organization=self.org,
            email="email@example.com"
        )
        contacts = Contact.objects.filter(email='email@example.com')
        response = self.client.get(self.url, {'search': 'email@example.com'})
        self.assertEqual(len(response.data['results']), contacts.count())
