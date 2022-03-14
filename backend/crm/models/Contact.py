"""Contact Model."""

# Django
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns

# CRM
from . import Organization


class Contact(models.Model):
    """Model representing a Contact"""
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=25)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.first_name

    def get_absolute_url(self):
        """Returns the url to access a particular Contact instance."""
        return reverse('contact-detail', args=[str(self.id)])
