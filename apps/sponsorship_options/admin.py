from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    SponsorshipPageProxy, SponsorshipHeroProxy, SponsorsProxy, SponsorshipFormProxy,
    SponsorshipHero, Sponsor, SponsorshipFormSettings, SponsorshipApplication
)

# --- Inlines ---

class SponsorshipHeroInline(StackedInline):
    model = SponsorshipHero
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

class SponsorInline(TabularInline):
    model = Sponsor
    extra = 3
    fieldsets = (
        (None, {
            'fields': (
                ('name_ne', 'name_en', 'name_de'),
                ('logo', 'link', 'order', 'is_active'),
            )
        }),
    )

class SponsorshipFormSettingsInline(StackedInline):
    model = SponsorshipFormSettings
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
                ('label_type_ne', 'label_type_en', 'label_type_de'),
                ('label_amount_ne', 'label_amount_en', 'label_amount_de'),
                ('label_voucher_ne', 'label_voucher_en', 'label_voucher_de'),
                ('label_message_ne', 'label_message_en', 'label_message_de'),
                ('label_submit_ne', 'label_submit_en', 'label_submit_de'),
            )
        }),
        ('Selection Options', {
            'classes': ('collapse',),
            'description': 'Comma-separated values for dropdowns',
            'fields': (
                ('options_type_ne', 'options_type_en', 'options_type_de'),
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

@admin.register(SponsorshipPageProxy)
class SponsorshipPageProxyAdmin(ModelAdmin):
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

@admin.register(SponsorshipHeroProxy)
class SponsorshipHeroProxyAdmin(ModelAdmin):
    inlines = [SponsorshipHeroInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')

@admin.register(SponsorsProxy)
class SponsorsProxyAdmin(ModelAdmin):
    inlines = [SponsorInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')

@admin.register(SponsorshipFormProxy)
class SponsorshipFormProxyAdmin(ModelAdmin):
    inlines = [SponsorshipFormSettingsInline]
    exclude = COMPONENT_EXCLUDE
    list_display = ('__str__', 'updated_at')

@admin.register(SponsorshipApplication)
class SponsorshipApplicationAdmin(ModelAdmin):
    list_display = ('name', 'email', 'sponsorship_type', 'amount', 'is_approved', 'created_at')
    list_filter = ('sponsorship_type', 'is_approved', 'created_at')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    actions = ['approve_applications']
    
    fieldsets = (
        ('Status', {
            'fields': ('is_approved',)
        }),
        ('Sponsor Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Sponsorship Details', {
            'fields': ('sponsorship_type', 'amount', 'bank_voucher', 'message')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    @admin.action(description="Approve selected sponsorship applications")
    def approve_applications(self, request, queryset):
        count = 0
        for application in queryset.filter(is_approved=False):
            application.is_approved = True
            application.save()
            count += 1
        
        self.message_user(request, f"Successfully approved {count} applications and sent notification emails.")
