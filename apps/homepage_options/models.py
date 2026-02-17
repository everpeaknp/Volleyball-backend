from django.db import models
from apps.core.models import PublishableModel, SEOFields

# --- Home Page Real Models ---

class HomePage(PublishableModel, SEOFields):
    class Meta:
        db_table = 'pages_homepage'
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

class HomeHero(models.Model):
    page = models.OneToOneField(HomePage, on_delete=models.CASCADE, related_name='hero')
    video_file = models.FileField(upload_to='videos/hero/', null=True, blank=True, verbose_name="Video File (Upload)")
    video_url = models.URLField(blank=True, null=True, verbose_name="Video URL (YouTube/CDN)")
    image = models.ImageField(upload_to='images/hero/', null=True, blank=True, verbose_name="Fallback/Background Image (Upload)")
    image_url = models.URLField(blank=True, null=True, verbose_name="Background Image URL (External/CDN)")
    title_ne = models.TextField(verbose_name="Title (NE)")
    title_en = models.TextField(verbose_name="Title (EN)")
    title_de = models.TextField(verbose_name="Title (DE)")
    subtitle_ne = models.TextField(verbose_name="Subtitle (NE)")
    subtitle_en = models.TextField(verbose_name="Subtitle (EN)")
    subtitle_de = models.TextField(verbose_name="Subtitle (DE)")
    cta_join_label_ne = models.CharField(max_length=100, verbose_name="Join CTA (NE)")
    cta_join_label_en = models.CharField(max_length=100, verbose_name="Join CTA (EN)")
    cta_join_label_de = models.CharField(max_length=100, verbose_name="Join CTA (DE)")
    cta_learn_label_ne = models.CharField(max_length=100, verbose_name="Learn CTA (NE)")
    cta_learn_label_en = models.CharField(max_length=100, verbose_name="Learn CTA (EN)")
    cta_learn_label_de = models.CharField(max_length=100, verbose_name="Learn CTA (DE)")

    class Meta:
        db_table = 'pages_homehero'
        verbose_name = "Home Hero"

    def __str__(self):
        return f"Hero Section ({self.page})"

class HomeIntro(models.Model):
    page = models.OneToOneField(HomePage, on_delete=models.CASCADE, related_name='intro')
    image = models.ImageField(upload_to='images/intro/', null=True, blank=True, verbose_name="Image File (Upload)")
    image_url = models.URLField(blank=True, null=True, verbose_name="Image URL (External/CDN)")
    mini_header_ne = models.CharField(max_length=200, verbose_name="Mini Header (NE)")
    mini_header_en = models.CharField(max_length=200, verbose_name="Mini Header (EN)")
    mini_header_de = models.CharField(max_length=200, verbose_name="Mini Header (DE)")
    title_ne = models.CharField(max_length=200, verbose_name="Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Title (DE)")
    text_ne = models.TextField(verbose_name="Text (NE)")
    text_en = models.TextField(verbose_name="Text (EN)")
    text_de = models.TextField(verbose_name="Text (DE)")
    subtext_ne = models.TextField(verbose_name="Subtext (NE)")
    subtext_en = models.TextField(verbose_name="Subtext (EN)")
    subtext_de = models.TextField(verbose_name="Subtext (DE)")

    class Meta:
        db_table = 'pages_homeintro'
        verbose_name = "Home Intro"

    def __str__(self):
        return f"Intro Section ({self.page})"

class HomeMission(models.Model):
    page = models.OneToOneField(HomePage, on_delete=models.CASCADE, related_name='mission')
    mission_label_ne = models.CharField(max_length=100, verbose_name="Label (NE)")
    mission_label_en = models.CharField(max_length=100, verbose_name="Label (EN)")
    mission_label_de = models.CharField(max_length=100, verbose_name="Label (DE)")
    title_ne = models.CharField(max_length=200, verbose_name="Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Title (DE)")
    description_ne = models.TextField(verbose_name="Description (NE)")
    description_en = models.TextField(verbose_name="Description (EN)")
    description_de = models.TextField(verbose_name="Description (DE)")

    class Meta:
        db_table = 'pages_homemission'
        verbose_name = "Home Mission"

    def __str__(self):
        return f"Mission Section ({self.page})"

class HomeObjective(models.Model):
    mission = models.ForeignKey(HomeMission, on_delete=models.CASCADE, related_name='objectives', null=True)
    image = models.ImageField(upload_to='images/objectives/', null=True, blank=True, verbose_name="Image (Upload)")
    image_url = models.URLField(blank=True, null=True, verbose_name="Image URL (CDN)")
    badge_number = models.CharField(max_length=10, default="01")
    text_ne = models.TextField(verbose_name="Text (NE)")
    text_en = models.TextField(verbose_name="Text (EN)")
    text_de = models.TextField(verbose_name="Text (DE)")
    goal_prefix_ne = models.CharField(max_length=50, default="Goal", verbose_name="Prefix (NE)")
    goal_prefix_en = models.CharField(max_length=50, default="Goal", verbose_name="Prefix (EN)")
    goal_prefix_de = models.CharField(max_length=50, default="Ziel", verbose_name="Prefix (DE)")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        db_table = 'pages_homeobjective'
        ordering = ['order']
        verbose_name = "Home Objective"

class HomeMotto(models.Model):
    page = models.OneToOneField(HomePage, on_delete=models.CASCADE, related_name='motto')
    text_ne = models.TextField(verbose_name="Motto (NE)")
    text_en = models.TextField(verbose_name="Motto (EN)")
    text_de = models.TextField(verbose_name="Motto (DE)")
    button_label_ne = models.CharField(max_length=100, verbose_name="Button (NE)")
    button_label_en = models.CharField(max_length=100, verbose_name="Button (EN)")
    button_label_de = models.CharField(max_length=100, verbose_name="Button (DE)")

    class Meta:
        db_table = 'pages_homemotto'
        verbose_name = "Home Motto"

    def __str__(self):
        return f"Motto Section ({self.page})"

class HomeStat(models.Model):
    page = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name='stats')
    label_ne = models.CharField(max_length=100, verbose_name="Label (NE)")
    label_en = models.CharField(max_length=100, verbose_name="Label (EN)")
    label_de = models.CharField(max_length=100, verbose_name="Label (DE)")
    value = models.PositiveIntegerField()
    suffix = models.CharField(max_length=10, default="+")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        db_table = 'pages_homestat'
        ordering = ['order']
        verbose_name = "Home Stat"

# --- Home Page Proxy Models (for Sidebar organization) ---

class HomePageProxy(HomePage):
    class Meta:
        proxy = True
        app_label = 'homepage_options'
        verbose_name = 'Step 1: Main Settings'
        verbose_name_plural = 'Step 1: Main Settings'

class HomeHeroProxy(HomeHero):
    class Meta:
        proxy = True
        app_label = 'homepage_options'
        verbose_name = 'Step 2: Hero Section'
        verbose_name_plural = 'Step 2: Hero Section'

class HomeIntroProxy(HomeIntro):
    class Meta:
        proxy = True
        app_label = 'homepage_options'
        verbose_name = 'Step 3: Intro Section'
        verbose_name_plural = 'Step 3: Intro Section'

class HomeMissionProxy(HomeMission):
    class Meta:
        proxy = True
        app_label = 'homepage_options'
        verbose_name = 'Step 4: Mission Section'
        verbose_name_plural = 'Step 4: Mission Section'

class HomeObjectiveProxy(HomeObjective):
    class Meta:
        proxy = True
        app_label = 'homepage_options'
        verbose_name = 'Step 5: Objectives'
        verbose_name_plural = 'Step 5: Objectives'

class HomeMottoProxy(HomeMotto):
    class Meta:
        proxy = True
        app_label = 'homepage_options'
        verbose_name = 'Step 6: Motto Section'
        verbose_name_plural = 'Step 6: Motto Section'

class HomeStatProxy(HomeStat):
    class Meta:
        proxy = True
        app_label = 'homepage_options'
        verbose_name = 'Step 7: Stats'
        verbose_name_plural = 'Step 7: Stats'
