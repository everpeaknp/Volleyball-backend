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



class ExecutiveMember(models.Model):
    page = models.ForeignKey(CommitteePage, on_delete=models.CASCADE, related_name='executives')
    name = models.CharField(max_length=200, verbose_name="Name")
    role_ne = models.CharField(max_length=200, verbose_name="Role (NE)")
    role_en = models.CharField(max_length=200, verbose_name="Role (EN)")
    role_de = models.CharField(max_length=200, verbose_name="Role (DE)")
    desc_ne = models.TextField(verbose_name="Description (NE)", blank=True)
    desc_en = models.TextField(verbose_name="Description (EN)", blank=True)
    desc_de = models.TextField(verbose_name="Description (DE)", blank=True)
    image = models.ImageField(upload_to='images/committee/executives/', null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Executive Member"
        verbose_name_plural = "Executive Members"

    def __str__(self):
        return self.name

class CommitteeGroup(models.Model):
    page = models.ForeignKey(CommitteePage, on_delete=models.CASCADE, related_name='groups')
    
    title_ne = models.CharField(max_length=200, verbose_name="Group Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Group Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Group Title (DE)")
    
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Committee Group"
        verbose_name_plural = "Committee Groups"

    def __str__(self):
        return f"{self.title_en} ({self.page})"

class CommitteeMember(models.Model):
    # page field remains for now to facilitate data migration, but will eventually be removed or redirected via group
    page = models.ForeignKey(CommitteePage, on_delete=models.CASCADE, related_name='members', null=True, blank=True)
    group = models.ForeignKey(CommitteeGroup, on_delete=models.CASCADE, related_name='members', null=True, blank=True)
    
    name_ne = models.CharField(max_length=200, verbose_name="Name (NE)", default='')
    name_en = models.CharField(max_length=200, verbose_name="Name (EN)", default='')
    name_de = models.CharField(max_length=200, verbose_name="Name (DE)", default='')
    name = models.CharField(max_length=200, blank=True) # Fallback
    image = models.ImageField(upload_to='images/committee/members/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Committee Member"
        verbose_name_plural = "Committee Members"

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

class CommitteeGroupProxy(CommitteePage):
    class Meta:
        proxy = True
        verbose_name = "04. Committee Groups"
        verbose_name_plural = "04. Committee Groups"

class CommitteeTitleProxy(CommitteePage):
    class Meta:
        proxy = True
        verbose_name = "05. Section Titles"
        verbose_name_plural = "05. Section Titles"
