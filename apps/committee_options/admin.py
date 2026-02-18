from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline, TabularInline, StackedInline
from .models import (
    CommitteePageProxy, CommitteeHeroProxy, CommitteeExecutiveProxy,
    CommitteeGeneralProxy, CommitteeTitleProxy, 
    CommitteeHero, CommitteeBoard, CommitteeMember, CommitteeSectionSettings
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

class CommitteeBoardInline(StackedInline):
    model = CommitteeBoard
    can_delete = False
    fieldsets = (
        ('President', {
            'fields': (
                'pres_name',
                ('pres_role_ne', 'pres_role_en', 'pres_role_de'),
                ('pres_desc_ne', 'pres_desc_en', 'pres_desc_de'),
                ('pres_image', 'pres_email'),
            )
        }),
        ('Secretary', {
            'fields': (
                'sec_name',
                ('sec_role_ne', 'sec_role_en', 'sec_role_de'),
                ('sec_desc_ne', 'sec_desc_en', 'sec_desc_de'),
                ('sec_image', 'sec_email'),
            )
        }),
        ('Treasurer', {
            'fields': (
                'tres_name',
                ('tres_role_ne', 'tres_role_en', 'tres_role_de'),
                ('tres_desc_ne', 'tres_desc_en', 'tres_desc_de'),
                ('tres_image', 'tres_email'),
            )
        }),
    )

class CommitteeGeneralInline(TabularInline):
    model = CommitteeMember
    extra = 1
    tab = True
    verbose_name = "General Member"
    verbose_name_plural = "General Committee Members"
    fields = ('name', 'image', 'order')

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
    
    def get_queryset(self, request):
        return super().get_queryset(request)

@admin.register(CommitteeExecutiveProxy)
class CommitteeExecutiveProxyAdmin(ModelAdmin):
    inlines = [CommitteeBoardInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')

@admin.register(CommitteeGeneralProxy)
class CommitteeGeneralProxyAdmin(ModelAdmin):
    inlines = [CommitteeGeneralInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')

@admin.register(CommitteeTitleProxy)
class CommitteeTitleProxyAdmin(ModelAdmin):
    inlines = [CommitteeSectionSettingsInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')
