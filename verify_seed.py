import sys
import os
import django

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volleyball_cms.settings.base')
django.setup()

from apps.pages.models import HomePage

try:
    count = HomePage.objects.count()
    if count > 0:
        page = HomePage.objects.first()
        with open('seed_status.txt', 'w') as f:
            f.write(f"SUCCESS: Found {count} HomePage. Title: {page.hero_title_en}")
    else:
        with open('seed_status.txt', 'w') as f:
            f.write("FAILURE: No HomePage found")
except Exception as e:
    with open('seed_status.txt', 'w') as f:
        f.write(f"ERROR: {str(e)}")
