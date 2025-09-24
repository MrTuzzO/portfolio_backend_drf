from django.contrib import admin
from django.utils.html import format_html
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'result', 'location']
    list_filter = ['start_date', 'end_date', 'location']
    search_fields = ['degree', 'institution', 'location']
    date_hierarchy = 'start_date'
    ordering = ['-start_date']
    
    fieldsets = (
        ('Institution Information', {
            'fields': ('institution', 'location')
        }),
        ('Academic Details', {
            'fields': ('degree', 'result')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date'),
            'description': 'Leave end date blank if currently studying'
        }),
        ('Additional Information', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
    )
    