"""Meeting Model."""

# Django
from django.db import models
from django.urls import reverse # To generate URLS by reversing URL patterns

from . import Project, Contact


class Meeting(models.Model):
    """Model representing a Meeting"""
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(null=False, blank=False)
    
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular Meeting instance."""
        return reverse('meeting-detail', args=[str(self.id)])
