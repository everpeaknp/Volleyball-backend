from rest_framework import serializers
from apps.gallery_options.models import (
    GalleryPage, GalleryHero, GalleryCategory, GalleryImage, GallerySettings
)
from apps.contact_options.models import (
    ContactPage, ContactHero, ContactInfo, ContactSocial, ContactSettings
)

# --- Gallery Serializers ---

class GalleryHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryHero
        fields = ['title_ne', 'title_en', 'title_de', 'text_ne', 'text_en', 'text_de']

class GalleryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryCategory
        fields = ['id', 'name_ne', 'name_en', 'name_de', 'order']

class GalleryImageSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(source='category', read_only=True)
    class Meta:
        model = GalleryImage
        fields = ['id', 'image', 'image_url', 'category_id', 'title_ne', 'title_en', 'title_de', 'order']

class GallerySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GallerySettings
        fields = ['no_images_text_ne', 'no_images_text_en', 'no_images_text_de']

class GalleryPageSerializer(serializers.ModelSerializer):
    hero = GalleryHeroSerializer(read_only=True)
    categories = GalleryCategorySerializer(many=True, read_only=True, source='page_categories') # need to check related name or just query
    images = GalleryImageSerializer(many=True, read_only=True)
    settings = GallerySettingsSerializer(read_only=True)

    class Meta:
        model = GalleryPage
        fields = ['status', 'meta_title_ne', 'meta_title_en', 'meta_title_de', 'hero', 'images', 'settings']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Categories aren't directly linked to GalleryPage in my model, so I'll fetch them all
        ret['categories'] = GalleryCategorySerializer(GalleryCategory.objects.all(), many=True).data
        return ret

# --- Contact Serializers ---

class ContactHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactHero
        fields = ['image', 'image_url', 'title_ne', 'title_en', 'title_de', 'subtitle_ne', 'subtitle_en', 'subtitle_de']

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['icon', 'label_ne', 'label_en', 'label_de', 'value', 'order']

class ContactSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSocial
        fields = ['platform', 'url', 'icon', 'order']

class ContactSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSettings
        fields = [
            'form_title_ne', 'form_title_en', 'form_title_de',
            'label_name_ne', 'label_name_en', 'label_name_de',
            'label_email_ne', 'label_email_en', 'label_email_de',
            'label_subject_ne', 'label_subject_en', 'label_subject_de',
            'label_message_ne', 'label_message_en', 'label_message_de',
            'label_submit_ne', 'label_submit_en', 'label_submit_de',
            'info_section_title_ne', 'info_section_title_en', 'info_section_title_de',
            'social_section_title_ne', 'social_section_title_en', 'social_section_title_de',
        ]

class ContactPageSerializer(serializers.ModelSerializer):
    hero = ContactHeroSerializer(read_only=True)
    contact_methods = ContactInfoSerializer(many=True, read_only=True)
    social_links = ContactSocialSerializer(many=True, read_only=True)
    settings = ContactSettingsSerializer(read_only=True)

    class Meta:
        model = ContactPage
        fields = ['status', 'meta_title_ne', 'meta_title_en', 'meta_title_de', 'hero', 'contact_methods', 'social_links', 'settings']
