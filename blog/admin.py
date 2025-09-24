from django.contrib import admin
from django.utils.html import format_html
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_status', 'published_date', 'featured_image_preview', 'is_published']
    list_filter = ['is_published', 'published_date', 'author']
    search_fields = ['title', 'content', 'author']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ['-published_date']
    list_editable = ['is_published']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author')
        }),
        ('Content', {
            'fields': ('excerpt', 'content', 'featured_image')
        }),
        ('Publishing', {
            'fields': ('is_published',),
            'description': 'Control blog post visibility'
        }),
    )
    
    def published_status(self, obj):
        """Display publication status with color coding"""
        if obj.is_published:
            return format_html(
                '<span style="color: green; font-weight: bold;">✓ Published</span>'
            )
        return format_html(
            '<span style="color: red; font-weight: bold;">✗ Draft</span>'
        )
    
    published_status.short_description = 'Status'
    
    def featured_image_preview(self, obj):
        """Display featured image preview"""
        if obj.featured_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 4px; object-fit: cover;" />',
                obj.featured_image.url
            )
        return format_html('<span style="color: gray;">No image</span>')
    
    featured_image_preview.short_description = 'Image'
