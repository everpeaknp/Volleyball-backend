from rest_framework import serializers
from .models import CommitteePage, CommitteeHero, ExecutiveMember, CommitteeMember, CommitteeGroup, CommitteeSectionSettings

class CommitteeHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeHero
        fields = [
            'title_ne', 'title_en', 'title_de',
            'subtitle_ne', 'subtitle_en', 'subtitle_de',
            'background_image', 'background_color'
        ]

class ExecutiveMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutiveMember
        fields = [
            'name', 'role_ne', 'role_en', 'role_de',
            'desc_ne', 'desc_en', 'desc_de', 'image', 'email', 'order'
        ]

class CommitteeMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeMember
        fields = ['name_ne', 'name_en', 'name_de', 'name', 'image', 'order']

class CommitteeGroupSerializer(serializers.ModelSerializer):
    members = CommitteeMemberSerializer(many=True, read_only=True)
    
    class Meta:
        model = CommitteeGroup
        fields = ['title_ne', 'title_en', 'title_de', 'order', 'members']

class CommitteeSectionSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeSectionSettings
        fields = [
            'member_section_title_ne', 'member_section_title_en', 'member_section_title_de'
        ]

class CommitteePageFullSerializer(serializers.ModelSerializer):
    hero = CommitteeHeroSerializer(read_only=True)
    executives = ExecutiveMemberSerializer(many=True, read_only=True)
    groups = CommitteeGroupSerializer(many=True, read_only=True)
    section_settings = CommitteeSectionSettingsSerializer(read_only=True)
    og_image_url = serializers.SerializerMethodField()

    class Meta:
        model = CommitteePage
        fields = [
            'id', 'status', 'published_at',
            'meta_title_ne', 'meta_title_en', 'meta_title_de',
            'meta_description_ne', 'meta_description_en', 'meta_description_de',
            'meta_keywords',
            'og_title_ne', 'og_title_en', 'og_title_de',
            'og_description_ne', 'og_description_en', 'og_description_de',
            'og_image_url', 'canonical_url',
            'hero', 'executives', 'groups', 'section_settings'
        ]

    def get_og_image_url(self, obj):
        if obj.og_image and obj.og_image.file:
            try:
                return obj.og_image.file.url
            except ValueError:
                return None
        return None
