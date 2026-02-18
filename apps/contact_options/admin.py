from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline, StackedInline, TabularInline
from .models import (
    ContactPage, ContactHero, ContactInfo, ContactSocial, ContactSettings, ContactSubmission,
    ContactPageProxy, ContactHeroProxy, ContactInfoProxy, ContactSocialProxy, ContactLabelsProxy
)

class ContactHeroInline(StackedInline):
    model = ContactHero
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

class ContactInfoInline(StackedInline):
    model = ContactInfo
    extra = 1
    tab = True
    fieldsets = (
        (None, {
            'fields': (
                ('label_ne', 'label_en', 'label_de'),
                'value',
                ('icon', 'order'),
            )
        }),
    )

class ContactSocialInline(StackedInline):
    model = ContactSocial
    extra = 1
    tab = True
    fieldsets = (
        (None, {
            'fields': (
                'platform',
                'url',
                ('icon', 'order'),
            )
        }),
    )

class ContactSettingsInline(StackedInline):
    model = ContactSettings
    can_delete = False
    fieldsets = (
        ('Section Titles', {
            'fields': (
                ('info_section_title_ne', 'info_section_title_en', 'info_section_title_de'),
                ('social_section_title_ne', 'social_section_title_en', 'social_section_title_de'),
                ('form_title_ne', 'form_title_en', 'form_title_de'),
            )
        }),
        ('Form Labels', {
            'classes': ('collapse',),
            'fields': (
                ('label_name_ne', 'label_name_en', 'label_name_de'),
                ('label_email_ne', 'label_email_en', 'label_email_de'),
                ('label_subject_ne', 'label_subject_en', 'label_subject_de'),
                ('label_message_ne', 'label_message_en', 'label_message_de'),
                ('label_submit_ne', 'label_submit_en', 'label_submit_de'),
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

@admin.register(ContactPageProxy)
class ContactPageAdmin(ModelAdmin):
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

@admin.register(ContactHeroProxy)
class ContactHeroAdmin(ModelAdmin):
    exclude = COMPONENT_EXCLUDE
    inlines = [ContactHeroInline]
    def has_add_permission(self, request): return False

@admin.register(ContactInfoProxy)
class ContactInfoAdmin(ModelAdmin):
    exclude = COMPONENT_EXCLUDE
    inlines = [ContactInfoInline]
    def has_add_permission(self, request): return False

@admin.register(ContactSocialProxy)
class ContactSocialAdmin(ModelAdmin):
    exclude = COMPONENT_EXCLUDE
    inlines = [ContactSocialInline]
    def has_add_permission(self, request): return False

@admin.register(ContactLabelsProxy)
class ContactLabelsAdmin(ModelAdmin):
    exclude = COMPONENT_EXCLUDE
    inlines = [ContactSettingsInline]
    def has_add_permission(self, request): return False

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Contact Details', {
            'fields': ('name', 'email', 'subject')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
