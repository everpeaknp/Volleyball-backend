from rest_framework import viewsets
from apps.homepage_options.models import HomePage
from apps.about_options.models import AboutPage
from .models import (
    NoticePage
)
from apps.events_options.models import EventsPage
from apps.news_options.models import NewsPage
from apps.committee_options.models import CommitteePage
from apps.team_options.models import TeamPage
from apps.membership_options.models import MembershipPage
from apps.gallery_options.models import GalleryPage
from apps.contact_options.models import ContactPage
from .serializers import (
    HomePageSerializer, AboutPageSerializer, CommitteePageSerializer,
    TeamPageSerializer, MembershipPageSerializer,
    GalleryPageSerializer, ContactPageSerializer,
    NoticePageSerializer
)
from apps.api.news_events_serializers import EventsPageSerializer, NewsPageSerializer

class HomePageViewSet(viewsets.ModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer

class AboutPageViewSet(viewsets.ModelViewSet):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer

class CommitteePageViewSet(viewsets.ModelViewSet):
    queryset = CommitteePage.objects.all()
    serializer_class = CommitteePageSerializer

class TeamPageViewSet(viewsets.ModelViewSet):
    queryset = TeamPage.objects.all()
    serializer_class = TeamPageSerializer

class MembershipPageViewSet(viewsets.ModelViewSet):
    queryset = MembershipPage.objects.all()
    serializer_class = MembershipPageSerializer

class EventsPageViewSet(viewsets.ModelViewSet):
    queryset = EventsPage.objects.all()
    serializer_class = EventsPageSerializer

class NewsPageViewSet(viewsets.ModelViewSet):
    queryset = NewsPage.objects.all()
    serializer_class = NewsPageSerializer

class GalleryPageViewSet(viewsets.ModelViewSet):
    queryset = GalleryPage.objects.all()
    serializer_class = GalleryPageSerializer

class ContactPageViewSet(viewsets.ModelViewSet):
    queryset = ContactPage.objects.all()
    serializer_class = ContactPageSerializer

class NoticePageViewSet(viewsets.ModelViewSet):
    queryset = NoticePage.objects.all()
    serializer_class = NoticePageSerializer
