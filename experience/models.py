from django.db import models
from ckeditor.fields import RichTextField
from skills_and_technology.models import SkillAndTechnology

WORK_TYPE_CHOICES = (
    ('onsite', 'Onsite'),
    ('remote', 'Remote'),
    ('hybrid', 'Hybrid'),
)

EMPLOYMENT_TYPE_CHOICES = (
    ('full-time', 'Full-time'),
    ('part-time', 'Part-time'),
    ('contract', 'Contract'),
    ('internship', 'Internship'),
    ('freelance', 'Freelance'),
)


class WorkExperience(models.Model):
    designation = models.CharField(max_length=100, help_text="Job title/position")
    organization = models.CharField(max_length=100, help_text="Company/Organization name")
    starting_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank for current position")
    location = models.CharField(max_length=128, help_text="City, Country")
    work_type = models.CharField(max_length=10, choices=WORK_TYPE_CHOICES, default='onsite')
    employment_type = models.CharField(max_length=15, choices=EMPLOYMENT_TYPE_CHOICES, default='full-time')
    description = RichTextField(help_text="Job responsibilities and achievements")
    technologies = models.ManyToManyField(SkillAndTechnology, blank=True, related_name='work_experiences')
    company_website = models.URLField(blank=True, null=True)
    
    class Meta:
        ordering = ['-starting_date']
        verbose_name = 'Work Experience'
        verbose_name_plural = 'Work Experiences'
    
    def __str__(self):
        return f"{self.designation} at {self.organization}"

