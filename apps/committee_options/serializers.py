from rest_framework import serializers
from .models import CommitteePage, CommitteeHero, CommitteeBoard, CommitteeMember, CommitteeSectionSettings

class CommitteeHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeHero
        fields = [
            'title_ne', 'title_en', 'title_de',
            'subtitle_ne', 'subtitle_en', 'subtitle_de',
            'background_image', 'background_color'
        ]

class CommitteeBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeBoard
        fields = [
            'pres_name', 'pres_role_ne', 'pres_role_en', 'pres_role_de',
            'pres_desc_ne', 'pres_desc_en', 'pres_desc_de', 'pres_image', 'pres_email',
            'sec_name', 'sec_role_ne', 'sec_role_en', 'sec_role_de',
            'sec_desc_ne', 'sec_desc_en', 'sec_desc_de', 'sec_image', 'sec_email',
            'tres_name', 'tres_role_ne', 'tres_role_en', 'tres_role_de',
            'tres_desc_ne', 'tres_desc_en', 'tres_desc_de', 'tres_image', 'tres_email'
        ]

class CommitteeMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeMember
        fields = ['name', 'image', 'order']

class CommitteeSectionSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeSectionSettings
        fields = [
            'member_section_title_ne', 'member_section_title_en', 'member_section_title_de'
        ]

class CommitteePageFullSerializer(serializers.ModelSerializer):
    hero = CommitteeHeroSerializer(read_only=True)
    board = CommitteeBoardSerializer(read_only=True)
    members = CommitteeMemberSerializer(many=True, read_only=True)
    section_settings = CommitteeSectionSettingsSerializer(read_only=True)

    class Meta:
        model = CommitteePage
        fields = [
            'id', 'status', 'published_at',
            'meta_title_ne', 'meta_title_en', 'meta_title_de',
            'meta_description_ne', 'meta_description_en', 'meta_description_de',
            'meta_keywords',
            'og_title_ne', 'og_title_en', 'og_title_de',
            'og_description_ne', 'og_description_en', 'og_description_de',
            'og_image', 'canonical_url',
            'hero', 'board', 'members', 'section_settings'
        ]
