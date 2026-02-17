from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .models import GlobalStyles
from .serializers import GlobalStylesSerializer

class GlobalStylesViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    Singleton view for global styles.
    """
    queryset = GlobalStyles.objects.all()
    serializer_class = GlobalStylesSerializer

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset().last()
        if not instance:
            return Response({})
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
