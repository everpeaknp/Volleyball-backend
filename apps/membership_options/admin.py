from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from .models import (
    MembershipPageProxy, MembershipHeroProxy, MembershipBenefitsProxy, MembershipFormProxy,
    MembershipHero, MembershipBenefit, MembershipFormSettings
)

# --- Inlines ---

class MembershipHeroInline(StackedInline):
    model = MembershipHero
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

class MembershipBenefitInline(StackedInline):
    model = MembershipBenefit
    extra = 1
    tab = True
    fieldsets = (
        (None, {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('desc_ne', 'desc_en', 'desc_de'),
                ('icon', 'order'),
            )
        }),
    )

class MembershipFormSettingsInline(StackedInline):
    model = MembershipFormSettings
    can_delete = False
    fieldsets = (
        ('Header & Success Message', {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('text_ne', 'text_en', 'text_de'),
                ('success_title_ne', 'success_title_en', 'success_title_de'),
                ('success_text_ne', 'success_text_en', 'success_text_de'),
            )
        }),
        ('Form Labels', {
            'classes': ('collapse',),
            'fields': (
                ('label_name_ne', 'label_name_en', 'label_name_de'),
                ('label_email_ne', 'label_email_en', 'label_email_de'),
                ('label_phone_ne', 'label_phone_en', 'label_phone_de'),
                ('label_address_ne', 'label_address_en', 'label_address_de'),
                ('label_dob_ne', 'label_dob_en', 'label_dob_de'),
                ('label_gender_ne', 'label_gender_en', 'label_gender_de'),
                ('label_experience_ne', 'label_experience_en', 'label_experience_de'),
                ('label_position_ne', 'label_position_en', 'label_position_de'),
                ('label_reason_ne', 'label_reason_en', 'label_reason_de'),
                ('label_submit_ne', 'label_submit_en', 'label_submit_de'),
            )
        }),
        ('Selection Options', {
            'classes': ('collapse',),
            'description': 'Comma-separated values for dropdowns',
            'fields': (
                ('options_gender_ne', 'options_gender_en', 'options_gender_de'),
                ('options_experience_ne', 'options_experience_en', 'options_experience_de'),
                ('options_position_ne', 'options_position_en', 'options_position_de'),
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

@admin.register(MembershipPageProxy)
class MembershipPageProxyAdmin(ModelAdmin):
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

@admin.register(MembershipHeroProxy)
class MembershipHeroProxyAdmin(ModelAdmin):
    inlines = [MembershipHeroInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')

@admin.register(MembershipBenefitsProxy)
class MembershipBenefitsProxyAdmin(ModelAdmin):
    inlines = [MembershipBenefitInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')

@admin.register(MembershipFormProxy)
class MembershipFormProxyAdmin(ModelAdmin):
    inlines = [MembershipFormSettingsInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')
