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
    list_filter = ['organization', ]
    search_fields = ('name', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'organization', 'email', 'phone')
    list_filter = ('organization', 'country', 'city')
    search_fields = ('first_name', 'last_name', 'email', 'phone')


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'project')
    list_filter = ('contact', 'date', 'project')
    search_fields = ('title', 'date')
