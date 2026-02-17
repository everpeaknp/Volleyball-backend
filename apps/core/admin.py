from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import GlobalStyles

@admin.register(GlobalStyles)
class GlobalStylesAdmin(ModelAdmin):
    list_display = ('brand_name_en', 'primary_500', 'secondary_500', 'accent_500')
    fieldsets = (
        ('Identity', {
            'classes': ('tab',),
            'fields': (
                ('brand_name_ne', 'brand_name_en', 'brand_name_de'),
                ('brand_subtitle_ne', 'brand_subtitle_en', 'brand_subtitle_de'),
            )
        }),
        ('Colors', {
            'classes': ('tab',),
            'fields': (
                ('primary_500', 'primary_600'),
                ('secondary_500', 'accent_500'),
            )
        }),
        ('Patterns', {
            'classes': ('tab',),
            'fields': (
                ('enable_nepal_pattern', 'enable_volleyball_pattern'),
                'nepal_pattern_svg', 'volleyball_pattern_svg',
            )
        }),
        ('Config', {
            'classes': ('tab',),
            'fields': ('transition_duration',)
        })
    )
