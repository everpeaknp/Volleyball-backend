from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import (
    NoticePage, NoticeHero, NoticeCTA, NoticeCategory, Notice,
    NoticePageProxy, NoticeHeroProxy
)

# --- Inlines ---

class NoticeHeroInline(StackedInline):
    model = NoticeHero
    can_delete = False
    fieldsets = (
        (None, {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('text_ne', 'text_en', 'text_de'),
            )
        }),
    )

class NoticeCTAInline(StackedInline):
    model = NoticeCTA
    can_delete = False
    fieldsets = (
        ('CTA Section', {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('text_ne', 'text_en', 'text_de'),
                ('button_text_ne', 'button_text_en', 'button_text_de'),
                'button_icon',
            )
        }),
    )

class NoticeInline(StackedInline):
    model = Notice
    extra = 1
    tab = True
    fieldsets = (
        (None, {
            'fields': (
                ('title_ne', 'title_en', 'title_de'),
                ('content_ne', 'content_en', 'content_de'),
                ('category', 'icon', 'order'),
                ('date_text_ne', 'date_text_en', 'date_text_de'),
                'is_published',
            )
        }),
    )

# --- Step-by-Step Admin Structure ---

@admin.register(NoticePageProxy)
class NoticePageProxyAdmin(ModelAdmin):
    list_display = ['id', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = [
        ('Page Status', {
            'fields': ['status', 'published_at']
        }),
        ('SEO - Meta Tags', {
            'fields': [
                ('meta_title_ne', 'meta_title_en', 'meta_title_de'),
                ('meta_description_ne', 'meta_description_en', 'meta_description_de'),
                'meta_keywords'
            ],
            'classes': ['collapse']
        }),
        ('SEO - Open Graph', {
            'fields': [
                ('og_title_ne', 'og_title_en', 'og_title_de'),
                ('og_description_ne', 'og_description_en', 'og_description_de'),
                'og_image', 'canonical_url'
            ],
            'classes': ['collapse']
        }),
        ('Timestamps', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        })
    ]
    
    def response_post_save_add(self, request, obj):
        return HttpResponseRedirect(reverse('admin:notice_options_noticeheroproxy_changelist'))
    
    def response_post_save_change(self, request, obj):
        return HttpResponseRedirect(reverse('admin:notice_options_noticeheroproxy_changelist'))

@admin.register(NoticeHeroProxy)
class NoticeHeroProxyAdmin(ModelAdmin):
    inlines = [NoticeHeroInline]
    
    # Explicitly exclude all page fields
    exclude = [
        'status', 'published_at', 'created_at', 'updated_at',
        'meta_title_ne', 'meta_title_en', 'meta_title_de',
        'meta_description_ne', 'meta_description_en', 'meta_description_de',
        'meta_keywords', 'og_title_ne', 'og_title_en', 'og_title_de',
        'og_description_ne', 'og_description_en', 'og_description_de',
        'og_image', 'canonical_url'
    ]
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        page, created = NoticePage.objects.get_or_create(id=1)
        return qs.filter(id=page.id)
    
    def changelist_view(self, request, extra_context=None):
        page, created = NoticePage.objects.get_or_create(id=1)
        return HttpResponseRedirect(reverse('admin:notice_options_noticeheroproxy_change', args=[page.id]))

# --- Categories Admin ---

@admin.register(NoticeCategory)
class NoticeCategoryAdmin(ModelAdmin):
    list_display = ['name_en', 'name_ne', 'name_de', 'order']
    list_editable = ['order']
    ordering = ['order']
    
    fieldsets = [
        ('Category Names', {
            'fields': [
                ('name_ne', 'name_en', 'name_de'),
                'order'
            ]
        })
    ]

# --- Main Management Admin ---

@admin.register(NoticePage)
class NoticeManagementAdmin(ModelAdmin):
    inlines = [NoticeCTAInline, NoticeInline]
    
    fieldsets = [
        ('Page Status', {
            'fields': ['status'],
            'classes': ['collapse']
        })
    ]
    
    def has_add_permission(self, request):
        return not NoticePage.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        page, created = NoticePage.objects.get_or_create(id=1)
        return qs.filter(id=page.id)
    
    def changelist_view(self, request, extra_context=None):
        page, created = NoticePage.objects.get_or_create(id=1)
        return HttpResponseRedirect(reverse('admin:notice_options_noticepage_change', args=[page.id]))

# --- Individual Notice Admin (for detailed editing) ---

@admin.register(Notice)
class NoticeAdmin(ModelAdmin):
    list_display = ['title_en', 'category', 'date_text_en', 'icon', 'is_published', 'order']
    list_editable = ['order', 'is_published']
    list_filter = ['category', 'is_published']
    search_fields = ['title_en', 'title_ne', 'title_de', 'content_en']
    ordering = ['order']
    
    fieldsets = [
        ('Basic Info', {
            'fields': [
                ('title_ne', 'title_en', 'title_de'),
                'category',
                ('date_text_ne', 'date_text_en', 'date_text_de'),
                'icon',
                ('order', 'is_published')
            ]
        }),
        ('Content', {
            'fields': [
                'content_ne',
                'content_en', 
                'content_de'
            ]
        })
    ]
    
    def save_model(self, request, obj, form, change):
        if not obj.page_id:
            page, created = NoticePage.objects.get_or_create(id=1)
            obj.page = page
        super().save_model(request, obj, form, change)