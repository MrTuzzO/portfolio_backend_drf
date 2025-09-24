from django.contrib import admin
from django.utils.html import format_html
from .models import Certification


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuing_organization', 'issue_date']
    list_filter = ['issuing_organization', 'issue_date']
    search_fields = ['name', 'issuing_organization', 'credential_id']
    date_hierarchy = 'issue_date'
    ordering = ['-issue_date']
    
    fieldsets = (
        ('Certification Information', {
            'fields': ('name', 'issuing_organization', 'issue_date')
        }),
        ('Credential Details', {
            'fields': ('credential_id', 'credential_url'),
            'description': 'Optional credential verification details'
        }),
    )