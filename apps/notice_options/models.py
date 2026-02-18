from django.db import models
from apps.core.models import PublishableModel, SEOFields

class NoticePage(PublishableModel, SEOFields):
    class Meta:
        verbose_name = "04: Notices Management"
        verbose_name_plural = "04: Notices Management"

    def __str__(self):
        return f"Notice Page ({self.status})"

class NoticeHero(models.Model):
    page = models.OneToOneField(NoticePage, on_delete=models.CASCADE, related_name='hero', null=True, blank=True)
    title_ne = models.CharField(max_length=200, verbose_name="Hero Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Hero Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Hero Title (DE)")
    text_ne = models.TextField(verbose_name="Hero Text (NE)")
    text_en = models.TextField(verbose_name="Hero Text (EN)")
    text_de = models.TextField(verbose_name="Hero Text (DE)")

    class Meta:
        verbose_name = "Notice Hero"

class NoticeCTA(models.Model):
    page = models.OneToOneField(NoticePage, on_delete=models.CASCADE, related_name='cta', null=True, blank=True)
    
    title_ne = models.CharField(max_length=200, default="सूचना प्राप्त गर्नुहोस्")
    title_en = models.CharField(max_length=200, default="Get Notifications")
    title_de = models.CharField(max_length=200, default="Benachrichtigungen erhalten")
    
    text_ne = models.TextField(default="नयाँ सूचना आएपछि इमेलमा जानकारी पाउनुहोस्।")
    text_en = models.TextField(default="Get notified via email when new notices are published.")
    text_de = models.TextField(default="Lassen Sie sich per E-Mail benachrichtigen, wenn neue Mitteilungen veröffentlicht werden.")
    
    button_text_ne = models.CharField(max_length=100, default="सम्पर्क गर्नुहोस्")
    button_text_en = models.CharField(max_length=100, default="Contact Us")
    button_text_de = models.CharField(max_length=100, default="Kontaktieren Sie uns")
    
    button_icon = models.CharField(max_length=50, default="ChevronRight", help_text="Lucide icon name")

    class Meta:
        verbose_name = "Notice CTA Section"

class NoticeCategory(models.Model):
    name_ne = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "03: Notice Categories"
        verbose_name_plural = "03: Notice Categories"

    def __str__(self):
        return self.name_en

class Notice(models.Model):
    page = models.ForeignKey(NoticePage, on_delete=models.CASCADE, related_name='notices', null=True, blank=True)
    title_ne = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_de = models.CharField(max_length=200)
    
    content_ne = models.TextField()
    content_en = models.TextField()
    content_de = models.TextField()
    
    category = models.ForeignKey(NoticeCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='notices')
    
    date_text_ne = models.CharField(max_length=100, help_text="e.g. फेब्रुअरी २५, २०२६")
    date_text_en = models.CharField(max_length=100, help_text="e.g. February 25, 2026")
    date_text_de = models.CharField(max_length=100, help_text="e.g. 25. Februar 2026")
    
    icon = models.CharField(max_length=50, default="Bell", help_text="Lucide icon name")
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Notice"
        verbose_name_plural = "Notices"

    def __str__(self):
        return self.title_en

# Proxy Models for Clean Step-by-Step Admin
class NoticePageProxy(NoticePage):
    class Meta:
        proxy = True
        verbose_name = "01: Main Settings"
        verbose_name_plural = "01: Main Settings"

class NoticeHeroProxy(NoticePage):
    class Meta:
        proxy = True
        verbose_name = "02: Hero Section"
        verbose_name_plural = "02: Hero Section"

# Categories and Notices get their own clean admin sections
# NoticeCategoryAdmin will be "03: Notice Categories" 
# NoticeManagementAdmin (NoticePage with inlines) will be "04: Notices Management"
