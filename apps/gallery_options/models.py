from django.db import models
from apps.core.models import PublishableModel, SEOFields

class GalleryPage(PublishableModel, SEOFields):
    class Meta:
        verbose_name = "Gallery Page"
        verbose_name_plural = "Gallery Pages"

    def __str__(self):
        return f"Gallery Page ({self.status})"

class GalleryHero(models.Model):
    page = models.OneToOneField(GalleryPage, on_delete=models.CASCADE, related_name='hero')
    title_ne = models.CharField(max_length=200, verbose_name="Hero Title (NE)")
    title_en = models.CharField(max_length=200, verbose_name="Hero Title (EN)")
    title_de = models.CharField(max_length=200, verbose_name="Hero Title (DE)")
    text_ne = models.TextField(verbose_name="Hero Text (NE)")
    text_en = models.TextField(verbose_name="Hero Text (EN)")
    text_de = models.TextField(verbose_name="Hero Text (DE)")

    class Meta:
        verbose_name = "Gallery Hero"

class GalleryCategory(models.Model):
    name_ne = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Gallery Category"
        verbose_name_plural = "Gallery Categories"

    def __str__(self):
        return self.name_en

class GalleryImage(models.Model):
    page = models.ForeignKey(GalleryPage, on_delete=models.CASCADE, related_name='images')
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='images')
    image = models.ImageField(upload_to='images/gallery/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Image URL (CDN)")
    title_ne = models.CharField(max_length=200, blank=True)
    title_en = models.CharField(max_length=200, blank=True)
    title_de = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

class GallerySettings(models.Model):
    page = models.OneToOneField(GalleryPage, on_delete=models.CASCADE, related_name='settings')
    no_images_text_ne = models.CharField(max_length=200, default="यो श्रेणीमा कुनै तस्बिर छैन।")
    no_images_text_en = models.CharField(max_length=200, default="No photos in this category.")
    no_images_text_de = models.CharField(max_length=200, default="Keine Fotos in dieser Kategorie.")

    class Meta:
        verbose_name = "Gallery Labels & Settings"

# Proxy Models for Step-by-Step Admin
class GalleryPageProxy(GalleryPage):
    class Meta:
        proxy = True
        verbose_name = "01: Main Settings"
        verbose_name_plural = "01: Main Settings"

class GalleryHeroProxy(GalleryPage):
    class Meta:
        proxy = True
        verbose_name = "02: Hero Section"
        verbose_name_plural = "02: Hero Section"

class GalleryCategoriesProxy(GalleryCategory):
    class Meta:
        proxy = True
        verbose_name = "03: Categories"
        verbose_name_plural = "03: Categories"

class GalleryImagesProxy(GalleryPage):
    class Meta:
        proxy = True
        verbose_name = "04: Gallery Images"
        verbose_name_plural = "04: Gallery Images"

class GalleryLabelsProxy(GalleryPage):
    class Meta:
        proxy = True
        verbose_name = "05: Labels & Settings"
        verbose_name_plural = "05: Labels & Settings"
