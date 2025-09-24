from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from skills_and_technology.models import SkillAndTechnology

class ProjectCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=128)
    short_description = models.TextField()
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='projects')
    featured_image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    detailed_description = RichTextUploadingField()
    live_link = models.URLField(blank=True, null=True)
    repo_link = models.URLField(blank=True, null=True)
    technologies = models.ManyToManyField(SkillAndTechnology, blank=True, related_name='projects')

    def __str__(self):
        return self.title
