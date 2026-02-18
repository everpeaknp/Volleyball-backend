from rest_framework import serializers
from .models import NoticePage, NoticeHero, NoticeCTA, NoticeCategory, Notice

class NoticeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeCategory
        fields = ['id', 'name_ne', 'name_en', 'name_de', 'order']

class NoticeSerializer(serializers.ModelSerializer):
    category = NoticeCategorySerializer(read_only=True)
    
    class Meta:
        model = Notice
        fields = [
            'id', 'title_ne', 'title_en', 'title_de',
            'content_ne', 'content_en', 'content_de',
            'date_text_ne', 'date_text_en', 'date_text_de',
            'category', 'icon', 'order', 'is_published'
        ]

class NoticeHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeHero
        fields = ['title_ne', 'title_en', 'title_de', 'text_ne', 'text_en', 'text_de']

class NoticeCTASerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeCTA
        fields = [
            'title_ne', 'title_en', 'title_de',
            'text_ne', 'text_en', 'text_de',
            'button_text_ne', 'button_text_en', 'button_text_de',
            'button_icon'
        ]

class NoticePageSerializer(serializers.ModelSerializer):
    hero = NoticeHeroSerializer(read_only=True)
    cta = NoticeCTASerializer(read_only=True)
    notices = NoticeSerializer(many=True, read_only=True)
    
    class Meta:
        model = NoticePage
        fields = [
            'id', 'status', 'created_at', 'updated_at',
            'meta_title_ne', 'meta_title_en', 'meta_title_de',
            'meta_description_ne', 'meta_description_en', 'meta_description_de',
            'hero', 'cta', 'notices'
        ]
