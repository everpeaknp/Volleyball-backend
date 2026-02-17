from django.db import models
from django.utils.translation import gettext_lazy as _

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class PublishableModel(TimeStampedModel):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    published_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        abstract = True

class SEOFields(models.Model):
    # Meta Title
    meta_title_ne = models.CharField(max_length=200, blank=True, verbose_name="Meta Title (NE)")
    meta_title_en = models.CharField(max_length=200, blank=True, verbose_name="Meta Title (EN)")
    meta_title_de = models.CharField(max_length=200, blank=True, verbose_name="Meta Title (DE)")
    
    # Meta Description
    meta_description_ne = models.TextField(blank=True, verbose_name="Meta Description (NE)")
    meta_description_en = models.TextField(blank=True, verbose_name="Meta Description (EN)")
    meta_description_de = models.TextField(blank=True, verbose_name="Meta Description (DE)")
    
    meta_keywords = models.CharField(max_length=500, blank=True, help_text="Comma separated")
    
    # OG
    og_title_ne = models.CharField(max_length=200, blank=True)
    og_title_en = models.CharField(max_length=200, blank=True)
    og_title_de = models.CharField(max_length=200, blank=True)
    
    og_description_ne = models.TextField(blank=True)
    og_description_en = models.TextField(blank=True)
    og_description_de = models.TextField(blank=True)
    
    og_image = models.ForeignKey('media.Media', on_delete=models.SET_NULL, null=True, blank=True, related_name='%(app_label)s_%(class)s_og_image')
    canonical_url = models.URLField(blank=True)
    
    class Meta:
        abstract = True

class GlobalStyles(models.Model):
    """Singleton model for global styling tokens"""
    # Brand Info
    brand_name_ne = models.CharField(max_length=200, default="Nepal Volleyball Club")
    brand_name_en = models.CharField(max_length=200, default="Nepal Volleyball Club")
    brand_name_de = models.CharField(max_length=200, default="Nepal Volleyball Club")
    
    brand_subtitle_ne = models.CharField(max_length=200, default="Hamburg e.V.")
    brand_subtitle_en = models.CharField(max_length=200, default="Hamburg e.V.")
    brand_subtitle_de = models.CharField(max_length=200, default="Hamburg e.V.")

    # Colors
    primary_500 = models.CharField(max_length=7, default='#DC143C', help_text="Main Crimson")
    primary_600 = models.CharField(max_length=7, default='#B01030', help_text="Hover Crimson")
    secondary_500 = models.CharField(max_length=7, default='#003893', help_text="Main Blue")
    accent_500 = models.CharField(max_length=7, default='#FFD700', help_text="Gold")
    
    # Patterns
    enable_nepal_pattern = models.BooleanField(default=True)
    enable_volleyball_pattern = models.BooleanField(default=True)
    nepal_pattern_svg = models.TextField(blank=True)
    volleyball_pattern_svg = models.TextField(blank=True)
    
    # Micro-interactions
    transition_duration = models.PositiveIntegerField(default=300, help_text="in ms")
    
    def __str__(self):
        return "Global Styles & Brand"

    class Meta:
        verbose_name = "Global Styles & Brand"
        verbose_name_plural = "Global Styles & Brand"
