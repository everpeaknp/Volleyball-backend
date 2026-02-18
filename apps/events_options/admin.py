from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline, StackedInline, TabularInline
from .models import (
    EventsPage, EventsHero, EventsSettings, Event,
    EventsPageProxy, EventsHeroProxy, EventsManagementProxy, EventsLabelsProxy
)

class EventsHeroInline(StackedInline):
    model = EventsHero
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

class EventsSettingsInline(StackedInline):
    model = EventsSettings
    can_delete = False
    fieldsets = (
        ('Section Titles', {
            'fields': (
                ('upcoming_title_ne', 'upcoming_title_en', 'upcoming_title_de'),
                ('past_title_ne', 'past_title_en', 'past_title_de'),
            )
        }),
        ('Labels & Buttons', {
            'fields': (
                ('register_btn_ne', 'register_btn_en', 'register_btn_de'),
                ('label_upcoming_ne', 'label_upcoming_en', 'label_upcoming_de'),
                ('label_past_ne', 'label_past_en', 'label_past_de'),
            )
        }),
    )

class EventInline(StackedInline):
    model = Event
    extra = 1
    tab = True
    fieldsets = (
        (None, {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('description_ne', 'description_en', 'description_de'),
                ('date_text_ne', 'date_text_en', 'date_text_de'),
                ('time', 'is_past', 'order'),
                ('location_ne', 'location_en', 'location_de'),
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

@admin.register(EventsPageProxy)
class EventsPageAdmin(ModelAdmin):
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

@admin.register(EventsHeroProxy)
class EventsHeroAdmin(ModelAdmin):
    exclude = COMPONENT_EXCLUDE
    inlines = [EventsHeroInline]
    def has_add_permission(self, request): return False

@admin.register(EventsManagementProxy)
class EventsManagementAdmin(ModelAdmin):
    exclude = COMPONENT_EXCLUDE
    inlines = [EventInline]
    def has_add_permission(self, request): return False

@admin.register(EventsLabelsProxy)
class EventsLabelsAdmin(ModelAdmin):
    exclude = COMPONENT_EXCLUDE
    inlines = [EventsSettingsInline]
    def has_add_permission(self, request): return False
