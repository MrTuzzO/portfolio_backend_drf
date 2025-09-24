from django.contrib import admin
from django.utils.html import format_html
from .models import SiteContent, SocialLink


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    """
    Admin for singleton SiteContent model
    """
    list_display = ['name', 'designation', 'email', 'profile_preview']
    filter_horizontal = ['social_links']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'designation', 'email', 'mobile', 'address')
        }),
        ('Profile Content', {
            'fields': ('profile_image', 'short_bio', 'about_me', 'about_me_img')
        }),
        ('Footer & Links', {
            'fields': ('footer_description', 'footer_copyright', 'resume_link')
        }),
        ('Social Media', {
            'fields': ('social_links',)
        }),
    )
    
    def profile_preview(self, obj):
        """Display profile image preview"""
        if obj.profile_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 50%; object-fit: cover;" />',
                obj.profile_image.url
            )
        return format_html('<span style="color: gray;">No image</span>')
    
    profile_preview.short_description = 'Profile Image'
    
    def has_add_permission(self, request):
        """Prevent adding multiple instances"""
        if SiteContent.objects.exists():
            return False
        return super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of the singleton instance"""
        return False


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'link_preview']
    search_fields = ['platform']
    ordering = ['platform']
    
    def link_preview(self, obj):
        """Display clickable link"""
        return format_html(
            '<a href="{}" target="_blank" style="color: blue;">🔗 View</a>',
            obj.url
        )
    
    link_preview.short_description = 'Link'
