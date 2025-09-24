from django.db import models
from django.core.exceptions import ValidationError


class SiteContent(models.Model):
    name = models.CharField(max_length=100, default="Portfolio Site")
    profile_image = models.ImageField(upload_to='profile_images/')
    designation = models.CharField(max_length=100)
    short_bio = models.TextField()
    about_me = models.TextField()
    about_me_img = models.ImageField(upload_to='about_images/')
    footer_description = models.CharField(max_length=255, blank=True)
    footer_copyright = models.CharField(max_length=255, blank=True)
    social_links = models.ManyToManyField('SocialLink', blank=True, related_name='site_contents')
    email = models.EmailField()
    mobile = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=128, blank=True)
    resume_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Site Content'
        verbose_name_plural = 'Site Content'

    def save(self, *args, **kwargs):
        # Ensure only one instance exists (Singleton)
        if not self.pk and SiteContent.objects.exists():
            raise ValidationError('Only one SiteContent instance is allowed.')
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        """Get the singleton instance, create if doesn't exist"""
        instance, created = cls.objects.get_or_create(
            pk=1,
            defaults={
                'name': 'Portfolio Site',
                'designation': 'Developer',
                'short_bio': 'Welcome to my portfolio',
                'about_me': 'Tell us about yourself',
                'email': 'contact@example.com'
            }
        )
        return instance

    def __str__(self):
        return f"Site Content - {self.name}"
    

class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()
    
    def __str__(self):
        return self.platform