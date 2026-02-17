from rest_framework.routers import DefaultRouter
from .views import (
    HomePageViewSet, AboutPageViewSet, CommitteePageViewSet,
    TeamPageViewSet, MembershipPageViewSet, EventsPageViewSet,
    NewsPageViewSet, GalleryPageViewSet, ContactPageViewSet,
    NoticePageViewSet
)

router = DefaultRouter()
router.register(r'home', HomePageViewSet)
router.register(r'about', AboutPageViewSet)
router.register(r'committee', CommitteePageViewSet)
router.register(r'team', TeamPageViewSet)
router.register(r'membership', MembershipPageViewSet)
router.register(r'events', EventsPageViewSet)
router.register(r'news', NewsPageViewSet)
router.register(r'gallery', GalleryPageViewSet)
router.register(r'contact', ContactPageViewSet)
router.register(r'notice', NoticePageViewSet)

urlpatterns = router.urls
