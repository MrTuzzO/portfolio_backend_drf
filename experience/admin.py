from django.contrib import admin
from django.utils.html import format_html
from .models import WorkExperience


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['designation', 'organization', 'work_type', 'employment_type']
    list_filter = ['work_type', 'employment_type', 'starting_date']
    search_fields = ['designation', 'organization', 'location']
    filter_horizontal = ['technologies']
    date_hierarchy = 'starting_date'
    ordering = ['-starting_date']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('designation', 'organization', 'location', 'company_website')
        }),
        ('Employment Details', {
            'fields': ('work_type', 'employment_type')
        }),
        ('Duration', {
            'fields': ('starting_date', 'end_date'),
            'description': 'Leave end date blank for current position'
        }),
        ('Job Description', {
            'fields': ('description',)
        }),
        ('Technologies Used', {
            'fields': ('technologies',)
        }),
    )
    
