import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volleyball_cms.settings.development')
django.setup()

from apps.homepage_options.models import HomePage
from apps.about_options.models import AboutPage
from apps.committee_options.models import CommitteePage
from apps.team_options.models import TeamPage
from apps.membership_options.models import MembershipPage
from apps.events_options.models import EventsPage
from apps.news_options.models import NewsPage
from apps.gallery_options.models import GalleryPage
from apps.contact_options.models import ContactPage
from apps.pages.models import NoticePage

def cleanup_duplicates():
    print("Starting cleanup of duplicate page objects...")
    
    models = [
        HomePage, AboutPage, CommitteePage, TeamPage, 
        MembershipPage, EventsPage, NewsPage, GalleryPage, ContactPage,
        NoticePage
    ]
    
    for model in models:
        # Keep only the object with ID 1, delete the rest
        duplicates = model.objects.exclude(id=1)
        count = duplicates.count()
        if count > 0:
            print(f"Deleting {count} duplicates from {model.__name__} (keeping ID 1)")
            duplicates.delete()
        else:
            print(f"No duplicates found for {model.__name__}")

if __name__ == "__main__":
    cleanup_duplicates()
