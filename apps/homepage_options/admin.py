from django.contrib import admin
from django.utils.html import mark_safe
from unfold.admin import ModelAdmin, TabularInline
from .models import (
    HomePageProxy, HomeHeroProxy, HomeIntroProxy, HomeMissionProxy, 
    HomeObjectiveProxy, HomeMottoProxy, HomeStatProxy
)

@admin.register(HomePageProxy)
class HomePageProxyAdmin(ModelAdmin):
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

@admin.register(HomeHeroProxy)
class HomeHeroProxyAdmin(ModelAdmin):
    list_display = ('title_en', 'page')
    readonly_fields = ('_preview_video', '_preview_image')
    fieldsets = (
        ('Content', {
            'classes': ('tab',),
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('subtitle_ne', 'subtitle_en', 'subtitle_de'),
                ('cta_join_label_ne', 'cta_join_label_en', 'cta_join_label_de'),
                ('cta_learn_label_ne', 'cta_learn_label_en', 'cta_learn_label_de'),
            )
        }),
        ('Media', {
            'classes': ('tab',),
            'fields': (
                ('video_file', 'video_url'),
                '_preview_video',
                ('image', 'image_url'),
                '_preview_image',
            )
        }),
    )

    def _preview_video(self, obj):
        if obj.video_url:
            return mark_safe(f'<iframe width="320" height="180" src="{obj.video_url}" frameborder="0" allowfullscreen></iframe>')
        if obj.video_file:
            return mark_safe(f'<video width="320" height="180" controls><source src="{obj.video_file.url}" type="video/mp4">Your browser does not support the video tag.</video>')
        return "No video uploaded"
    _preview_video.short_description = "Video Preview"

    def _preview_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px; max-width: 100%;" />')
        if obj.image_url:
            return mark_safe(f'<img src="{obj.image_url}" style="max-height: 200px; max-width: 100%;" />')
        return "No image uploaded"
    _preview_image.short_description = "Image Preview"

@admin.register(HomeIntroProxy)
class HomeIntroProxyAdmin(ModelAdmin):
    list_display = ('title_en', 'page')
    readonly_fields = ('_preview_image',)
    fieldsets = (
        ('Header', {
            'classes': ('tab',),
            'fields': (
                ('mini_header_ne', 'mini_header_en', 'mini_header_de'),
                ('title_ne', 'title_en', 'title_de'),
            )
        }),
        ('Description', {
            'classes': ('tab',),
            'fields': (
                'text_ne', 'text_en', 'text_de',
                'subtext_ne', 'subtext_en', 'subtext_de',
            )
        }),
        ('Media', {
            'classes': ('tab',),
            'fields': (
                ('image', 'image_url'),
                '_preview_image',
            )
        }),
    )

    def _preview_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px; max-width: 100%;" />')
        if obj.image_url:
            return mark_safe(f'<img src="{obj.image_url}" style="max-height: 200px; max-width: 100%;" />')
        return "No image uploaded"
    _preview_image.short_description = "Image Preview"

@admin.register(HomeObjectiveProxy)
class HomeObjectiveProxyAdmin(ModelAdmin):
    list_display = ('text_en', 'order', 'mission')
    list_editable = ('order',)
    fieldsets = (
        ('Content', {
            'classes': ('tab',),
            'fields': (
                'mission',
                ('goal_prefix_ne', 'goal_prefix_en', 'goal_prefix_de'),
                ('text_ne', 'text_en', 'text_de'),
                ('badge_number', 'order'),
            )
        }),
        ('Image', {
            'classes': ('tab',),
            'fields': (
                ('image', 'image_url'),
            )
        }),
    )

class HomeObjectiveInline(TabularInline):
    model = HomeObjectiveProxy
    fk_name = 'mission'
    extra = 1
    readonly_fields = ('_preview_image',)
    fields = (
        'order', 'badge_number',
        'goal_prefix_ne', 'goal_prefix_en', 'goal_prefix_de',
        'text_ne', 'text_en', 'text_de',
        'image', 'image_url', '_preview_image'
    )
    
    def _preview_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px; max-width: 50px;" />')
        if obj.image_url:
            return mark_safe(f'<img src="{obj.image_url}" style="max-height: 50px; max-width: 50px;" />')
        return ""
    _preview_image.short_description = "Preview"

@admin.register(HomeMissionProxy)
class HomeMissionProxyAdmin(ModelAdmin):
    list_display = ('title_en', 'page')
    inlines = [HomeObjectiveInline]
    fieldsets = (
        ('Mission', {
            'classes': ('tab',),
            'fields': (
                ('mission_label_ne', 'mission_label_en', 'mission_label_de'),
                ('title_ne', 'title_en', 'title_de'),
            )
        }),
        ('Description', {
            'classes': ('tab',),
            'fields': (
                'description_ne', 'description_en', 'description_de',
            )
        }),
    )

@admin.register(HomeMottoProxy)
class HomeMottoProxyAdmin(ModelAdmin):
    list_display = ('text_en', 'page')
    fieldsets = (
        ('Motto', {
            'classes': ('tab',),
            'fields': (
                ('text_ne', 'text_en', 'text_de'),
                ('button_label_ne', 'button_label_en', 'button_label_de'),
            )
        }),
    )

@admin.register(HomeStatProxy)
class HomeStatProxyAdmin(ModelAdmin):
    list_display = ('label_en', 'value', 'suffix', 'order', 'page')
    list_editable = ('value', 'order', 'suffix')
    fieldsets = (
        ('Stats', {
            'classes': ('tab',),
            'fields': (
                'page',
                'label_ne', 'label_en', 'label_de',
                'value', 'suffix', 'order',
            )
        }),
    )
