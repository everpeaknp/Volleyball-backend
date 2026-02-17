from django.db import models
from apps.core.models import PublishableModel

class NavigationSettings(PublishableModel):
    """Singleton model for global navigation settings"""
    logo = models.ImageField(upload_to='logos/navbar/', null=True, blank=True)
    # Brand Name (Trilingual or Universal? Frontend implies one string parts, but let's support trilingual just in case or just parts)
    brand_name_main_ne = models.CharField(max_length=100, default="Nepal Volleyball Club")
    brand_name_main_en = models.CharField(max_length=100, default="Nepal Volleyball Club")
    brand_name_main_de = models.CharField(max_length=100, default="Nepal Volleyball Club")
    
    brand_name_secondary_ne = models.CharField(max_length=100, default="Hamburg e.V.")
    brand_name_secondary_en = models.CharField(max_length=100, default="Hamburg e.V.")
    brand_name_secondary_de = models.CharField(max_length=100, default="Hamburg e.V.")

    def __str__(self):
        return f"Navigation Settings"
    
    class Meta:
        verbose_name = "Navigation Settings"
        verbose_name_plural = "Navigation Settings"

class NavigationItem(models.Model):
    order = models.PositiveIntegerField(default=0)
    href = models.CharField(max_length=200)
    
    label_ne = models.CharField(max_length=100)
    label_en = models.CharField(max_length=100)
    label_de = models.CharField(max_length=100)
    
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Navigation Item"
        verbose_name_plural = "Navigation Items"
    
    def __str__(self):
        return self.label_en

class FooterSettings(PublishableModel):
    """Singleton model for footer content"""
    # Brand
    logo = models.ImageField(upload_to='logos/footer/', null=True, blank=True)
    brand_name_main_ne = models.CharField(max_length=100, default="Nepal Volleyball Club")
    brand_name_main_en = models.CharField(max_length=100, default="Nepal Volleyball Club")
    brand_name_main_de = models.CharField(max_length=100, default="Nepal Volleyball Club")

    brand_name_secondary_ne = models.CharField(max_length=100, default="Hamburg e.V.")
    brand_name_secondary_en = models.CharField(max_length=100, default="Hamburg e.V.")
    brand_name_secondary_de = models.CharField(max_length=100, default="Hamburg e.V.")

    # Description
    description_ne = models.TextField(blank=True, verbose_name="Description (NE)")
    description_en = models.TextField(blank=True, verbose_name="Description (EN)")
    description_de = models.TextField(blank=True, verbose_name="Description (DE)")
    
    # Social Links
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    
    # Section Headers
    quick_links_title_ne = models.CharField(max_length=100, default="Quick Links")
    quick_links_title_en = models.CharField(max_length=100, default="Quick Links")
    quick_links_title_de = models.CharField(max_length=100, default="Quick Links")
    
    contact_info_title_ne = models.CharField(max_length=100, default="Contact Us")
    contact_info_title_en = models.CharField(max_length=100, default="Contact Us")
    contact_info_title_de = models.CharField(max_length=100, default="Kontakt")

    # Content
    address_ne = models.CharField(max_length=200, blank=True)
    address_en = models.CharField(max_length=200, blank=True)
    address_de = models.CharField(max_length=200, blank=True)
    
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    registered_info = models.CharField(max_length=100, blank=True)
    
    # Membership
    membership_title_ne = models.CharField(max_length=100, default="Membership")
    membership_title_en = models.CharField(max_length=100, default="Membership")
    membership_title_de = models.CharField(max_length=100, default="Mitgliedschaft")
    
    membership_description_ne = models.TextField(blank=True)
    membership_description_en = models.TextField(blank=True)
    membership_description_de = models.TextField(blank=True)
    
    membership_button_text_ne = models.CharField(max_length=50, default="Join Now")
    membership_button_text_en = models.CharField(max_length=50, default="Join Now")
    membership_button_text_de = models.CharField(max_length=50, default="Jetzt beitreten")
    
    # Copyright
    copyright_text_ne = models.CharField(max_length=200, help_text="Use [year] placeholder")
    copyright_text_en = models.CharField(max_length=200, help_text="Use [year] placeholder")
    copyright_text_de = models.CharField(max_length=200, help_text="Use [year] placeholder")
    
    # Legal Links Labels
    privacy_label_ne = models.CharField(max_length=100, default="Privacy Policy")
    privacy_label_en = models.CharField(max_length=100, default="Privacy Policy")
    privacy_label_de = models.CharField(max_length=100, default="Datenschutz")
    
    terms_label_ne = models.CharField(max_length=100, default="Terms of Service")
    terms_label_en = models.CharField(max_length=100, default="Terms of Service")
    terms_label_de = models.CharField(max_length=100, default="AGB")

    class Meta:
        verbose_name = "Footer Settings"
        verbose_name_plural = "Footer Settings"

class FooterLink(models.Model):
    footer = models.ForeignKey(FooterSettings, on_delete=models.CASCADE, related_name='quick_links')
    label_ne = models.CharField(max_length=100)
    label_en = models.CharField(max_length=100)
    label_de = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Footer Quick Link"
        verbose_name_plural = "Footer Quick Links"
    
    def __str__(self):
        return self.label_en
