from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import MembershipApplication
from .serializers import MembershipApplicationSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def create_membership_application(request):
    """
    Create a new membership application
    """
    print("=== DEBUG: Membership Application Submission ===")
    print(f"Request method: {request.method}")
    print(f"Request data: {request.data}")
    print(f"Request headers: {dict(request.headers)}")
    
    serializer = MembershipApplicationSerializer(data=request.data)
    
    if serializer.is_valid():
        application = serializer.save()
        print(f"SUCCESS: Application saved with ID {application.id}")
        
        # Send confirmation email to applicant
        try:
            send_mail(
                subject=f'Membership Application Received - Nepal Volleyball Club Hamburg',
                message=f'Dear {application.full_name},\n\nThank you for your interest in joining Nepal Volleyball Club Hamburg e.V.!\n\nWe have received your membership application and will review it shortly. Our team will contact you within the next few days.\n\nApplication Details:\n- Name: {application.full_name}\n- Email: {application.email}\n- Experience Level: {application.get_experience_display()}\n- Preferred Position: {application.get_position_display()}\n\nWe look forward to welcoming you to our volleyball community!\n\nBest regards,\nNepal Volleyball Club Hamburg e.V. Team',
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@nepalvolleyballhh.de'),
                recipient_list=[application.email],
                fail_silently=True,
            )
            
            # Send notification email to admin
            admin_emails = getattr(settings, 'ADMIN_EMAIL_LIST', ['admin@nepalvolleyballhh.de'])
            send_mail(
                subject=f'New Membership Application - {application.full_name}',
                message=f'A new membership application has been submitted:\n\nName: {application.full_name}\nEmail: {application.email}\nPhone: {application.phone}\nAddress: {application.address}\nDate of Birth: {application.date_of_birth}\nGender: {application.get_gender_display()}\nExperience: {application.get_experience_display()}\nPosition: {application.get_position_display()}\nReason: {application.reason}\n\nPlease review the application in the admin panel.',
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@nepalvolleyballhh.de'),
                recipient_list=admin_emails,
                fail_silently=True,
            )
        except Exception as e:
            # Log email error but don't fail the request
            print(f"Email sending failed: {str(e)}")
        
        return Response({
            'success': True,
            'message': 'Application submitted successfully! We will contact you shortly.',
            'application_id': application.id
        }, status=status.HTTP_201_CREATED)
    
    print(f"ERROR: Serializer validation failed")
    print(f"Errors: {serializer.errors}")
    return Response({
        'success': False,
        'errors': serializer.errors,
        'message': 'Please check your form data and try again.'
    }, status=status.HTTP_400_BAD_REQUEST)