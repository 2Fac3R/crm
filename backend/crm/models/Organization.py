"""Organization Model."""

# Django
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns


class Organization(models.Model):
    """Model representing a Organization"""
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=25)
    
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular Organization instance."""
        return reverse('organization-detail', args=[str(self.id)])
