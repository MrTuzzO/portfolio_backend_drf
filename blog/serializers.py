from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'featured_image', 'content', 
            'excerpt', 'author', 'published_date', 'updated_date'
        ]


class BlogListSerializer(serializers.ModelSerializer):
    """Simplified serializer for blog list view"""
    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'featured_image', 'excerpt', 
            'author', 'published_date'
        ]