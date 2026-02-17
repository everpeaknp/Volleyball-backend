from django.db import models
from apps.core.models import PublishableModel, SEOFields

# --- Other Pages Models ---

# Note: TeamPage (04), MembershipPage (05), EventsPage (06), and NewsPage (07) 
# have been moved to dedicated modular apps.

# GalleryPage (08) and ContactPage (09) have been moved to dedicated modular apps.

class NoticePage(PublishableModel, SEOFields):
    hero_title_ne = models.CharField(max_length=200)
    hero_title_en = models.CharField(max_length=200)
    hero_title_de = models.CharField(max_length=200)
    hero_text_ne = models.TextField()
    hero_text_en = models.TextField()
    hero_text_de = models.TextField()
    cta_title_ne = models.CharField(max_length=200)
    cta_title_en = models.CharField(max_length=200)
    cta_title_de = models.CharField(max_length=200)
    cta_text_ne = models.TextField()
    cta_text_en = models.TextField()
    cta_text_de = models.TextField()
    cta_button_text_ne = models.CharField(max_length=100)
    cta_button_text_en = models.CharField(max_length=100)
    cta_button_text_de = models.CharField(max_length=100)
