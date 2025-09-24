from rest_framework import serializers
from .models import Project, ProjectCategory


class ProjectCategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = ProjectCategory
        fields = ['id', 'name']


class ProjectListSerializer(serializers.ModelSerializer):
    """Simplified serializer for project list view"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    technologies = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'short_description', 'category_name', 
            'featured_image', 'live_link', 'repo_link', 'technologies'
        ]


class ProjectDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for project detail view"""
    category = ProjectCategorySerializer(read_only=True)
    technologies = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'short_description', 'detailed_description',
            'category', 'featured_image', 'live_link', 'repo_link', 'technologies'
        ]