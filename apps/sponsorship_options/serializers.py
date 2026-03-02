from rest_framework import serializers
from .models import (
    SponsorshipPage, SponsorshipHero, Sponsor, 
    SponsorshipFormSettings, SponsorshipApplication
)

class SponsorshipHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorshipHero
        fields = [
            'image', 'image_url', 
            'title_ne', 'title_en', 'title_de',
            'text_ne', 'text_en', 'text_de'
        ]

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = [
            'name_ne', 'name_en', 'name_de', 
            'logo', 'link', 'order'
        ]

class SponsorshipFormSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorshipFormSettings
        fields = '__all__'

class SponsorshipPageSerializer(serializers.ModelSerializer):
    hero = SponsorshipHeroSerializer(read_only=True)
    sponsors = SponsorSerializer(many=True, read_only=True)
    form_settings = SponsorshipFormSettingsSerializer(read_only=True)

    class Meta:
        model = SponsorshipPage
        fields = [
            'status', 'updated_at', 
            'hero', 'sponsors', 'form_settings',
            'meta_title_ne', 'meta_title_en', 'meta_title_de',
            'meta_description_ne', 'meta_description_en', 'meta_description_de',
            'meta_keywords', 'og_title_ne', 'og_title_en', 'og_title_de',
            'og_description_ne', 'og_description_en', 'og_description_de',
            'og_image', 'canonical_url'
        ]

class SponsorshipApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorshipApplication
        fields = '__all__'
        read_only_fields = ['is_approved', 'created_at', 'updated_at']
