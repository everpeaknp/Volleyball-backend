from django.db import models
from apps.core.models import PublishableModel, SEOFields

class CommitteePage(PublishableModel, SEOFields):
    class Meta:
        db_table = 'pages_committeepage'
        verbose_name = "Committee Page"
        verbose_name_plural = "Committee Pages"

    def __str__(self):
        return f"Committee Page ({self.get_status_display()})"

class CommitteeHero(models.Model):
    page = models.OneToOneField(CommitteePage, on_delete=models.CASCADE, related_name='hero')
    
    title_ne = models.CharField(max_length=200, verbose_name="Hero Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Hero Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Hero Title (DE)")
    
    subtitle_ne = models.CharField(max_length=300, verbose_name="Hero Subtitle (NE)")
    subtitle_en = models.CharField(max_length=300, verbose_name="Hero Subtitle (EN)")
    subtitle_de = models.CharField(max_length=300, verbose_name="Hero Subtitle (DE)")
    
    background_image = models.ImageField(upload_to='images/committee/hero/', null=True, blank=True, verbose_name="Background Image")
    background_color = models.CharField(max_length=20, default="#030712", verbose_name="Background Color (if no image)")

    def __str__(self):
        return f"Hero Section ({self.page})"

class CommitteeBoard(models.Model):
    page = models.OneToOneField(CommitteePage, on_delete=models.CASCADE, related_name='board', null=True, blank=True)
    
    # President
    pres_name = models.CharField(max_length=200, verbose_name="President Name")
    pres_role_ne = models.CharField(max_length=200, verbose_name="President Role (NE)")
    pres_role_en = models.CharField(max_length=200, verbose_name="President Role (EN)")
    pres_role_de = models.CharField(max_length=200, verbose_name="President Role (DE)")
    pres_desc_ne = models.TextField(verbose_name="President Description (NE)", blank=True)
    pres_desc_en = models.TextField(verbose_name="President Description (EN)", blank=True)
    pres_desc_de = models.TextField(verbose_name="President Description (DE)", blank=True)
    pres_image = models.ImageField(upload_to='images/committee/board/', null=True, blank=True, verbose_name="President Image")
    pres_email = models.EmailField(blank=True, null=True, verbose_name="President Email")

    # Secretary
    sec_name = models.CharField(max_length=200, verbose_name="Secretary Name")
    sec_role_ne = models.CharField(max_length=200, verbose_name="Secretary Role (NE)")
    sec_role_en = models.CharField(max_length=200, verbose_name="Secretary Role (EN)")
    sec_role_de = models.CharField(max_length=200, verbose_name="Secretary Role (DE)")
    sec_desc_ne = models.TextField(verbose_name="Secretary Description (NE)", blank=True)
    sec_desc_en = models.TextField(verbose_name="Secretary Description (EN)", blank=True)
    sec_desc_de = models.TextField(verbose_name="Secretary Description (DE)", blank=True)
    sec_image = models.ImageField(upload_to='images/committee/board/', null=True, blank=True, verbose_name="Secretary Image")
    sec_email = models.EmailField(blank=True, null=True, verbose_name="Secretary Email")

    # Treasurer
    tres_name = models.CharField(max_length=200, verbose_name="Treasurer Name")
    tres_role_ne = models.CharField(max_length=200, verbose_name="Treasurer Role (NE)")
    tres_role_en = models.CharField(max_length=200, verbose_name="Treasurer Role (EN)")
    tres_role_de = models.CharField(max_length=200, verbose_name="Treasurer Role (DE)")
    tres_desc_ne = models.TextField(verbose_name="Treasurer Description (NE)", blank=True)
    tres_desc_en = models.TextField(verbose_name="Treasurer Description (EN)", blank=True)
    tres_desc_de = models.TextField(verbose_name="Treasurer Description (DE)", blank=True)
    tres_image = models.ImageField(upload_to='images/committee/board/', null=True, blank=True, verbose_name="Treasurer Image")
    tres_email = models.EmailField(blank=True, null=True, verbose_name="Treasurer Email")

    def __str__(self):
        return f"Executive Board ({self.page})"

class CommitteeMember(models.Model):
    page = models.ForeignKey(CommitteePage, on_delete=models.CASCADE, related_name='members', null=True, blank=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/committee/members/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "General Member"
        verbose_name_plural = "General Members"

    def __str__(self):
        return self.name

class CommitteeSectionSettings(models.Model):
    page = models.OneToOneField(CommitteePage, on_delete=models.CASCADE, related_name='section_settings')
    
    member_section_title_ne = models.CharField(max_length=200, default="कार्यसमिति सदस्यहरू", verbose_name="Member Section Title (NE)")
    member_section_title_en = models.CharField(max_length=200, default="Committee Members", verbose_name="Member Section Title (EN)")
    member_section_title_de = models.CharField(max_length=200, default="Vorstandsmitglieder", verbose_name="Member Section Title (DE)")

    def __str__(self):
        return f"Section Titles ({self.page})"


# Proxy models for Admin organization
class CommitteePageProxy(CommitteePage):
    class Meta:
        proxy = True
        verbose_name = "01. Main Settings"
        verbose_name_plural = "01. Main Settings"

class CommitteeHeroProxy(CommitteePage):
    class Meta:
        proxy = True
        verbose_name = "02. Hero Section"
        verbose_name_plural = "02. Hero Section"

class CommitteeExecutiveProxy(CommitteePage):
    class Meta:
        proxy = True
        verbose_name = "03. Executive Board"
        verbose_name_plural = "03. Executive Board"

class CommitteeGeneralProxy(CommitteePage):
    class Meta:
        proxy = True
        verbose_name = "04. General Members"
        verbose_name_plural = "04. General Members"

class CommitteeTitleProxy(CommitteePage):
    class Meta:
        proxy = True
        verbose_name = "05. Section Titles"
        verbose_name_plural = "05. Section Titles"
