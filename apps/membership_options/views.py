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
        
        # Determine category label for email
        category_label = "Player" if application.category == "player" else "Committee"
        
        # Send confirmation email to applicant
        try:
            position_info = f"- Preferred Position: {application.get_position_display()}\n- Experience Level: {application.get_experience_display()}" if application.category == 'player' else ""
            voucher_info = "\n- Bank Voucher: Submitted" if application.category == 'committee' and application.bank_voucher else ""
            
            send_mail(
                subject=f'Membership Application Received - Nepal Volleyball Club Hamburg',
                message=f'Dear {application.full_name},\n\nThank you for your interest in joining Nepal Volleyball Club Hamburg e.V. as a {category_label}!\n\nWe have received your membership application and will review it shortly. Our team will contact you within the next few days.\n\nApplication Details:\n- Name: {application.full_name}\n- Email: {application.email}\n- Category: {category_label}{position_info}{voucher_info}\n\nWe look forward to welcoming you to our volleyball community!\n\nBest regards,\nNepal Volleyball Club Hamburg e.V. Team',
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@nepalvolleyballhh.de'),
                recipient_list=[application.email],
                fail_silently=True,
            )
            
            # Send notification email to admin
            admin_emails = getattr(settings, 'ADMIN_EMAIL_LIST', ['admin@nepalvolleyballhh.de'])
            
            admin_message = f'A new membership application has been submitted:\n\n' \
                            f'Name: {application.full_name}\n' \
                            f'Email: {application.email}\n' \
                            f'Category: {category_label}\n'
            
            if application.category == 'player':
                admin_message += f'Experience: {application.get_experience_display()}\n' \
                                 f'Position: {application.get_position_display()}\n'
            elif application.category == 'committee' and application.bank_voucher:
                admin_message += f'Bank Voucher: {request.build_absolute_uri(application.bank_voucher.url)}\n'
            
            admin_message += f'\nPlease review the application in the admin panel.'
            
            send_mail(
                subject=f'New {category_label} Membership Application - {application.full_name}',
                message=admin_message,
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