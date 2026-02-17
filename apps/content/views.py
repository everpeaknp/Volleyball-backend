from rest_framework import viewsets
from .models import Member, Article, Notice, Event, GalleryImage
from .serializers import (
    MemberSerializer, ArticleSerializer, NoticeSerializer,
    EventSerializer, GalleryImageSerializer
)

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filterset_fields = ['member_type', 'language']

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
    filterset_fields = ['category', 'is_featured', 'language']

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    filterset_fields = ['category', 'language']

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_fields = ['event_status', 'language']

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    filterset_fields = ['category', 'language']
