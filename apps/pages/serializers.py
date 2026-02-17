from rest_framework import serializers
from .models import (
    NoticePage
)
from apps.committee_options.serializers import CommitteePageFullSerializer
from apps.team_options.serializers import TeamPageFullSerializer
from apps.membership_options.serializers import MembershipPageFullSerializer
from apps.api.news_events_serializers import EventsPageSerializer as NewEventsPageSerializer, NewsPageSerializer as NewNewsPageSerializer
from apps.api.gallery_contact_serializers import GalleryPageSerializer as NewGalleryPageSerializer, ContactPageSerializer as NewContactPageSerializer
from apps.homepage_options.models import (
    HomePage, HomeHero, HomeIntro, HomeMission, HomeObjective, HomeMotto, HomeStat
)
from apps.about_options.models import (
    AboutPage, AboutHero, AboutIntro, AboutStat, AboutCore, AboutStrategic, AboutObjective
)
from apps.media.serializers import MediaSerializer

# --- Home Page Serializers ---

class HomeHeroSerializer(serializers.ModelSerializer):
    hero_video = MediaSerializer(source='video_file', read_only=True)
    class Meta:
        model = HomeHero
        exclude = ('id', 'page')

class HomeIntroSerializer(serializers.ModelSerializer):
    intro_image = MediaSerializer(source='image', read_only=True)
    class Meta:
        model = HomeIntro
        exclude = ('id', 'page')

class HomeObjectiveSerializer(serializers.ModelSerializer):
    image = MediaSerializer(read_only=True)
    class Meta:
        model = HomeObjective
        exclude = ('id', 'mission')

class HomeMissionSerializer(serializers.ModelSerializer):
    objectives = HomeObjectiveSerializer(many=True, read_only=True)
    class Meta:
        model = HomeMission
        exclude = ('id', 'page')

class HomeMottoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeMotto
        exclude = ('id', 'page')

class HomeStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeStat
        exclude = ('id', 'page')

class HomePageSerializer(serializers.ModelSerializer):
    hero = HomeHeroSerializer(read_only=True)
    intro = HomeIntroSerializer(read_only=True)
    mission = HomeMissionSerializer(read_only=True)
    motto = HomeMottoSerializer(read_only=True)
    stats = HomeStatSerializer(many=True, read_only=True)
    og_image = MediaSerializer(read_only=True)

    class Meta:
        model = HomePage
        fields = [
            'id', 'status', 'published_at', 'updated_at',
            'meta_title_ne', 'meta_title_en', 'meta_title_de',
            'meta_description_ne', 'meta_description_en', 'meta_description_de',
            'meta_keywords',
            'og_title_ne', 'og_title_en', 'og_title_de',
            'og_description_ne', 'og_description_en', 'og_description_de',
            'og_image', 'canonical_url',
            'hero', 'intro', 'mission', 'motto', 'stats'
        ]

# --- About Page Serializers ---

class AboutHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHero
        exclude = ('id', 'page')

class AboutStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutStat
        exclude = ('id', 'intro')

class AboutIntroSerializer(serializers.ModelSerializer):
    stats = AboutStatSerializer(many=True, read_only=True)
    main_image = MediaSerializer(read_only=True)
    secondary_image = MediaSerializer(read_only=True)
    class Meta:
        model = AboutIntro
        exclude = ('id', 'page')

class AboutCoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCore
        exclude = ('id', 'page')

class AboutObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutObjective
        exclude = ('id', 'strategic')

class AboutStrategicSerializer(serializers.ModelSerializer):
    objectives = AboutObjectiveSerializer(many=True, read_only=True)
    side_image = MediaSerializer(read_only=True)
    class Meta:
        model = AboutStrategic
        exclude = ('id', 'page')

class AboutPageSerializer(serializers.ModelSerializer):
    hero = AboutHeroSerializer(read_only=True)
    intro = AboutIntroSerializer(read_only=True)
    core = AboutCoreSerializer(read_only=True)
    strategic = AboutStrategicSerializer(read_only=True)
    og_image = MediaSerializer(read_only=True)

    class Meta:
        model = AboutPage
        fields = [
            'id', 'status', 'published_at', 'updated_at',
            'meta_title_ne', 'meta_title_en', 'meta_title_de',
            'meta_description_ne', 'meta_description_en', 'meta_description_de',
            'meta_keywords',
            'og_title_ne', 'og_title_en', 'og_title_de',
            'og_description_ne', 'og_description_en', 'og_description_de',
            'og_image', 'canonical_url',
            'hero', 'intro', 'core', 'strategic'
        ]

# --- Generic Page Serializers ---

# CommitteePage is now handled by apps.committee_options
CommitteePageSerializer = CommitteePageFullSerializer

# TeamPage is now handled by apps.team_options
TeamPageSerializer = TeamPageFullSerializer

# MembershipPage is now handled by apps.membership_options
MembershipPageSerializer = MembershipPageFullSerializer

# EventsPage and NewsPage are now handled by apps.api.news_events_serializers
EventsPageSerializer = NewEventsPageSerializer
NewsPageSerializer = NewNewsPageSerializer

# GalleryPage and ContactPage are now handled by apps.api.gallery_contact_serializers
GalleryPageSerializer = NewGalleryPageSerializer
ContactPageSerializer = NewContactPageSerializer

class NoticePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticePage
        fields = '__all__'
