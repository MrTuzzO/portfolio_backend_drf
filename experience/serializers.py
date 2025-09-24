from rest_framework import serializers
from .models import WorkExperience


class WorkExperienceSerializer(serializers.ModelSerializer):
    technologies = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = WorkExperience
        fields = [
            'id', 'designation', 'organization', 'starting_date', 'end_date',
            'location', 'work_type', 'employment_type', 'description', 
            'technologies', 'company_website'
        ]