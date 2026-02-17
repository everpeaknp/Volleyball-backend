from django.contrib import admin
from django.utils.html import mark_safe
from unfold.admin import ModelAdmin, TabularInline
from .models import NavigationSettings, NavigationItem, FooterSettings, FooterLink

@admin.register(NavigationSettings)
class NavigationSettingsAdmin(ModelAdmin):
    readonly_fields = ('logo_preview',)
    fieldsets = (
        ('Identity', {
            'classes': ('tab',),
            'fields': (
                ('brand_name_main_ne', 'brand_name_main_en', 'brand_name_main_de'),
                ('brand_name_secondary_ne', 'brand_name_secondary_en', 'brand_name_secondary_de'),
                'logo', 'logo_preview',
            )
        }),
        ('Status', {
            'classes': ('tab',),
            'fields': (('status', 'published_at'),),
        }),
    )

    def logo_preview(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" style="max-height: 100px; border-radius: 8px; border: 1px solid #e5e7eb;" />')
        return "No logo uploaded."
    logo_preview.short_description = "Preview"

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

class FooterLinkInline(TabularInline):
    model = FooterLink
    extra = 0
    fields = ('order', 'url', 'label_ne', 'label_en', 'label_de')

@admin.register(FooterSettings)
class FooterSettingsAdmin(ModelAdmin):
    inlines = [FooterLinkInline]
    list_display = ('__str__', 'status', 'updated_at')
    readonly_fields = ('logo_preview',)
    fieldsets = (
        ('Identity', {
            'classes': ('tab',),
            'fields': (
                ('brand_name_main_ne', 'brand_name_main_en', 'brand_name_main_de'),
                ('brand_name_secondary_ne', 'brand_name_secondary_en', 'brand_name_secondary_de'),
                'logo', 'logo_preview',
            )
        }),
        ('Description', {
            'classes': ('tab',),
            'fields': (
                'description_ne', 'description_en', 'description_de',
            )
        }),
        ('Social', {
            'classes': ('tab',),
            'fields': (
                ('facebook_url', 'instagram_url', 'youtube_url'),
            )
        }),
        ('Headers', {
            'classes': ('tab',),
            'fields': (
                ('quick_links_title_ne', 'quick_links_title_en', 'quick_links_title_de'),
                ('contact_info_title_ne', 'contact_info_title_en', 'contact_info_title_de'),
            )
        }),
        ('Contact', {
            'classes': ('tab',),
            'fields': (
                ('address_ne', 'address_en', 'address_de'),
                ('phone', 'email', 'registered_info'),
            )
        }),
        ('Membership', {
            'classes': ('tab',),
            'fields': (
                ('membership_title_ne', 'membership_title_en', 'membership_title_de'),
                'membership_description_ne', 'membership_description_en', 'membership_description_de',
                ('membership_button_text_ne', 'membership_button_text_en', 'membership_button_text_de'),
            )
        }),
        ('Legal', {
            'classes': ('tab',),
            'fields': (
                ('copyright_text_ne', 'copyright_text_en', 'copyright_text_de'),
                ('privacy_label_ne', 'privacy_label_en', 'privacy_label_de'),
                ('terms_label_ne', 'terms_label_en', 'terms_label_de'),
            )
        }),
        ('Metadata', {
            'classes': ('tab',),
            'fields': (('status', 'published_at'),),
        }),
    )

    def logo_preview(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" style="max-height: 100px; border-radius: 8px; border: 1px solid #e5e7eb;" />')
        return "No logo uploaded."
    logo_preview.short_description = "Preview"

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(NavigationItem)
class NavigationItemAdmin(ModelAdmin):
    list_display = ('label_en', 'href', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('label_en', 'label_ne', 'label_de', 'href')
    fieldsets = (
        ('Item', {
            'classes': ('tab',),
            'fields': (
                'order',
                'href',
                ('label_ne', 'label_en', 'label_de'),
                'is_active',
            )
        }),
    )
