from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.membership_options.models import MembershipApplication
from django.core.mail import send_mail
from django.conf import settings
import datetime

class Command(BaseCommand):
    help = 'Check for expiring memberships and send emails'

    def handle(self, *args, **options):
        now = timezone.now()
        thirty_days_from_now = now + datetime.timedelta(days=30)
        
        # 1. Expire past memberships
        expired_apps = MembershipApplication.objects.filter(
            status='active',
            expires_at__lt=now
        )
        
        count_expired = 0
        for app in expired_apps:
            app.status = 'expired'
            app.save(update_fields=['status'])
            self._send_expired_email(app)
            count_expired += 1
            
        self.stdout.write(self.style.SUCCESS(f'Expired {count_expired} memberships.'))
        
        # 2. Warn ending soon memberships (under 30 days)
        warning_apps = MembershipApplication.objects.filter(
            status='active',
            expires_at__lte=thirty_days_from_now,
            expires_at__gt=now
        )
        
        count_warnings = 0
        for app in warning_apps:
            # Check the 3-day rule
            if not app.last_warning_sent_at or app.last_warning_sent_at < (now - datetime.timedelta(days=3)):
                self._send_warning_email(app)
                app.last_warning_sent_at = now
                app.save(update_fields=['last_warning_sent_at'])
                count_warnings += 1
                
        self.stdout.write(self.style.SUCCESS(f'Sent {count_warnings} warning emails.'))

    def _send_expired_email(self, app):
        admin_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@nepalvolleyballhh.de')
        subject = 'Your Membership has Expired'
        message = (
            f"Dear {app.full_name},\n\n"
            f"Your membership with Nepal Volleyball Club Hamburg e.V. has officially expired.\n"
            f"If you'd like to continue being a part of our club, please visit our website to renew your membership.\n\n"
            f"Best regards,\nNepal Volleyball Club Hamburg e.V."
        )
        send_mail(subject, message, admin_email, [app.email], fail_silently=True)

    def _send_warning_email(self, app):
        admin_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@nepalvolleyballhh.de')
        days_left = (app.expires_at - timezone.now()).days
        subject = f'Action Required: Your Membership Expires in {days_left} Days'
        message = (
            f"Dear {app.full_name},\n\n"
            f"This is an automated reminder that your membership with Nepal Volleyball Club Hamburg e.V. "
            f"will expire in exactly {days_left} days on {app.expires_at.strftime('%Y-%m-%d')}.\n\n"
            f"Please visit our localized membership page to renew your membership before it expires.\n\n"
            f"Best regards,\nNepal Volleyball Club Hamburg e.V."
        )
        send_mail(subject, message, admin_email, [app.email], fail_silently=True)
