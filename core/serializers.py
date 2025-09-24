from rest_framework import serializers
from .models import SiteContent, SocialLink


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['id', 'platform', 'url']


class SiteContentSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True, read_only=True)
    
    class Meta:
        model = SiteContent
        fields = ['name', 'profile_image', 'designation', 'short_bio', 
            'about_me', 'about_me_img', 'footer_description', 
            'footer_copyright', 'social_links', 'email', 'mobile', 
            'address', 'resume_link'
        ]