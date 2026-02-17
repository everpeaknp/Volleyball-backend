from django.db import models
from django.core.cache import cache
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _


class PublishableManager(Manager):
    """
    Manager that only returns published objects by default.
    """
    
    def get_queryset(self):
        return super().get_queryset().filter(status='published')
    
    def all_with_drafts(self):
        """Return all objects including drafts."""
        return super().get_queryset()
    
    def drafts(self):
        """Return only draft objects."""
        return super().get_queryset().filter(status='draft')
    
    def published(self):
        """Return only published objects."""
        return self.get_queryset()


class MultiLanguageManager(Manager):
    """
    Manager for multi-language content with caching.
    """
    
    def get_by_language(self, language, fallback=True):
        """
        Get content by language with optional fallback.
        
        Args:
            language: Language code (NE, EN, DE)
            fallback: Whether to fallback to default language if content not found
        """
        cache_key = f"{self.model._meta.model_name}:{language}"
        cached_result = cache.get(cache_key)
        
        if cached_result:
            return cached_result
        
        try:
            obj = self.get(language=language)
        except self.model.DoesNotExist:
            if fallback and language != 'NE':
                # Fallback to Nepali as default
                try:
                    obj = self.get(language='NE')
                except self.model.DoesNotExist:
                    obj = None
            else:
                obj = None
        
        # Cache the result for 1 hour
        if obj:
            cache.set(cache_key, obj, 3600)
        
        return obj
    
    def get_all_languages(self):
        """Get all language versions of content."""
        cache_key = f"{self.model._meta.model_name}:all_languages"
        cached_result = cache.get(cache_key)
        
        if cached_result:
            return cached_result
        
        objects = {}
        for lang_code, lang_name in self.model.LANGUAGE_CHOICES:
            try:
                objects[lang_code] = self.get(language=lang_code)
            except self.model.DoesNotExist:
                objects[lang_code] = None
        
        # Cache for 1 hour
        cache.set(cache_key, objects, 3600)
        
        return objects


class OrderedManager(Manager):
    """
    Manager that returns objects in order by default.
    """
    
    def get_queryset(self):
        return super().get_queryset().order_by('order')


class MediaManager(Manager):
    """
    Manager for media files with type filtering.
    """
    
    def images(self):
        """Return only image files."""
        return self.get_queryset().filter(file_type='image')
    
    def videos(self):
        """Return only video files."""
        return self.get_queryset().filter(file_type='video')
    
    def documents(self):
        """Return only document files."""
        return self.get_queryset().filter(file_type='document')
    
    def by_category(self, category):
        """Return media files by category."""
        return self.get_queryset().filter(category=category)


class SeoManager(Manager):
    """
    Manager for SEO-aware content.
    """
    
    def with_seo(self):
        """Return objects that have SEO data."""
        return self.get_queryset().exclude(
            models.Q(meta_title='') &
            models.Q(meta_description='') &
            models.Q(meta_keywords='')
        )
    
    def without_seo(self):
        """Return objects that don't have SEO data."""
        return self.get_queryset().filter(
            models.Q(meta_title='') |
            models.Q(meta_description='') |
            models.Q(meta_keywords='')
        )
