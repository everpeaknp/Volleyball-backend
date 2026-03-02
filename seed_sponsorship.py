import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volleyball_cms.settings.development')
django.setup()

from apps.sponsorship_options.models import SponsorshipPage, SponsorshipHero, SponsorshipFormSettings

def seed():
    page, created = SponsorshipPage.objects.get_or_create(status='published')
    if created:
        print("Created SponsorshipPage")
    
    settings, created = SponsorshipFormSettings.objects.get_or_create(
        page=page,
        defaults={
            'title_en': 'Become a Sponsor',
            'title_ne': 'एक प्रायोजक बन्नुहोस्',
            'title_de': 'Werden Sie Sponsor',
            'text_en': 'Support our club and gain visibility. Fill out the application form below.',
            'text_ne': 'हाम्रो क्लबलाई समर्थन गर्नुहोस् र दृश्यात्मकता प्राप्त गर्नुहोस्। तलको आवेदन फारम भर्नुहोस्।',
            'text_de': 'Unterstützen Sie unseren Club und gewinnen Sie Sichtbarkeit. Füllen Sie das folgende Antragsformular aus.',
            'success_title_en': 'Application Received',
            'success_text_en': 'Thank you! We will review your sponsorship application soon.',
            'success_title_ne': 'आवेदन प्राप्त भयो',
            'success_text_ne': 'धन्यवाद! हामी तपाईंको आवेदन चाँडै समीक्षा गर्नेछौं।',
            'success_title_de': 'Antrag erhalten',
            'success_text_de': 'Vielen Dank! Wir werden Ihren Sponsoring-Antrag in Kürze prüfen.',
        }
    )
    if created:
        print("Created SponsorshipFormSettings")
    else:
        print("SponsorshipFormSettings already exists")

    hero, created = SponsorshipHero.objects.get_or_create(
        page=page,
        defaults={
            'title_en': 'Sponsorship',
            'text_en': 'Partner with Nepal Volleyball Club Hamburg e.V.',
            'title_ne': 'प्रायोजन',
            'text_ne': 'नेपाल भलिबल क्लब ह्याम्बर्ग e.V. सँग साझेदारी गर्नुहोस्',
            'title_de': 'Sponsoring',
            'text_de': 'Werden Sie Partner des Nepal Volleyball Club Hamburg e.V.',
        }
    )
    if created:
        print("Created SponsorshipHero")

if __name__ == '__main__':
    seed()
