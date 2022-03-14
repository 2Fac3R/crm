"""Admin Site."""

# Django
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Catalog
from .models import Organization, Project, Contact, Meeting


# Unregister the provided model admin
admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Register our own model admin, based on the default UserAdmin."""
    pass


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone')
    list_filter = ('country', 'city')
    search_fields = ('name', 'phone')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization')
    list_filter = ['organization',]
    search_fields = ('name', 'description')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('city', 'first_name', 'organization')
    list_filter = ('country', 'organization', )
    search_fields = ('first_name', 'last_name', 'organization')

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'project')
    list_filter = ('contact', 'date', 'project')
    search_fields = ('contact', 'title', 'project')
