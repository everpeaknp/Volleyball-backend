from django.db import models
from apps.core.models import PublishableModel, SEOFields

class NewsPage(PublishableModel, SEOFields):
    class Meta:
        verbose_name = "News Page"
        verbose_name_plural = "News Pages"

    def __str__(self):
        return f"News Page ({self.status})"

class NewsHero(models.Model):
    page = models.OneToOneField(NewsPage, on_delete=models.CASCADE, related_name='hero', null=True, blank=True)
    image = models.ImageField(upload_to='images/news/hero/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Hero Image URL (CDN)")
    title_ne = models.CharField(max_length=200, verbose_name="Hero Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Hero Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Hero Title (DE)")
    text_ne = models.TextField(verbose_name="Hero Text (NE)")
    text_en = models.TextField(verbose_name="Hero Text (EN)")
    text_de = models.TextField(verbose_name="Hero Text (DE)")

    class Meta:
        verbose_name = "News Hero"

class NewsSettings(models.Model):
    page = models.OneToOneField(NewsPage, on_delete=models.CASCADE, related_name='settings', null=True, blank=True)
    
    featured_label_ne = models.CharField(max_length=100, default="मुख्य समाचार")
    featured_label_en = models.CharField(max_length=100, default="Featured News")
    featured_label_de = models.CharField(max_length=100, default="Top-Nachricht")
    
    read_more_label_ne = models.CharField(max_length=100, default="पूरा पढ्नुहोस्")
    read_more_label_en = models.CharField(max_length=100, default="Read More")
    read_more_label_de = models.CharField(max_length=100, default="Weiterlesen")
    
    other_news_title_ne = models.CharField(max_length=200, default="अन्य समाचार")
    other_news_title_en = models.CharField(max_length=200, default="Other News")
    other_news_title_de = models.CharField(max_length=200, default="Weitere Neuigkeiten")

    class Meta:
        verbose_name = "News Labels & Settings"

class NewsCategory(models.Model):
    name_ne = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "News Category"
        verbose_name_plural = "News Categories"

    def __str__(self):
        return self.name_en

class NewsArticle(models.Model):
    page = models.ForeignKey(NewsPage, on_delete=models.CASCADE, related_name='articles', null=True, blank=True)
    title_ne = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_de = models.CharField(max_length=200)
    
    excerpt_ne = models.TextField(blank=True)
    excerpt_en = models.TextField(blank=True)
    excerpt_de = models.TextField(blank=True)
    
    content_ne = models.TextField(blank=True) # Could be RichText later
    content_en = models.TextField(blank=True)
    content_de = models.TextField(blank=True)
    
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    
    image = models.ImageField(upload_to='images/news/articles/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Article Image URL")
    
    date_text_ne = models.CharField(max_length=100, help_text="e.g. फेब्रुअरी २५, २०२६")
    date_text_en = models.CharField(max_length=100, help_text="e.g. February 25, 2026")
    date_text_de = models.CharField(max_length=100, help_text="e.g. 25. Februar 2026")
    
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "News Article"
        verbose_name_plural = "News Articles"

# Proxy Models for Step-by-Step Admin
class NewsPageProxy(NewsPage):
    class Meta:
        proxy = True
        verbose_name = "01: Main Settings"
        verbose_name_plural = "01: Main Settings"

class NewsHeroProxy(NewsPage):
    class Meta:
        proxy = True
        verbose_name = "02: Hero Section"
        verbose_name_plural = "02: Hero Section"

class NewsCategoriesProxy(NewsCategory):
    class Meta:
        proxy = True
        verbose_name = "03: Categories"
        verbose_name_plural = "03: Categories"

class NewsArticlesProxy(NewsPage):
    class Meta:
        proxy = True
        verbose_name = "04: Articles"
        verbose_name_plural = "04: Articles"

class NewsLabelsProxy(NewsPage):
    class Meta:
        proxy = True
        verbose_name = "05: Labels & Settings"
        verbose_name_plural = "05: Labels & Settings"
