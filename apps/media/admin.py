from django.contrib import admin
from .models import Media

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_type', 'created_at')
    search_fields = ('title', 'alt_text_en', 'alt_text_ne', 'alt_text_de')
    list_filter = ('file_type', 'created_at')
    readonly_fields = ('size', 'width', 'height')
