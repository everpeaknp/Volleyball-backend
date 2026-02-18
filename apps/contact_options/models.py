from django.db import models
from apps.core.models import PublishableModel, SEOFields

class ContactPage(PublishableModel, SEOFields):
    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Pages"

    def __str__(self):
        return f"Contact Page ({self.status})"

class ContactHero(models.Model):
    page = models.OneToOneField(ContactPage, on_delete=models.CASCADE, related_name='hero')
    image = models.ImageField(upload_to='images/contact/hero/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Hero Image URL (CDN)")
    title_ne = models.CharField(max_length=200, verbose_name="Hero Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Hero Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Hero Title (DE)")
    subtitle_ne = models.CharField(max_length=200, verbose_name="Hero Subtitle (NE)")
    subtitle_en = models.CharField(max_length=200, verbose_name="Hero Subtitle (EN)")
    subtitle_de = models.CharField(max_length=200, verbose_name="Hero Subtitle (DE)")

    class Meta:
        verbose_name = "Contact Hero"

class ContactInfo(models.Model):
    page = models.ForeignKey(ContactPage, on_delete=models.CASCADE, related_name='contact_methods')
    icon = models.CharField(max_length=50, help_text="Lucide icon name (e.g. MapPin, Phone, Mail)")
    label_ne = models.CharField(max_length=100)
    label_en = models.CharField(max_length=100)
    label_de = models.CharField(max_length=100)
    value = models.CharField(max_length=255) # Values usually don't need translations (address/phone/email)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

class ContactSocial(models.Model):
    page = models.ForeignKey(ContactPage, on_delete=models.CASCADE, related_name='social_links')
    platform = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.CharField(max_length=50, help_text="Lucide icon name (e.g. Facebook, Instagram, Twitter)")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Social Media Link"
        verbose_name_plural = "Social Media Links"

class ContactSettings(models.Model):
    page = models.OneToOneField(ContactPage, on_delete=models.CASCADE, related_name='settings')
    
    # Form Labels & Settings
    form_title_ne = models.CharField(max_length=200, default="सन्देश पठाउनुहोस्")
    form_title_en = models.CharField(max_length=200, default="Send Message")
    form_title_de = models.CharField(max_length=200, default="Nachricht senden")
    
    label_name_ne = models.CharField(max_length=100, default="नाम")
    label_name_en = models.CharField(max_length=100, default="Name")
    label_name_de = models.CharField(max_length=100, default="Name")
    
    label_email_ne = models.CharField(max_length=100, default="इमेल")
    label_email_en = models.CharField(max_length=100, default="Email")
    label_email_de = models.CharField(max_length=100, default="E-Mail")
    
    label_subject_ne = models.CharField(max_length=100, default="विषय")
    label_subject_en = models.CharField(max_length=100, default="Subject")
    label_subject_de = models.CharField(max_length=100, default="Betreff")
    
    label_message_ne = models.CharField(max_length=100, default="सन्देश")
    label_message_en = models.CharField(max_length=100, default="Message")
    label_message_de = models.CharField(max_length=100, default="Nachricht")
    
    label_submit_ne = models.CharField(max_length=100, default="पठाउनुहोस्")
    label_submit_en = models.CharField(max_length=100, default="Send")
    label_submit_de = models.CharField(max_length=100, default="Senden")

    # Titles for Info sections
    info_section_title_ne = models.CharField(max_length=200, default="सम्पर्क जानकारी")
    info_section_title_en = models.CharField(max_length=200, default="Contact Information")
    info_section_title_de = models.CharField(max_length=200, default="Kontaktinformationen")
    
    social_section_title_ne = models.CharField(max_length=200, default="सामाजिक सञ्जाल")
    social_section_title_en = models.CharField(max_length=200, default="Social Media")
    social_section_title_de = models.CharField(max_length=200, default="Soziale Medien")

    class Meta:
        verbose_name = "Contact Labels & Settings"

class ContactSubmission(models.Model):
    """Model to store contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    # Auto fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"

# Proxy Models for Step-by-Step Admin
class ContactPageProxy(ContactPage):
    class Meta:
        proxy = True
        verbose_name = "01: Main Settings"
        verbose_name_plural = "01: Main Settings"

class ContactHeroProxy(ContactPage):
    class Meta:
        proxy = True
        verbose_name = "02: Hero Section"
        verbose_name_plural = "02: Hero Section"

class ContactInfoProxy(ContactPage):
    class Meta:
        proxy = True
        verbose_name = "03: Contact Methods"
        verbose_name_plural = "03: Contact Methods"

class ContactSocialProxy(ContactPage):
    class Meta:
        proxy = True
        verbose_name = "04: Social Links"
        verbose_name_plural = "04: Social Links"

class ContactLabelsProxy(ContactPage):
    class Meta:
        proxy = True
        verbose_name = "05: Labels & Settings"
        verbose_name_plural = "05: Labels & Settings"
