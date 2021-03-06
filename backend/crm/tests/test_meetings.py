# Django
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

# Django Rest Framework
from rest_framework.test import APITestCase
from rest_framework import status

# CRM
from ..models import Organization, Project, Contact, Meeting


class MeetingTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.org = Organization.objects.create()
        self.project = Project.objects.create(organization=self.org)
        self.contact = Contact.objects.create(organization=self.org)
        self.url = reverse('meeting-list')

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
        meeting = Meeting.objects.create(
            project=self.project, contact=self.contact,
            title="string", description="string", date="2019-08-24T14:15:22Z")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, meeting)

    def test_create(self):
        """meetings_create."""
        self.client.force_authenticate(user=self.user)
        data = {
            "project":  reverse('project-detail', args=(self.project.pk,)),
            "contact":  reverse('contact-detail', args=(self.contact.pk,)),
            "title": "string",
            "description": "string",
            "date": "2019-08-24T14:15:22Z"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Meeting.objects.count(), 1)
        self.assertEqual(Meeting.objects.get().title, 'string')

    def test_read(self):
        """meetings_read."""
        self.client.force_authenticate(user=self.user)
        meeting = Meeting.objects.create(
            project=self.project, contact=self.contact,
            title="string", description="string", date="2019-08-24T14:15:22Z")
        response = self.client.get(
            reverse('meeting-detail', args=(meeting.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, meeting)

    def test_update(self):
        """meetings_update."""
        self.client.force_authenticate(user=self.user)
        meeting = Meeting.objects.create(
            project=self.project, contact=self.contact,
            title="string", description="string", date="2019-08-24T14:15:22Z")
        data = {
            "project":  reverse('project-detail', args=(self.project.pk,)),
            "contact":  reverse('contact-detail', args=(self.contact.pk,)),
            "title": "new",
            "description": "string",
            "date": "2019-08-24T14:15:22Z"
        }
        response = self.client.put(
            reverse('meeting-detail', args=(meeting.pk,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Meeting.objects.count(), 1)
        self.assertEqual(Meeting.objects.get().title, 'new')

    def test_partial_update(self):
        """meetings_partial_update."""
        self.client.force_authenticate(user=self.user)
        meeting = Meeting.objects.create(
            project=self.project, contact=self.contact,
            title="string", description="string", date="2019-08-24T14:15:22Z")
        data = {
            "title": "New title"
        }
        response = self.client.patch(
            reverse('meeting-detail', args=(meeting.pk,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Meeting.objects.count(), 1)
        self.assertEqual(Meeting.objects.get().title, 'New title')

    def test_delete(self):
        """meetings_delete."""
        self.client.force_authenticate(user=self.user)
        meeting = Meeting.objects.create(
            project=self.project, contact=self.contact,
            title="string", description="string", date="2019-08-24T14:15:22Z")
        response = self.client.delete(
            reverse('meeting-detail', args=(meeting.pk,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_pagination_is_fifteen(self):
        """Test pagination is exactly fifteen."""
        self.client.force_authenticate(user=self.user)
        for x in range(30):
            Meeting.objects.create(
                project=self.project,
                contact=self.contact,
                title="string",
                description="string",
                date="2019-08-24T14:15:22Z"
            )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data['results']), settings.REST_FRAMEWORK['PAGE_SIZE'])

    def test_search(self):
        """Test searching functionality."""
        self.client.force_authenticate(user=self.user)
        Meeting.objects.create(
            project=self.project,
            contact=self.contact,
            title="asd",
            description="string",
            date="2019-08-24T14:15:22Z"
        )
        meetings = Meeting.objects.filter(title='asd')
        response = self.client.get(self.url, {'search': 'asd'})
        self.assertEqual(len(response.data['results']), meetings.count())
