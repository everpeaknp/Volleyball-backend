import os
import django
import sys

# Setup Django
sys.path.append('/home/ram0niswack/RootProjects/volleyball-backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volleyball_cms.settings.base')
django.setup()

from apps.committee_options.models import CommitteePage, CommitteeBoard, CommitteeMember

def verify():
    print("Checking Committee Data...")
    
    page = CommitteePage.objects.filter(id=1).first()
    if not page:
        print("FAIL: CommitteePage not found")
        return

    print(f"Page Status: {page.status}")
    print(f"Meta Title (EN): {page.meta_title_en}")

    board = getattr(page, 'board', None)
    if not board:
        print("FAIL: CommitteeBoard not found for page")
    else:
        print(f"SUCCESS: Board Found. President: {board.pres_name}")
        print(f"President Role (DE): {board.pres_role_de}")
        print(f"President Description (NE): {board.pres_desc_ne}")

    members_count = page.members.count()
    print(f"Members Count: {members_count}")
    if members_count == 9:
        print("SUCCESS: 9 General Members found.")
    else:
        print(f"FAIL: Expected 9 members, found {members_count}")

    first_member = page.members.order_by('order').first()
    if first_member:
        print(f"First Member: {first_member.name}")

if __name__ == "__main__":
    verify()
