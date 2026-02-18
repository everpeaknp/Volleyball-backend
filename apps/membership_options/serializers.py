from rest_framework import serializers
from .models import MembershipPage, MembershipHero, MembershipBenefit, MembershipFormSettings, MembershipApplication
from apps.media.serializers import MediaSerializer

class MembershipHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipHero
        exclude = ('id', 'page')

class MembershipBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipBenefit
        exclude = ('id', 'page')

class MembershipFormSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipFormSettings
        exclude = ('id', 'page')

class MembershipPageFullSerializer(serializers.ModelSerializer):
    hero = MembershipHeroSerializer(read_only=True)
    benefits = MembershipBenefitSerializer(many=True, read_only=True)
    form_settings = MembershipFormSettingsSerializer(read_only=True)
    og_image_url = serializers.SerializerMethodField()

    class Meta:
        model = MembershipPage
        fields = [
            'id', 'status', 'published_at', 'updated_at',
            'meta_title_ne', 'meta_title_en', 'meta_title_de',
            'meta_description_ne', 'meta_description_en', 'meta_description_de',
            'meta_keywords',
            'og_title_ne', 'og_title_en', 'og_title_de',
            'og_description_ne', 'og_description_en', 'og_description_de',
            'og_image_url', 'canonical_url',
            'hero', 'benefits', 'form_settings'
        ]

    def get_og_image_url(self, obj):
        if obj.og_image and obj.og_image.file:
            try:
                return obj.og_image.file.url
            except ValueError:
                return None
        return None

class MembershipApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipApplication
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
