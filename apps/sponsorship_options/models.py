from django.db import models
from apps.core.models import PublishableModel, SEOFields

class SponsorshipPage(PublishableModel, SEOFields):
    class Meta:
        verbose_name = "Sponsorship Page"
        verbose_name_plural = "Sponsorship Pages"

    def __str__(self):
        return f"Sponsorship Page ({self.status})"

class SponsorshipHero(models.Model):
    page = models.OneToOneField(SponsorshipPage, on_delete=models.CASCADE, related_name='hero', null=True, blank=True)
    image = models.ImageField(upload_to='images/sponsorship/hero/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Hero Image URL (CDN)")
    title_ne = models.CharField(max_length=200, verbose_name="Hero Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Hero Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Hero Title (DE)")
    text_ne = models.TextField(verbose_name="Hero Text (NE)")
    text_en = models.TextField(verbose_name="Hero Text (EN)")
    text_de = models.TextField(verbose_name="Hero Text (DE)")

    class Meta:
        verbose_name = "Sponsorship Hero"

class Sponsor(models.Model):
    page = models.ForeignKey(SponsorshipPage, on_delete=models.CASCADE, related_name='sponsors', null=True, blank=True)
    name_ne = models.CharField(max_length=200, verbose_name="Sponsor Name (NE)")
    name_en = models.CharField(max_length=200, verbose_name="Sponsor Name (EN)")
    name_de = models.CharField(max_length=200, verbose_name="Sponsor Name (DE)")
    logo = models.ImageField(upload_to='images/sponsorship/logos/')
    link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"

    def __str__(self):
        return f"{self.name_en}"

class SponsorshipFormSettings(models.Model):
    page = models.OneToOneField(SponsorshipPage, on_delete=models.CASCADE, related_name='form_settings', null=True, blank=True)
    title_ne = models.CharField(max_length=200, verbose_name="Form Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Form Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Form Title (DE)")
    text_ne = models.TextField(verbose_name="Form Text (NE)")
    text_en = models.TextField(verbose_name="Form Text (EN)")
    text_de = models.TextField(verbose_name="Form Text (DE)")
    
    success_title_ne = models.CharField(max_length=200, verbose_name="Success Title (NE)")
    success_title_en = models.CharField(max_length=200, verbose_name="Success Title (EN)")
    success_title_de = models.CharField(max_length=200, verbose_name="Success Title (DE)")
    success_text_ne = models.TextField(verbose_name="Success Text (NE)")
    success_text_en = models.TextField(verbose_name="Success Text (EN)")
    success_text_de = models.TextField(verbose_name="Success Text (DE)")

    # Form Labels (Standardized with membership but customized for sponsors)
    label_name_ne = models.CharField(max_length=100, default="पूरा नाम / संस्थाको नाम")
    label_name_en = models.CharField(max_length=100, default="Full Name / Company Name")
    label_name_de = models.CharField(max_length=100, default="Vollständiger Name / Firmenname")
    
    label_email_ne = models.CharField(max_length=100, default="ईमेल")
    label_email_en = models.CharField(max_length=100, default="Email Address")
    label_email_de = models.CharField(max_length=100, default="E-Mail-Adresse")
    
    label_phone_ne = models.CharField(max_length=100, default="फोन नम्बर")
    label_phone_en = models.CharField(max_length=100, default="Phone Number")
    label_phone_de = models.CharField(max_length=100, default="Telefonnummer")
    
    label_type_ne = models.CharField(max_length=100, default="प्रयोजन प्रकार")
    label_type_en = models.CharField(max_length=100, default="Sponsorship Type")
    label_type_de = models.CharField(max_length=100, default="Sponsoring-Typ")
    
    label_amount_ne = models.CharField(max_length=100, default="प्रयोजन रकम (€)")
    label_amount_en = models.CharField(max_length=100, default="Sponsorship Amount (€)")
    label_amount_de = models.CharField(max_length=100, default="Sponsoring-Betrag (€)")

    label_voucher_ne = models.CharField(max_length=100, default="बैंक भौचर फोटो")
    label_voucher_en = models.CharField(max_length=100, default="Bank Voucher Photo")
    label_voucher_de = models.CharField(max_length=100, default="Bankbeleg Foto")

    label_message_ne = models.CharField(max_length=100, default="सन्देश")
    label_message_en = models.CharField(max_length=100, default="Message")
    label_message_de = models.CharField(max_length=100, default="Nachricht")
    
    label_submit_ne = models.CharField(max_length=100, default="आवेदन पठाउनुहोस्")
    label_submit_en = models.CharField(max_length=100, default="Submit Application")
    label_submit_de = models.CharField(max_length=100, default="Antrag absenden")

    # Options
    options_type_ne = models.CharField(max_length=500, default="प्लेटिनम, गोल्ड, सिल्भर, अन्य")
    options_type_en = models.CharField(max_length=500, default="Platinum, Gold, Silver, Other")
    options_type_de = models.CharField(max_length=500, default="Platin, Gold, Silber, Sonstiges")

    class Meta:
        verbose_name = "Form Settings & Labels"

class SponsorshipApplication(models.Model):
    TYPE_CHOICES = [
        ('platinum', 'Platinum'),
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200, verbose_name="Full Name / Company Name")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    sponsorship_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bank_voucher = models.ImageField(upload_to='images/sponsorship/applications/vouchers/')
    message = models.TextField(blank=True, null=True)
    
    is_approved = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sponsorship Application"
        verbose_name_plural = "Sponsorship Applications"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.sponsorship_type}"

    def send_approval_email(self):
        from django.core.mail import send_mail
        from django.conf import settings
        try:
            send_mail(
                subject='Sponsorship Application Approved! - Nepal Volleyball Club Hamburg',
                message=f'Dear {self.name},\n\n'
                        f'We are pleased to inform you that your sponsorship application for Nepal Volleyball Club Hamburg e.V. has been approved!\n\n'
                        f'Thank you for your generous support. We look forward to a successful partnership. Our team will contact you shortly with the next steps regarding branding and collaboration.\n\n'
                        f'Best regards,\n'
                        f'Nepal Volleyball Club Hamburg e.V. Team',
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@nepalvolleyballhh.de'),
                recipient_list=[self.email],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Failed to send sponsorship approval email to {self.email}: {e}")

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = SponsorshipApplication.objects.get(pk=self.pk)
                if not old_instance.is_approved and self.is_approved:
                    self.send_approval_email()
            except SponsorshipApplication.DoesNotExist:
                pass
        super().save(*args, **kwargs)

# --- Proxy Models for Admin ---

class SponsorshipPageProxy(SponsorshipPage):
    class Meta:
        proxy = True
        app_label = 'sponsorship_options'
        verbose_name = '01: Main Settings'
        verbose_name_plural = '01: Main Settings'

class SponsorshipHeroProxy(SponsorshipPage):
    class Meta:
        proxy = True
        app_label = 'sponsorship_options'
        verbose_name = '02: Hero Section'
        verbose_name_plural = '02: Hero Section'

class SponsorsProxy(SponsorshipPage):
    class Meta:
        proxy = True
        app_label = 'sponsorship_options'
        verbose_name = '03: Current Sponsors'
        verbose_name_plural = '03: Current Sponsors'

class SponsorshipFormProxy(SponsorshipPage):
    class Meta:
        proxy = True
        app_label = 'sponsorship_options'
        verbose_name = '04: Form & Labels'
        verbose_name_plural = '04: Form & Labels'
