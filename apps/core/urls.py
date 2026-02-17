from django.urls import path
from .views import GlobalStylesViewSet

urlpatterns = [
    path('global-styles/', GlobalStylesViewSet.as_view({'get': 'list'}), name='global-styles'),
]
