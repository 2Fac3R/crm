"""Project Model."""

# Django
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns

# CRM
from . import Organization


class Project(models.Model):
    """Model representing a Project"""
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular Project instance."""
        return reverse('project-detail', args=[str(self.id)])
