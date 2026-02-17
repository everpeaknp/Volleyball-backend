from django.db import models
from apps.core.models import PublishableModel, SEOFields

class TeamPage(PublishableModel, SEOFields):
    class Meta:
        verbose_name = "Team Page"
        verbose_name_plural = "Team Pages"

    def __str__(self):
        return f"Team Page ({self.status})"

class TeamHero(models.Model):
    page = models.OneToOneField(TeamPage, on_delete=models.CASCADE, related_name='hero', null=True, blank=True)
    image = models.ImageField(upload_to='images/team/hero/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Hero Image URL (CDN)")
    title_ne = models.CharField(max_length=200, verbose_name="Hero Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Hero Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Hero Title (DE)")
    text_ne = models.TextField(verbose_name="Hero Text (NE)")
    text_en = models.TextField(verbose_name="Hero Text (EN)")
    text_de = models.TextField(verbose_name="Hero Text (DE)")

    class Meta:
        verbose_name = "Team Hero"

    def __str__(self):
        return f"Hero Section ({self.page})"

class TeamCoachesSettings(models.Model):
    page = models.OneToOneField(TeamPage, on_delete=models.CASCADE, related_name='coaches_settings', null=True, blank=True)
    title_ne = models.CharField(max_length=200, verbose_name="Coaches Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Coaches Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Coaches Title (DE)")

    class Meta:
        verbose_name = "Coaches Section Settings"

class TeamPlayersSettings(models.Model):
    page = models.OneToOneField(TeamPage, on_delete=models.CASCADE, related_name='players_settings', null=True, blank=True)
    title_ne = models.CharField(max_length=200, verbose_name="Players Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Players Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Players Title (DE)")

    class Meta:
        verbose_name = "Players Section Settings"

class Coach(models.Model):
    page = models.ForeignKey(TeamPage, on_delete=models.CASCADE, related_name='coaches', null=True, blank=True)
    name_ne = models.CharField(max_length=200, verbose_name="Name (NE)", default="")
    name_en = models.CharField(max_length=200, verbose_name="Name (EN)", default="")
    name_de = models.CharField(max_length=200, verbose_name="Name (DE)", default="")
    role_ne = models.CharField(max_length=200, verbose_name="Role (NE)")
    role_en = models.CharField(max_length=200, verbose_name="Role (EN)")
    role_de = models.CharField(max_length=200, verbose_name="Role (DE)")
    experience_ne = models.CharField(max_length=200, verbose_name="Experience (NE)")
    experience_en = models.CharField(max_length=200, verbose_name="Experience (EN)")
    experience_de = models.CharField(max_length=200, verbose_name="Experience (DE)")
    image = models.ImageField(upload_to='images/team/coaches/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Image URL (CDN)")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Coach"
        verbose_name_plural = "Coaches"

class Player(models.Model):
    page = models.ForeignKey(TeamPage, on_delete=models.CASCADE, related_name='players', null=True, blank=True)
    name_ne = models.CharField(max_length=200, verbose_name="Name (NE)", default="")
    name_en = models.CharField(max_length=200, verbose_name="Name (EN)", default="")
    name_de = models.CharField(max_length=200, verbose_name="Name (DE)", default="")
    number = models.CharField(max_length=10)
    position_ne = models.CharField(max_length=100, verbose_name="Position (NE)")
    position_en = models.CharField(max_length=100, verbose_name="Position (EN)")
    position_de = models.CharField(max_length=100, verbose_name="Position (DE)")
    image = models.ImageField(upload_to='images/team/players/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Image URL (CDN)")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Player"
        verbose_name_plural = "Players"

class TeamPhotoSection(models.Model):
    page = models.OneToOneField(TeamPage, on_delete=models.CASCADE, related_name='photo_section', null=True, blank=True)
    title_ne = models.CharField(max_length=200, verbose_name="Photo Section Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Photo Section Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Photo Section Title (DE)")
    subtitle_ne = models.CharField(max_length=200, verbose_name="Photo Section Subtitle (NE)")
    subtitle_en = models.CharField(max_length=200, verbose_name="Photo Section Subtitle (EN)")
    subtitle_de = models.CharField(max_length=200, verbose_name="Photo Section Subtitle (DE)")
    image = models.ImageField(upload_to='images/team/photo/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Team Photo URL (CDN)")

    class Meta:
        verbose_name = "Team Photo Section"

class TeamCTA(models.Model):
    page = models.OneToOneField(TeamPage, on_delete=models.CASCADE, related_name='cta', null=True, blank=True)
    title_ne = models.CharField(max_length=200, verbose_name="CTA Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="CTA Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="CTA Title (DE)")
    text_ne = models.TextField(verbose_name="CTA Text (NE)")
    text_en = models.TextField(verbose_name="CTA Text (EN)")
    text_de = models.TextField(verbose_name="CTA Text (DE)")
    button_label_ne = models.CharField(max_length=100, verbose_name="Button Label (NE)")
    button_label_en = models.CharField(max_length=100, verbose_name="Button Label (EN)")
    button_label_de = models.CharField(max_length=100, verbose_name="Button Label (DE)")
    button_link = models.CharField(max_length=200, default="/membership")

    class Meta:
        verbose_name = "Team CTA"

# --- Proxy Models for Admin ---

class TeamPageProxy(TeamPage):
    class Meta:
        proxy = True
        app_label = 'team_options'
        verbose_name = '01: Main Settings'
        verbose_name_plural = '01: Main Settings'

class TeamHeroProxy(TeamPage):
    class Meta:
        proxy = True
        app_label = 'team_options'
        verbose_name = '02: Hero Section'
        verbose_name_plural = '02: Hero Section'

class TeamCoachesProxy(TeamPage):
    class Meta:
        proxy = True
        app_label = 'team_options'
        verbose_name = '03: Coaches Section'
        verbose_name_plural = '03: Coaches Section'

class TeamPlayersProxy(TeamPage):
    class Meta:
        proxy = True
        app_label = 'team_options'
        verbose_name = '04: Players Section'
        verbose_name_plural = '04: Players Section'

class TeamPhotoCTAProxy(TeamPage):
    class Meta:
        proxy = True
        app_label = 'team_options'
        verbose_name = '05: Photo & CTA Section'
        verbose_name_plural = '05: Photo & CTA Section'
