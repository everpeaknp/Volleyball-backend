from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import NoticePage
from .serializers import NoticePageSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def notice_page_view(request):
    """
    API endpoint for Notice Page content
    """
    try:
        notice_page = NoticePage.objects.filter(status='published').first()
        
        if not notice_page:
            return Response({
                'error': 'Notice page not found or not published'
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Filter only published notices
        published_notices = notice_page.notices.filter(is_published=True).order_by('order')
        
        serializer = NoticePageSerializer(notice_page)
        data = serializer.data
        
        # Override notices with only published ones
        from .serializers import NoticeSerializer
        data['notices'] = NoticeSerializer(published_notices, many=True).data
        
        return Response([data])  # Return as array to match frontend expectation
        
    except Exception as e:
        return Response({
            'error': f'An error occurred: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
