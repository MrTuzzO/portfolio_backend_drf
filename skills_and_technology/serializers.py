from rest_framework import serializers
from .models import STCategory, SkillAndTechnology


class STCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = STCategory
        fields = '__all__'


class SkillAndTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillAndTechnology
        fields = '__all__'