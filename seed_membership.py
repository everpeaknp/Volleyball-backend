import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volleyball_cms.settings.development')
django.setup()

from apps.membership_options.models import MembershipPage, MembershipFormSettings, MembershipHero

def seed():
    page, created = MembershipPage.objects.get_or_create(status='published')
    if created:
        print("Created MembershipPage")
    
    settings, created = MembershipFormSettings.objects.get_or_create(
        page=page,
        defaults={
            'title_en': 'Join Our Club',
            'title_ne': 'हाम्रो क्लबमा सामेल हुनुहोस्',
            'title_de': 'Treten Sie unserem Club bei',
            'text_en': 'Please fill out the form below.',
            'text_ne': 'तलको फारम भर्नुहोस्।',
            'text_de': 'Bitte füllen Sie das folgende Formular aus.',
            'success_title_en': 'Application Received',
            'success_text_en': 'Thank you! We will review your application soon.',
            'link_category_en': 'Membership Category', # Fallback labels will be used if not set
        }
    )
    if created:
        print("Created MembershipFormSettings")
    else:
        print("MembershipFormSettings already exists")

    hero, created = MembershipHero.objects.get_or_create(
        page=page,
        defaults={
            'title_en': 'Membership',
            'text_en': 'Become a part of Nepal Volleyball Club Hamburg',
        }
    )
    if created:
        print("Created MembershipHero")

if __name__ == '__main__':
    seed()
