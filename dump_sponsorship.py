import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volleyball_cms.settings.development')
django.setup()

from apps.sponsorship_options.models import Sponsor, SponsorshipPage
from apps.sponsorship_options.serializers import SponsorshipPageSerializer

def dump_data():
    page = SponsorshipPage.objects.filter(status='published').first()
    if not page:
        print("No published sponsorship page found.")
        return
    
    serializer = SponsorshipPageSerializer(page)
    with open('sponsorship_data_dump.json', 'w') as f:
        json.dump(serializer.data, f, indent=4)
    print("Sponsorship data dumped to sponsorship_data_dump.json")

if __name__ == '__main__':
    dump_data()
