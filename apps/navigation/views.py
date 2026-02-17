from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .models import NavigationSettings, NavigationItem, FooterSettings
from .serializers import NavigationSettingsSerializer, NavigationItemSerializer, FooterSettingsSerializer

class NavigationSettingsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    Singleton view for navigation settings.
    Always returns the first active instance or empty.
    """
    queryset = NavigationSettings.objects.all()
    serializer_class = NavigationSettingsSerializer

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset().last()
        if not instance:
            return Response({})
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class NavigationItemViewSet(viewsets.ModelViewSet):
    queryset = NavigationItem.objects.filter(is_active=True)
    serializer_class = NavigationItemSerializer

class FooterSettingsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    Singleton view for footer settings.
    """
    queryset = FooterSettings.objects.all()
    serializer_class = FooterSettingsSerializer

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset().last()
        if not instance:
            return Response({})
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
