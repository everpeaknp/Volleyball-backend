from rest_framework.routers import DefaultRouter
from .views import (
    MemberViewSet, ArticleViewSet, NoticeViewSet,
    EventViewSet, GalleryImageViewSet
)

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'notices', NoticeViewSet)
router.register(r'events', EventViewSet)
router.register(r'gallery', GalleryImageViewSet)

urlpatterns = router.urls
