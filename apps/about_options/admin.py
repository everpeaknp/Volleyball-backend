from django.contrib import admin
from django.utils.html import mark_safe
from unfold.admin import ModelAdmin, TabularInline
from .models import (
    AboutPageProxy, AboutHeroProxy, AboutIntroProxy,
    AboutCoreProxy, AboutStrategicProxy, AboutStat, AboutObjective
)

# --- Inlines ---

class AboutStatInline(TabularInline):
    model = AboutStat
    extra = 1
    tab = True
    verbose_name = "Stat"
    verbose_name_plural = "Statistics List"

class AboutObjectiveInline(TabularInline):
    model = AboutObjective
    extra = 1
    tab = True
    verbose_name = "Objective"
    verbose_name_plural = "Objectives List"

# --- Admin Classes ---

@admin.register(AboutPageProxy)
class AboutPageProxyAdmin(ModelAdmin):
    list_display = ('__str__', 'status', 'updated_at')
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

@admin.register(AboutHeroProxy)
class AboutHeroProxyAdmin(ModelAdmin):
    list_display = ('title_en', 'page')
    fieldsets = (
        ('Badge', {
            'classes': ('tab',),
            'fields': (
                ('since_text_ne', 'since_text_en', 'since_text_de'),
                'show_pulsing_dot',
            )
        }),
        ('Content', {
            'classes': ('tab',),
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('text_ne', 'text_en', 'text_de'),
                ('background_color',),
            )
        }),
        ('Design', {
            'classes': ('tab',),
            'fields': (
                'background_image',
            )
        }),
    )

@admin.register(AboutIntroProxy)
class AboutIntroProxyAdmin(ModelAdmin):
    inlines = [AboutStatInline]
    list_display = ('title_part1_en', 'page')
    fieldsets = (
        ('Header & Narrative', {
            'classes': ('tab',),
            'fields': (
                ('title_part1_ne', 'title_part1_en', 'title_part1_de'),
                ('title_part2_ne', 'title_part2_en', 'title_part2_de'),
                ('text1_ne', 'text1_en', 'text1_de'),
                ('text2_ne', 'text2_en', 'text2_de'),
            )
        }),
        ('Media & Metadata', {
            'classes': ('tab',),
            'fields': (
                ('main_image', 'secondary_image'),
                ('established_label_ne', 'established_label_en', 'established_label_de'),
                'established_year',
            )
        }),
    )

@admin.register(AboutCoreProxy)
class AboutCoreProxyAdmin(ModelAdmin):
    list_display = ('title_en', 'page')
    fieldsets = (
        ('Header', {
            'classes': ('tab',),
            'fields': (('title_ne', 'title_en', 'title_de'),),
        }),
        ('Vision', {
            'classes': ('tab',),
            'fields': (
                ('vision_title_ne', 'vision_title_en', 'vision_title_de'),
                ('vision_text_ne', 'vision_text_en', 'vision_text_de'),
                'vision_icon',
            )
        }),
        ('Mission', {
            'classes': ('tab',),
            'fields': (
                ('mission_title_ne', 'mission_title_en', 'mission_title_de'),
                ('mission_text_ne', 'mission_text_en', 'mission_text_de'),
                'mission_icon',
            )
        }),
    )

@admin.register(AboutStrategicProxy)
class AboutStrategicProxyAdmin(ModelAdmin):
    inlines = [AboutObjectiveInline]
    list_display = ('strategic_title_en', 'page')
    fieldsets = (
        ('Strategic Context', {
            'classes': ('tab',),
            'fields': (
                ('strategic_title_ne', 'strategic_title_en', 'strategic_title_de'),
                ('objectives_title_ne', 'objectives_title_en', 'objectives_title_de'),
            )
        }),
        ('Section Promo', {
            'classes': ('tab',),
            'fields': (
                ('promo_title_ne', 'promo_title_en', 'promo_title_de'),
                ('promo_text_ne', 'promo_text_en', 'promo_text_de'),
                'promo_icon',
                'side_image',
            )
        }),
    )
