from django.contrib import admin
from .models import Member, Article, Notice, Event, GalleryImage

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'member_type', 'role_en', 'status')
    list_filter = ('member_type', 'status')
    search_fields = ('name', 'role_en', 'bio_en')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'category_en', 'is_featured', 'status')
    list_filter = ('category_en', 'is_featured', 'status')
    search_fields = ('title_en', 'excerpt_en')
    prepopulated_fields = {'slug': ('title_en',)}

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'category_en', 'date', 'status')
    list_filter = ('category_en', 'status')
    search_fields = ('title_en', 'content_en')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'date', 'location', 'event_status', 'status')
    list_filter = ('event_status', 'status')
    search_fields = ('title_en', 'location')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'category_en', 'status')
    list_filter = ('category_en', 'status')
    search_fields = ('title_en',)
