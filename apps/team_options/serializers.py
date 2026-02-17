from rest_framework import serializers
from .models import (
    TeamPage, TeamHero, TeamCoachesSettings, TeamPlayersSettings,
    Coach, Player, TeamPhotoSection, TeamCTA
)
from apps.media.serializers import MediaSerializer

class TeamHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamHero
        exclude = ('id', 'page')

class TeamCoachesSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamCoachesSettings
        exclude = ('id', 'page')

class TeamPlayersSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPlayersSettings
        exclude = ('id', 'page')

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        exclude = ('id', 'page')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ('id', 'page')

class TeamPhotoSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPhotoSection
        exclude = ('id', 'page')

class TeamCTASerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamCTA
        exclude = ('id', 'page')

class TeamPageFullSerializer(serializers.ModelSerializer):
    hero = TeamHeroSerializer(read_only=True)
    coaches_settings = TeamCoachesSettingsSerializer(read_only=True)
    players_settings = TeamPlayersSettingsSerializer(read_only=True)
    coaches = CoachSerializer(many=True, read_only=True)
    players = PlayerSerializer(many=True, read_only=True)
    photo_section = TeamPhotoSectionSerializer(read_only=True)
    cta = TeamCTASerializer(read_only=True)
    og_image = MediaSerializer(read_only=True)

    class Meta:
        model = TeamPage
        fields = [
            'id', 'status', 'published_at', 'updated_at',
            'meta_title_ne', 'meta_title_en', 'meta_title_de',
            'meta_description_ne', 'meta_description_en', 'meta_description_de',
            'meta_keywords',
            'og_title_ne', 'og_title_en', 'og_title_de',
            'og_description_ne', 'og_description_en', 'og_description_de',
            'og_image', 'canonical_url',
            'hero', 'coaches_settings', 'players_settings', 'coaches', 'players', 'photo_section', 'cta'
        ]
