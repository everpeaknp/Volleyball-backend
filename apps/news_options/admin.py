from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline, TabularInline
from .models import (
    NewsPage, NewsHero, NewsSettings, NewsCategory, NewsArticle,
    NewsPageProxy, NewsHeroProxy, NewsCategoriesProxy, NewsArticlesProxy, NewsLabelsProxy
)

class NewsHeroInline(StackedInline):
    model = NewsHero
    can_delete = False
    fieldsets = (
        (None, {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('text_ne', 'text_en', 'text_de'),
                ('image', 'image_url'),
            )
        }),
    )

class NewsSettingsInline(StackedInline):
    model = NewsSettings
    can_delete = False
    fieldsets = (
        ('Header Labels', {
            'fields': (
                ('featured_label_ne', 'featured_label_en', 'featured_label_de'),
                ('other_news_title_ne', 'other_news_title_en', 'other_news_title_de'),
            )
        }),
        ('Action Buttons', {
            'fields': (
                ('read_more_label_ne', 'read_more_label_en', 'read_more_label_de'),
            )
        }),
    )

class NewsArticleInline(StackedInline):
    model = NewsArticle
    extra = 1
    tab = True
    fieldsets = (
        (None, {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('excerpt_ne', 'excerpt_en', 'excerpt_de'),
                ('category', 'featured', 'order'),
                ('date_text_ne', 'date_text_en', 'date_text_de'),
                ('image', 'image_url'),
            )
        }),
        ('Content', {
            'classes': ('collapse',),
            'fields': (
                'content_ne', 'content_en', 'content_de',
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

@admin.register(NewsPageProxy)
class NewsPageAdmin(ModelAdmin):
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

@admin.register(NewsHeroProxy)
class NewsHeroAdmin(ModelAdmin):
    exclude = COMPONENT_EXCLUDE
    inlines = [NewsHeroInline]
    def has_add_permission(self, request): return False

@admin.register(NewsCategoriesProxy)
class NewsCategoryAdmin(ModelAdmin):
    list_display = ['name_en', 'name_ne', 'name_de', 'order']
    list_editable = ['order']

@admin.register(NewsArticlesProxy)
class NewsArticlesAdmin(ModelAdmin):
    exclude = COMPONENT_EXCLUDE
    inlines = [NewsArticleInline]
    def has_add_permission(self, request): return False

@admin.register(NewsLabelsProxy)
class NewsLabelsAdmin(ModelAdmin):
    exclude = COMPONENT_EXCLUDE
    inlines = [NewsSettingsInline]
    def has_add_permission(self, request): return False
