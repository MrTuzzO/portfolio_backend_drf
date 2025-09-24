from django.db import models

class STCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SkillAndTechnology(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='skills_and_technologies/logos/')
    category = models.ForeignKey(STCategory, on_delete=models.CASCADE, related_name='skills_and_technologies')

    def __str__(self):
        return self.name