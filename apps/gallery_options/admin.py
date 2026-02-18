from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline, StackedInline, TabularInline
from .models import (
    GalleryPage, GalleryHero, GallerySettings, GalleryCategory, GalleryImage,
    GalleryPageProxy, GalleryHeroProxy, GalleryCategoriesProxy, GalleryImagesProxy, GalleryLabelsProxy
)

class GalleryHeroInline(StackedInline):
    model = GalleryHero
    can_delete = False
    fieldsets = (
        (None, {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('text_ne', 'text_en', 'text_de'),
            )
        }),
    )

class GallerySettingsInline(StackedInline):
    model = GallerySettings
    can_delete = False
    fieldsets = (
        ('Empty State Labels', {
            'fields': (
                ('no_images_text_ne', 'no_images_text_en', 'no_images_text_de'),
            )
        }),
    )

class GalleryImageInline(StackedInline):
    model = GalleryImage
    extra = 1
    tab = True
    fieldsets = (
        (None, {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('category', 'order'),
                ('image', 'image_url'),
            )
        }),
    )

# --- Common Exclude ---
COMPONENT_EXCLUDE = (
    'status', 'published_at',
    'meta_title_ne', 'meta_title_en', 'meta_title_de',
    'meta_description_ne', 'meta_description_en', 'meta_description_de',
    'meta_keywords',
    'og_title_ne', 'og_title_en', 'og_title_de',
    'og_description_ne', 'og_description_en', 'og_description_de',
    'og_image', 'canonical_url',
)

@admin.register(GalleryPageProxy)
class GalleryPageAdmin(ModelAdmin):
    list_display = ['__str__', 'status']
    fieldsets = (
        ('SEO Settings', {
            'classes': ('tab',),
            'fields': (
                ('meta_title_ne', 'meta_title_en', 'meta_title_de'),
                ('meta_description_ne', 'meta_description_en', 'meta_description_de'),
                'meta_keywords',
                ('og_title_ne', 'og_title_en', 'og_title_de'),
                ('og_description_ne', 'og_description_en', 'og_description_de'),
                'og_image',
                'canonical_url',
            )
        }),
        ('Metadata', {
            'classes': ('tab',),
            'fields': ('status', 'published_at')
        }),
    )

@admin.register(GalleryHeroProxy)
class GalleryHeroAdmin(ModelAdmin):
    exclude = COMPONENT_EXCLUDE
    inlines = [GalleryHeroInline]
    def has_add_permission(self, request): return False

@admin.register(GalleryCategoriesProxy)
class GalleryCategoryAdmin(ModelAdmin):
    list_display = ['name_en', 'name_ne', 'name_de', 'order']
    list_editable = ['order']

@admin.register(GalleryImagesProxy)
class GalleryImagesAdmin(ModelAdmin):
    exclude = COMPONENT_EXCLUDE
    inlines = [GalleryImageInline]
    def has_add_permission(self, request): return False

@admin.register(GalleryLabelsProxy)
class GalleryLabelsAdmin(ModelAdmin):
    exclude = COMPONENT_EXCLUDE
    inlines = [GallerySettingsInline]
    def has_add_permission(self, request): return False
