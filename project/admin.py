from django.contrib import admin
from django.utils.html import format_html
from .models import Project, ProjectCategory


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'projects_count']
    search_fields = ['name']
    ordering = ['name']
    
    def projects_count(self, obj):
        """Display the number of projects in this category"""
        count = obj.projects.count()
        if count > 0:
            return format_html(
                '<span style="color: green; font-weight: bold;">{} project{}</span>',
                count, 's' if count > 1 else ''
            )
        return format_html('<span style="color: red;">No projects</span>')
    
    projects_count.short_description = 'Projects Count'


class ProjectInline(admin.TabularInline):
    """Inline admin for projects in category admin"""
    model = Project
    extra = 1
    fields = ['title', 'short_description']
    readonly_fields = []


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'links_status', 'featured_image_preview', 'tech_count']
    list_filter = ['category']
    search_fields = ['title', 'short_description', 'category__name']
    filter_horizontal = ['technologies']
    ordering = ['-id']
    list_select_related = ['category']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'category', 'short_description')
        }),
        ('Content', {
            'fields': ('detailed_description', 'featured_image')
        }),
        ('Links', {
            'fields': ('live_link', 'repo_link')
        }),
        ('Technologies', {
            'fields': ('technologies',)
        }),
    )
    
    def links_status(self, obj):
        """Display link availability status"""
        links = []
        if obj.live_link:
            links.append('<span style="color: green;">🔗 Live</span>')
        if obj.repo_link:
            links.append('<span style="color: blue;">📁 Repo</span>')
        
        if links:
            return format_html(' | '.join(links))
        return format_html('<span style="color: red;">No links</span>')
    
    links_status.short_description = 'Links'
    
    def featured_image_preview(self, obj):
        """Display featured image preview"""
        if obj.featured_image:
            return format_html(
                '<img src="{}" width="40" height="40" style="border-radius: 4px; object-fit: cover;" />',
                obj.featured_image.url
            )
        return format_html('<span style="color: gray;">No image</span>')
    
    featured_image_preview.short_description = 'Image'
    
    def tech_count(self, obj):
        """Display technology count"""
        count = obj.technologies.count()
        return format_html(
            '<span style="background-color: #f0f8ff; padding: 2px 6px; border-radius: 3px; font-size: 11px;">{} tech{}</span>',
            count, 's' if count != 1 else ''
        )
    
    tech_count.short_description = 'Technologies'


# Add inline to category admin
ProjectCategoryAdmin.inlines = [ProjectInline]
