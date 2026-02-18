from django.db import models
from apps.core.models import PublishableModel, SEOFields

class MembershipPage(PublishableModel, SEOFields):
    class Meta:
        verbose_name = "Membership Page"
        verbose_name_plural = "Membership Pages"

    def __str__(self):
        return f"Membership Page ({self.status})"

class MembershipHero(models.Model):
    page = models.OneToOneField(MembershipPage, on_delete=models.CASCADE, related_name='hero', null=True, blank=True)
    image = models.ImageField(upload_to='images/membership/hero/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Hero Image URL (CDN)")
    title_ne = models.CharField(max_length=200, verbose_name="Hero Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Hero Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Hero Title (DE)")
    text_ne = models.TextField(verbose_name="Hero Text (NE)")
    text_en = models.TextField(verbose_name="Hero Text (EN)")
    text_de = models.TextField(verbose_name="Hero Text (DE)")

    class Meta:
        verbose_name = "Membership Hero"

class MembershipBenefit(models.Model):
    page = models.ForeignKey(MembershipPage, on_delete=models.CASCADE, related_name='benefits', null=True, blank=True)
    title_ne = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_de = models.CharField(max_length=200)
    desc_ne = models.TextField()
    desc_en = models.TextField()
    desc_de = models.TextField()
    icon = models.CharField(max_length=50, default="CheckCircle", help_text="Lucide icon name (e.g. Users, Award, Heart)")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Benefit"
        verbose_name_plural = "Benefits"

class MembershipFormSettings(models.Model):
    page = models.OneToOneField(MembershipPage, on_delete=models.CASCADE, related_name='form_settings', null=True, blank=True)
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

    # Form Labels
    label_name_ne = models.CharField(max_length=100, default="पूरा नाम")
    label_name_en = models.CharField(max_length=100, default="Full Name")
    label_name_de = models.CharField(max_length=100, default="Vollständiger Name")
    
    label_email_ne = models.CharField(max_length=100, default="ईमेल")
    label_email_en = models.CharField(max_length=100, default="Email Address")
    label_email_de = models.CharField(max_length=100, default="E-Mail-Adresse")
    
    label_phone_ne = models.CharField(max_length=100, default="फोन नम्बर")
    label_phone_en = models.CharField(max_length=100, default="Phone Number")
    label_phone_de = models.CharField(max_length=100, default="Telefonnummer")
    
    label_address_ne = models.CharField(max_length=100, default="ठेगाना")
    label_address_en = models.CharField(max_length=100, default="Address")
    label_address_de = models.CharField(max_length=100, default="Adresse")
    
    label_dob_ne = models.CharField(max_length=100, default="जन्म मिति")
    label_dob_en = models.CharField(max_length=100, default="Date of Birth")
    label_dob_de = models.CharField(max_length=100, default="Geburtsdatum")
    
    label_gender_ne = models.CharField(max_length=100, default="लिङ्ग")
    label_gender_en = models.CharField(max_length=100, default="Gender")
    label_gender_de = models.CharField(max_length=100, default="Geschlecht")
    
    label_experience_ne = models.CharField(max_length=100, default="अनुभव")
    label_experience_en = models.CharField(max_length=100, default="Volleyball Experience")
    label_experience_de = models.CharField(max_length=100, default="Volleyball-Erfahrung")
    
    label_position_ne = models.CharField(max_length=100, default="खेल्ने स्थान")
    label_position_en = models.CharField(max_length=100, default="Preferred Position")
    label_position_de = models.CharField(max_length=100, default="Bevorzugte Position")
    
    label_reason_ne = models.CharField(max_length=100, default="सदस्यताको कारण")
    label_reason_en = models.CharField(max_length=100, default="Reason for Joining")
    label_reason_de = models.CharField(max_length=100, default="Grund für den Beitritt")
    
    label_submit_ne = models.CharField(max_length=100, default="आवेदन पठाउनुहोस्")
    label_submit_en = models.CharField(max_length=100, default="Submit Application")
    label_submit_de = models.CharField(max_length=100, default="Antrag absenden")

    # Options (Stored as comma-separated strings for simplicity in Admin, or JSON if needed)
    options_gender_ne = models.CharField(max_length=500, default="पुरुष, महिला, अन्य")
    options_gender_en = models.CharField(max_length=500, default="Male, Female, Other")
    options_gender_de = models.CharField(max_length=500, default="Männlich, Weiblich, Andere")
    
    options_experience_ne = models.CharField(max_length=500, default="शुरुआती, मध्यवर्ती, उन्नत")
    options_experience_en = models.CharField(max_length=500, default="Beginner, Intermediate, Advanced")
    options_experience_de = models.CharField(max_length=500, default="Anfänger, Fortgeschritten, Profi")
    
    options_position_ne = models.CharField(max_length=500, default="सेटर, आउटसाइड हिटर, मिडल ब्लकर, लिबरो, राइट हिटर")
    options_position_en = models.CharField(max_length=500, default="Setter, Outside Hitter, Middle Blocker, Libero, Right Hitter")
    options_position_de = models.CharField(max_length=500, default="Zuspieler, Außenangreifer, Mittelblocker, Libero, Diagonalangreifer")

    class Meta:
        verbose_name = "Form Settings & Labels"

# Membership Application Model (for storing form submissions)
class MembershipApplication(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    EXPERIENCE_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    POSITION_CHOICES = [
        ('setter', 'Setter'),
        ('outside_hitter', 'Outside Hitter'),
        ('middle_blocker', 'Middle Blocker'),
        ('libero', 'Libero'),
        ('right_hitter', 'Right Hitter'),
    ]
    
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    position = models.CharField(max_length=30, choices=POSITION_CHOICES)
    reason = models.TextField()
    
    # Auto fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Membership Application"
        verbose_name_plural = "Membership Applications"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.full_name} - {self.email}"

# --- Proxy Models for Admin ---

class MembershipPageProxy(MembershipPage):
    class Meta:
        proxy = True
        app_label = 'membership_options'
        verbose_name = '01: Main Settings'
        verbose_name_plural = '01: Main Settings'

class MembershipHeroProxy(MembershipPage):
    class Meta:
        proxy = True
        app_label = 'membership_options'
        verbose_name = '02: Hero Section'
        verbose_name_plural = '02: Hero Section'

class MembershipBenefitsProxy(MembershipPage):
    class Meta:
        proxy = True
        app_label = 'membership_options'
        verbose_name = '03: Benefits Section'
        verbose_name_plural = '03: Benefits Section'

class MembershipFormProxy(MembershipPage):
    class Meta:
        proxy = True
        app_label = 'membership_options'
        verbose_name = '04: Form & Labels'
        verbose_name_plural = '04: Form & Labels'
