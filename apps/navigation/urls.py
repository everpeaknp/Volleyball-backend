from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NavigationSettingsViewSet, NavigationItemViewSet, FooterSettingsViewSet

router = DefaultRouter()
router.register(r'items', NavigationItemViewSet)

urlpatterns = [
    path('settings/', NavigationSettingsViewSet.as_view({'get': 'list'}), name='nav-settings'),
    path('footer/', FooterSettingsViewSet.as_view({'get': 'list'}), name='footer-settings'),
    path('', include(router.urls)),
]
