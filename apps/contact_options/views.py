from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactSubmission
from .serializers import ContactSubmissionSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def create_contact_submission(request):
    """
    Create a new contact form submission
    """
    print("=== DEBUG: Contact Form Submission ===")
    print(f"Request method: {request.method}")
    print(f"Request data: {request.data}")
    print(f"Request headers: {dict(request.headers)}")
    
    serializer = ContactSubmissionSerializer(data=request.data)
    
    if serializer.is_valid():
        submission = serializer.save()
        print(f"SUCCESS: Contact submission saved with ID {submission.id}")
        
        # Send confirmation email to sender
        try:
            send_mail(
                subject=f'Message Received - Nepal Volleyball Club Hamburg',
                message=f'Dear {submission.name},\n\nThank you for contacting Nepal Volleyball Club Hamburg e.V.!\n\nWe have received your message and will get back to you as soon as possible, usually within 24-48 hours.\n\nYour Message:\nSubject: {submission.subject}\nMessage: {submission.message}\n\nBest regards,\nNepal Volleyball Club Hamburg e.V. Team',
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@nepalvolleyballhh.de'),
                recipient_list=[submission.email],
                fail_silently=True,
            )
            
            # Send notification email to admin
            admin_emails = getattr(settings, 'ADMIN_EMAIL_LIST', ['admin@nepalvolleyballhh.de'])
            send_mail(
                subject=f'New Contact Message - {submission.subject}',
                message=f'A new contact message has been submitted:\n\nName: {submission.name}\nEmail: {submission.email}\nSubject: {submission.subject}\n\nMessage:\n{submission.message}\n\nPlease respond to this message promptly.',
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@nepalvolleyballhh.de'),
                recipient_list=admin_emails,
                fail_silently=True,
            )
        except Exception as e:
            # Log email error but don't fail the request
            print(f"Email sending failed: {str(e)}")
        
        return Response({
            'status': 'success',
            'message': 'Contact message sent successfully!',
            'submission_id': submission.id
        }, status=status.HTTP_201_CREATED)
    else:
        print(f"VALIDATION ERROR: {serializer.errors}")
        return Response({
            'status': 'error',
            'message': 'Please check your input and try again.',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)