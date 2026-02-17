from rest_framework import serializers
from apps.events_options.models import EventsPage, EventsHero, EventsSettings, Event
from apps.news_options.models import NewsPage, NewsHero, NewsSettings, NewsCategory, NewsArticle

# --- Events Serializers ---

class EventsHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsHero
        fields = ['title_ne', 'title_en', 'title_de', 'text_ne', 'text_en', 'text_de', 'image', 'image_url']

class EventsSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsSettings
        fields = [
            'upcoming_title_ne', 'upcoming_title_en', 'upcoming_title_de',
            'past_title_ne', 'past_title_en', 'past_title_de',
            'register_btn_ne', 'register_btn_en', 'register_btn_de',
            'label_upcoming_ne', 'label_upcoming_en', 'label_upcoming_de',
            'label_past_ne', 'label_past_en', 'label_past_de',
        ]

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'title_ne', 'title_en', 'title_de',
            'description_ne', 'description_en', 'description_de',
            'date_text_ne', 'date_text_en', 'date_text_de',
            'time', 'location_ne', 'location_en', 'location_de',
            'image', 'image_url', 'is_past', 'order'
        ]

class EventsPageSerializer(serializers.ModelSerializer):
    hero = EventsHeroSerializer(read_only=True)
    settings = EventsSettingsSerializer(read_only=True)
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = EventsPage
        fields = ['status', 'meta_title_ne', 'meta_title_en', 'meta_title_de', 'hero', 'settings', 'events']

# --- News Serializers ---

class NewsHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsHero
        fields = ['title_ne', 'title_en', 'title_de', 'text_ne', 'text_en', 'text_de', 'image', 'image_url']

class NewsSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsSettings
        fields = [
            'featured_label_ne', 'featured_label_en', 'featured_label_de',
            'read_more_label_ne', 'read_more_label_en', 'read_more_label_de',
            'other_news_title_ne', 'other_news_title_en', 'other_news_title_de',
        ]

class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ['name_ne', 'name_en', 'name_de', 'order']

class NewsArticleSerializer(serializers.ModelSerializer):
    category = NewsCategorySerializer(read_only=True)
    class Meta:
        model = NewsArticle
        fields = [
            'title_ne', 'title_en', 'title_de',
            'excerpt_ne', 'excerpt_en', 'excerpt_de',
            'content_ne', 'content_en', 'content_de',
            'category', 'image', 'image_url', 'date_text_ne', 'date_text_en', 'date_text_de',
            'featured', 'order'
        ]

class NewsPageSerializer(serializers.ModelSerializer):
    hero = NewsHeroSerializer(read_only=True)
    settings = NewsSettingsSerializer(read_only=True)
    articles = NewsArticleSerializer(many=True, read_only=True)

    class Meta:
        model = NewsPage
        fields = ['status', 'meta_title_ne', 'meta_title_en', 'meta_title_de', 'hero', 'settings', 'articles']
