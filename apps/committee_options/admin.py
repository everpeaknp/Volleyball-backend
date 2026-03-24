from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from .models import (
    CommitteePageProxy, CommitteeHeroProxy, CommitteeExecutiveProxy,
    CommitteeGroupProxy, CommitteeTitleProxy, 
    CommitteeHero, ExecutiveMember, CommitteeMember, CommitteeGroup, CommitteeSectionSettings
)

# --- Inlines ---

class CommitteeHeroInline(StackedInline):
    model = CommitteeHero
    can_delete = False
    fieldsets = (
        (None, {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('subtitle_ne', 'subtitle_en', 'subtitle_de'),
                ('background_image', 'background_color'),
            )
        }),
    )

class ExecutiveMemberInline(StackedInline):
    model = ExecutiveMember
    extra = 1
    tab = True
    fieldsets = (
        (None, {
            'fields': (
                'name',
                ('role_ne', 'role_en', 'role_de'),
                ('desc_ne', 'desc_en', 'desc_de'),
                ('image', 'email'),
                'order'
            )
        }),
    )

class CommitteeMemberInline(TabularInline):
    model = CommitteeMember
    extra = 1
    tab = True
    verbose_name = "Member"
    verbose_name_plural = "Members"
    fields = ('name_ne', 'name_en', 'name_de', 'name', 'image', 'order')

class CommitteeGroupInline(StackedInline):
    model = CommitteeGroup
    extra = 1
    tab = True
    verbose_name = "Committee Group"
    verbose_name_plural = "Committee Groups"
    fieldsets = (
        (None, {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                'order',
            )
        }),
    )

class CommitteeSectionSettingsInline(StackedInline):
    model = CommitteeSectionSettings
    can_delete = False
    fieldsets = (
        (None, {
            'fields': (
                ('member_section_title_ne', 'member_section_title_en', 'member_section_title_de'),
            )
        }),
    )

# --- Admin Classes ---

@admin.register(CommitteePageProxy)
class CommitteePageProxyAdmin(ModelAdmin):
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

# Common exclude list for component proxies
COMPONENT_EXCLUDE = (
    'status', 'published_at',
    'meta_title_ne', 'meta_title_en', 'meta_title_de',
    'meta_description_ne', 'meta_description_en', 'meta_description_de',
    'meta_keywords',
    'og_title_ne', 'og_title_en', 'og_title_de',
    'og_description_ne', 'og_description_en', 'og_description_de',
    'og_image', 'canonical_url',
)

@admin.register(CommitteeHeroProxy)
class CommitteeHeroProxyAdmin(ModelAdmin):
    inlines = [CommitteeHeroInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')

@admin.register(CommitteeExecutiveProxy)
class CommitteeExecutiveProxyAdmin(ModelAdmin):
    inlines = [ExecutiveMemberInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')

@admin.register(CommitteeGroupProxy)
class CommitteeGroupProxyAdmin(ModelAdmin):
    inlines = [CommitteeGroupInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')

@admin.register(CommitteeTitleProxy)
class CommitteeTitleProxyAdmin(ModelAdmin):
    inlines = [CommitteeSectionSettingsInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')

# Separately manage members if needed, or better, include them in Group admin if possible.
# Django Unfold might not supported nested inlines well out of the box, 
# so we'll register CommitteeGroup directly too for member management.
@admin.register(CommitteeGroup)
class CommitteeGroupAdmin(ModelAdmin):
    inlines = [CommitteeMemberInline]
    list_display = ('title_en', 'page', 'order')
    list_filter = ('page',)
