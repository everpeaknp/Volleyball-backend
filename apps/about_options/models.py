from django.db import models
from apps.core.models import PublishableModel, SEOFields

# --- About Page Real Models ---

class AboutPage(PublishableModel, SEOFields):
    class Meta:
        db_table = 'pages_aboutpage'
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"

class AboutHero(models.Model):
    page = models.OneToOneField(AboutPage, on_delete=models.CASCADE, related_name='hero')
    since_text_ne = models.CharField(max_length=100, verbose_name="Since Text (NE)")
    since_text_en = models.CharField(max_length=100, verbose_name="Since Text (EN)")
    since_text_de = models.CharField(max_length=100, verbose_name="Since Text (DE)")
    show_pulsing_dot = models.BooleanField(default=True, verbose_name="Show Pulsing Dot Icon")
    title_ne = models.CharField(max_length=200, verbose_name="Hero Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Hero Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Hero Title (DE)")
    text_ne = models.TextField(verbose_name="Hero Text (NE)")
    text_en = models.TextField(verbose_name="Hero Text (EN)")
    text_de = models.TextField(verbose_name="Hero Text (DE)")
    background_image = models.ImageField(upload_to='images/about/hero/', null=True, blank=True, verbose_name="Background Image")
    background_color = models.CharField(max_length=20, default="#030712", verbose_name="Background Color (Hex)")

    class Meta:
        db_table = 'pages_abouthero'
        verbose_name = "About Hero"

    def __str__(self):
        return f"About Hero ({self.page})"

class AboutIntro(models.Model):
    page = models.OneToOneField(AboutPage, on_delete=models.CASCADE, related_name='intro')
    title_part1_ne = models.CharField(max_length=100, verbose_name="Title Part 1 (NE)")
    title_part1_en = models.CharField(max_length=100, verbose_name="Title Part 1 (EN)")
    title_part1_de = models.CharField(max_length=100, verbose_name="Title Part 1 (DE)")
    title_part2_ne = models.CharField(max_length=100, verbose_name="Title Part 2 (NE)")
    title_part2_en = models.CharField(max_length=100, verbose_name="Title Part 2 (EN)")
    title_part2_de = models.CharField(max_length=100, verbose_name="Title Part 2 (DE)")
    text1_ne = models.TextField(verbose_name="Main Text Paragraph 1 (NE)")
    text1_en = models.TextField(verbose_name="Main Text Paragraph 1 (EN)")
    text1_de = models.TextField(verbose_name="Main Text Paragraph 1 (DE)")
    text2_ne = models.TextField(verbose_name="Main Text Paragraph 2 (NE)")
    text2_en = models.TextField(verbose_name="Main Text Paragraph 2 (EN)")
    text2_de = models.TextField(verbose_name="Main Text Paragraph 2 (DE)")
    main_image = models.ImageField(upload_to='images/about/intro/', null=True, blank=True, verbose_name="Main Image")
    secondary_image = models.ImageField(upload_to='images/about/intro/', null=True, blank=True, verbose_name="Secondary Overlay Image")
    established_label_ne = models.CharField(max_length=50, verbose_name="Established Label (NE)")
    established_label_en = models.CharField(max_length=50, verbose_name="Established Label (EN)")
    established_label_de = models.CharField(max_length=50, verbose_name="Established Label (DE)")
    established_year = models.CharField(max_length=10, default="2020", verbose_name="Established Year")

    class Meta:
        db_table = 'pages_aboutintro'
        verbose_name = "About Intro"

    def __str__(self):
        return f"About Intro ({self.page})"

class AboutStat(models.Model):
    intro = models.ForeignKey(AboutIntro, on_delete=models.CASCADE, related_name='stats')
    label_ne = models.CharField(max_length=100, verbose_name="Label (NE)")
    label_en = models.CharField(max_length=100, verbose_name="Label (EN)")
    label_de = models.CharField(max_length=100, verbose_name="Label (DE)")
    value = models.CharField(max_length=20, verbose_name="Value (e.g. 50+)")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        db_table = 'pages_aboutstat'
        ordering = ['order']
        verbose_name = "About Stat"

class AboutCore(models.Model):
    page = models.OneToOneField(AboutPage, on_delete=models.CASCADE, related_name='core')
    title_ne = models.CharField(max_length=200, verbose_name="Section Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Section Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Section Title (DE)")
    vision_title_ne = models.CharField(max_length=100, verbose_name="Vision Title (NE)")
    vision_title_en = models.CharField(max_length=100, verbose_name="Vision Title (EN)")
    vision_title_de = models.CharField(max_length=100, verbose_name="Vision Title (DE)")
    vision_text_ne = models.TextField(verbose_name="Vision Text (NE)")
    vision_text_en = models.TextField(verbose_name="Vision Text (EN)")
    vision_text_de = models.TextField(verbose_name="Vision Text (DE)")
    vision_icon = models.CharField(max_length=50, default="Eye", verbose_name="Vision Icon (Lucide name)")
    mission_title_ne = models.CharField(max_length=100, verbose_name="Mission Title (NE)")
    mission_title_en = models.CharField(max_length=100, verbose_name="Mission Title (EN)")
    mission_title_de = models.CharField(max_length=100, verbose_name="Mission Title (DE)")
    mission_text_ne = models.TextField(verbose_name="Mission Text (NE)")
    mission_text_en = models.TextField(verbose_name="Mission Text (EN)")
    mission_text_de = models.TextField(verbose_name="Mission Text (DE)")
    mission_icon = models.CharField(max_length=50, default="Target", verbose_name="Mission Icon (Lucide name)")

    class Meta:
        db_table = 'pages_aboutcore'
        verbose_name = "About Core (Vision/Mission)"

    def __str__(self):
        return f"Core Section ({self.page})"

class AboutStrategic(models.Model):
    page = models.OneToOneField(AboutPage, on_delete=models.CASCADE, related_name='strategic')
    strategic_title_ne = models.CharField(max_length=200, verbose_name="Label (NE)")
    strategic_title_en = models.CharField(max_length=200, verbose_name="Label (EN)")
    strategic_title_de = models.CharField(max_length=200, verbose_name="Label (DE)")
    objectives_title_ne = models.CharField(max_length=200, verbose_name="Objectives Title (NE)")
    objectives_title_en = models.CharField(max_length=200, verbose_name="Objectives Title (EN)")
    objectives_title_de = models.CharField(max_length=200, verbose_name="Objectives Title (DE)")
    side_image = models.ImageField(upload_to='images/about/strategic/', null=True, blank=True, verbose_name="Side Graphic Image")
    promo_title_ne = models.CharField(max_length=200, verbose_name="Promo Title (NE)")
    promo_title_en = models.CharField(max_length=200, verbose_name="Promo Title (EN)")
    promo_title_de = models.CharField(max_length=200, verbose_name="Promo Title (DE)")
    promo_text_ne = models.TextField(verbose_name="Promo Text (NE)")
    promo_text_en = models.TextField(verbose_name="Promo Text (EN)")
    promo_text_de = models.TextField(verbose_name="Promo Text (DE)")
    promo_icon = models.CharField(max_length=50, default="Globe", verbose_name="Promo Icon (Lucide name)")

    class Meta:
        db_table = 'pages_aboutstrategic'
        verbose_name = "About Strategic"

    def __str__(self):
        return f"Strategic Section ({self.page})"

class AboutObjective(models.Model):
    strategic = models.ForeignKey(AboutStrategic, on_delete=models.CASCADE, related_name='objectives')
    text_ne = models.TextField(verbose_name="Objective Text (NE)")
    text_en = models.TextField(verbose_name="Objective Text (EN)")
    text_de = models.TextField(verbose_name="Objective Text (DE)")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        db_table = 'pages_aboutobjective'
        ordering = ['order']
        verbose_name = "About Objective"

# --- About Page Proxy Models (for Sidebar organization) ---

class AboutPageProxy(AboutPage):
    class Meta:
        proxy = True
        app_label = 'about_options'
        verbose_name = 'Step 1: Main Settings'
        verbose_name_plural = 'Step 1: Main Settings'

class AboutHeroProxy(AboutHero):
    class Meta:
        proxy = True
        app_label = 'about_options'
        verbose_name = 'Step 2: Hero Section'
        verbose_name_plural = 'Step 2: Hero Section'

class AboutIntroProxy(AboutIntro):
    class Meta:
        proxy = True
        app_label = 'about_options'
        verbose_name = 'Step 3: Intro Section'
        verbose_name_plural = 'Step 3: Intro Section'

class AboutCoreProxy(AboutCore):
    class Meta:
        proxy = True
        app_label = 'about_options'
        verbose_name = 'Step 4: Vision & Mission'
        verbose_name_plural = 'Step 4: Vision & Mission'

class AboutStrategicProxy(AboutStrategic):
    class Meta:
        proxy = True
        app_label = 'about_options'
        verbose_name = 'Step 5: Strategic Goals'
        verbose_name_plural = 'Step 5: Strategic Goals'
