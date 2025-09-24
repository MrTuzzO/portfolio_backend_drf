from django.contrib import admin
from .models import STCategory, SkillAndTechnology


@admin.register(STCategory)
class STCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(SkillAndTechnology)
class SkillAndTechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    search_fields = ['name']
