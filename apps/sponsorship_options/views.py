from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.mail import send_mail
from django.conf import settings
from .models import SponsorshipPage, SponsorshipApplication
from .serializers import SponsorshipPageSerializer, SponsorshipApplicationSerializer

class SponsorshipPageView(APIView):
    def get(self, request):
        page = SponsorshipPage.objects.filter(status='published').first()
        if not page:
            return Response({"error": "Sponsorship page not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SponsorshipPageSerializer(page)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def submit_sponsorship_application(request):
    """
    Create a new sponsorship application
    """
    serializer = SponsorshipApplicationSerializer(data=request.data)
    if serializer.is_valid():
        application = serializer.save()
        
        # Determine notification settings
        admin_email = getattr(settings, 'ADMIN_EMAIL', 'yummyever.np@gmail.com')
        admin_email_list = getattr(settings, 'ADMIN_EMAIL_LIST', [admin_email])
        
        # Build absolute URL for bank voucher
        voucher_url = ""
        if application.bank_voucher:
            voucher_url = request.build_absolute_uri(application.bank_voucher.url)

        # 1. Send confirmation email to applicant
        applicant_subject = "Sponsorship Application Received - Nepal Volleyball Club Hamburg"
        applicant_message = (
            f"Dear {application.name},\n\n"
            f"Thank you for your interest in sponsoring Nepal Volleyball Club Hamburg e.V.!\n\n"
            f"We have received your sponsorship application and our team will review it shortly. "
            f"We appreciate your support and interest in partnering with us.\n\n"
            f"Application Details:\n"
            f"- Name/Company: {application.name}\n"
            f"- Sponsorship Type: {application.get_sponsorship_type_display()}\n"
            f"- Amount: €{application.amount}\n\n"
            f"Our team will contact you within the next few days with further information.\n\n"
            f"Best regards,\n"
            f"Nepal Volleyball Club Hamburg e.V. Team"
        )
        
        try:
            send_mail(
                subject=applicant_subject,
                message=applicant_message,
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@nepalvolleyballhh.de'),
                recipient_list=[application.email],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Failed to send sponsorship applicant confirmation: {e}")

        # 2. Send notification email to admin
        admin_subject = f"NEW Sponsorship Application: {application.name}"
        admin_message = (
            f"A new sponsorship application has been submitted from the website.\n\n"
            f"Name/Company: {application.name}\n"
            f"Email: {application.email}\n"
            f"Phone: {application.phone}\n"
            f"Sponsorship Type: {application.get_sponsorship_type_display()}\n"
            f"Amount: €{application.amount}\n"
            f"Voucher: {voucher_url}\n\n"
            f"Message: {application.message}\n\n"
            f"Please log in to the admin panel to review and approve this application."
        )
        
        try:
            send_mail(
                subject=admin_subject,
                message=admin_message,
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@nepalvolleyballhh.de'),
                recipient_list=admin_email_list,
                fail_silently=True,
            )
        except Exception as e:
            print(f"Failed to send sponsorship admin notification: {e}")
            
        return Response({
            "success": True, 
            "message": "Sponsorship application submitted successfully! Our team will contact you shortly.",
            "application_id": application.id
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
