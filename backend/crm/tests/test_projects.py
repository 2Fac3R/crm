# Django
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

# Django Rest Framework
from rest_framework.test import APITestCase
from rest_framework import status

# CRM
from ..models import Organization, Project


class ProjectTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.org = Organization.objects.create()
        self.url = reverse('project-list')

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
        project = Project.objects.create(organization=self.org)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, project)

    def test_create(self):
        """projects_create."""
        self.client.force_authenticate(user=self.user)
        data = {
            "organization": reverse('organization-detail', args=(self.org.pk,)),
            "name": "string",
            "description": "string"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get().name, 'string')

    def test_read(self):
        """projects_read."""
        self.client.force_authenticate(user=self.user)
        project = Project.objects.create(organization=self.org)
        response = self.client.get(
            reverse('project-detail', args=(project.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, project)

    def test_update(self):
        """projects_update."""
        self.client.force_authenticate(user=self.user)
        project = Project.objects.create(organization=self.org)
        data = {
            "organization": reverse('organization-detail', args=(self.org.pk,)),
            "name": "new",
            "description": "string"
        }
        response = self.client.put(
            reverse('project-detail', args=(project.pk,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get().name, 'new')

    def test_partial_update(self):
        """projects_partial_update."""
        self.client.force_authenticate(user=self.user)
        project = Project.objects.create(organization=self.org)
        data = {
            "description": "New description."
        }
        response = self.client.patch(
            reverse('project-detail', args=(project.pk,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get().description, 'New description.')

    def test_delete(self):
        """projects_delete."""
        self.client.force_authenticate(user=self.user)
        project = Project.objects.create(organization=self.org)
        response = self.client.delete(
            reverse('project-detail', args=(project.pk,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_pagination_is_fifteen(self):
        """Test pagination is exactly fifteen."""
        self.client.force_authenticate(user=self.user)
        for x in range(30):
            Project.objects.create(organization=self.org)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data['results']), settings.REST_FRAMEWORK['PAGE_SIZE'])
