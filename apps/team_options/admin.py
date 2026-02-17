from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from .models import (
    TeamPageProxy, TeamHeroProxy, TeamCoachesProxy, TeamPlayersProxy, TeamPhotoCTAProxy,
    TeamHero, Coach, Player, TeamPhotoSection, TeamCTA, TeamCoachesSettings, TeamPlayersSettings
)

# --- Inlines ---

class TeamHeroInline(StackedInline):
    model = TeamHero
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

class TeamCoachesSettingsInline(StackedInline):
    model = TeamCoachesSettings
    can_delete = False
    fieldsets = (
        ('Section Title', {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
            )
        }),
    )

class TeamPlayersSettingsInline(StackedInline):
    model = TeamPlayersSettings
    can_delete = False
    fieldsets = (
        ('Section Title', {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
            )
        }),
    )

class CoachInline(StackedInline):
    model = Coach
    extra = 1
    tab = True
    fieldsets = (
        (None, {
            'fields': (
                ('name_ne', 'name_en', 'name_de'),
                ('role_ne', 'role_en', 'role_de'),
                ('experience_ne', 'experience_en', 'experience_de'),
                ('image', 'order'),
            )
        }),
    )

class PlayerInline(StackedInline):
    model = Player
    extra = 1
    tab = True
    fieldsets = (
        (None, {
            'fields': (
                ('name_ne', 'name_en', 'name_de'),
                'number',
                ('position_ne', 'position_en', 'position_de'),
                ('image', 'order'),
            )
        }),
    )

class TeamPhotoInline(StackedInline):
    model = TeamPhotoSection
    can_delete = False
    fieldsets = (
        (None, {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('subtitle_ne', 'subtitle_en', 'subtitle_de'),
                ('image', 'image_url'),
            )
        }),
    )

class TeamCTAInline(StackedInline):
    model = TeamCTA
    can_delete = False
    fieldsets = (
        (None, {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('text_ne', 'text_en', 'text_de'),
                ('button_label_ne', 'button_label_en', 'button_label_de'),
                'button_link',
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

# --- Admin Classes ---

@admin.register(TeamPageProxy)
class TeamPageProxyAdmin(ModelAdmin):
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

@admin.register(TeamHeroProxy)
class TeamHeroProxyAdmin(ModelAdmin):
    inlines = [TeamHeroInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')

@admin.register(TeamCoachesProxy)
class TeamCoachesProxyAdmin(ModelAdmin):
    inlines = [TeamCoachesSettingsInline, CoachInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')

@admin.register(TeamPlayersProxy)
class TeamPlayersProxyAdmin(ModelAdmin):
    inlines = [TeamPlayersSettingsInline, PlayerInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')

@admin.register(TeamPhotoCTAProxy)
class TeamPhotoCTAProxyAdmin(ModelAdmin):
    inlines = [TeamPhotoInline, TeamCTAInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')
