from rest_framework import serializers
from .models import Member, Article, Notice, Event, GalleryImage
from apps.media.serializers import MediaSerializer

class MemberSerializer(serializers.ModelSerializer):
    image = MediaSerializer()
    class Meta:
        model = Member
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    featured_image = MediaSerializer()
    class Meta:
        model = Article
        fields = '__all__'

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    image = MediaSerializer()
    class Meta:
        model = Event
        fields = '__all__'

class GalleryImageSerializer(serializers.ModelSerializer):
    image = MediaSerializer()
    class Meta:
        model = GalleryImage
        fields = '__all__'
