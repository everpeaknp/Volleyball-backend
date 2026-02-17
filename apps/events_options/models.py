from django.db import models
from apps.core.models import PublishableModel, SEOFields

class EventsPage(PublishableModel, SEOFields):
    class Meta:
        verbose_name = "Events Page"
        verbose_name_plural = "Events Pages"

    def __str__(self):
        return f"Events Page ({self.status})"

class EventsHero(models.Model):
    page = models.OneToOneField(EventsPage, on_delete=models.CASCADE, related_name='hero', null=True, blank=True)
    image = models.ImageField(upload_to='images/events/hero/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Hero Image URL (CDN)")
    title_ne = models.CharField(max_length=200, verbose_name="Hero Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Hero Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Hero Title (DE)")
    text_ne = models.TextField(verbose_name="Hero Text (NE)")
    text_en = models.TextField(verbose_name="Hero Text (EN)")
    text_de = models.TextField(verbose_name="Hero Text (DE)")

    class Meta:
        verbose_name = "Events Hero"

class EventsSettings(models.Model):
    page = models.OneToOneField(EventsPage, on_delete=models.CASCADE, related_name='settings', null=True, blank=True)
    
    upcoming_title_ne = models.CharField(max_length=200, default="आगामी कार्यक्रमहरू")
    upcoming_title_en = models.CharField(max_length=200, default="Upcoming Events")
    upcoming_title_de = models.CharField(max_length=200, default="Kommende Veranstaltungen")
    
    past_title_ne = models.CharField(max_length=200, default="विगतका कार्यक्रमहरू")
    past_title_en = models.CharField(max_length=200, default="Past Events")
    past_title_de = models.CharField(max_length=200, default="Vergangene Veranstaltungen")
    
    register_btn_ne = models.CharField(max_length=100, default="दर्ता गर्नुहोस्")
    register_btn_en = models.CharField(max_length=100, default="Register")
    register_btn_de = models.CharField(max_length=100, default="Registrieren")
    
    label_upcoming_ne = models.CharField(max_length=100, default="आगामी")
    label_upcoming_en = models.CharField(max_length=100, default="Upcoming")
    label_upcoming_de = models.CharField(max_length=100, default="Kommende")
    
    label_past_ne = models.CharField(max_length=100, default="विगत")
    label_past_en = models.CharField(max_length=100, default="Past")
    label_past_de = models.CharField(max_length=100, default="Vergangene")

    class Meta:
        verbose_name = "Events Labels & Settings"

class Event(models.Model):
    page = models.ForeignKey(EventsPage, on_delete=models.CASCADE, related_name='events', null=True, blank=True)
    title_ne = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_de = models.CharField(max_length=200)
    
    description_ne = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_de = models.TextField(blank=True)
    
    date_text_ne = models.CharField(max_length=100, help_text="e.g. मार्च १५, २०२६")
    date_text_en = models.CharField(max_length=100, help_text="e.g. March 15, 2026")
    date_text_de = models.CharField(max_length=100, help_text="e.g. 15. März 2026")
    
    time = models.CharField(max_length=100, blank=True, help_text="e.g. 10:00 AM")
    
    location_ne = models.CharField(max_length=200, blank=True)
    location_en = models.CharField(max_length=200, blank=True)
    location_de = models.CharField(max_length=200, blank=True)
    
    image = models.ImageField(upload_to='images/events/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Event Image URL")
    
    is_past = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Event"
        verbose_name_plural = "Events"

# Proxy Models for Step-by-Step Admin
class EventsPageProxy(EventsPage):
    class Meta:
        proxy = True
        verbose_name = "01: Main Settings"
        verbose_name_plural = "01: Main Settings"

class EventsHeroProxy(EventsPage):
    class Meta:
        proxy = True
        verbose_name = "02: Hero Section"
        verbose_name_plural = "02: Hero Section"

class EventsManagementProxy(EventsPage):
    class Meta:
        proxy = True
        verbose_name = "03: Events Management"
        verbose_name_plural = "03: Events Management"

class EventsLabelsProxy(EventsPage):
    class Meta:
        proxy = True
        verbose_name = "04: Labels & Settings"
        verbose_name_plural = "04: Labels & Settings"
