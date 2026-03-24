# Generated internally
from django.db import migrations

def transfer_status(apps, schema_editor):
    MembershipApplication = apps.get_model('membership_options', 'MembershipApplication')
    for app in MembershipApplication.objects.all():
        if app.is_approved:
            app.status = 'active'
            if not app.approved_at:
                app.approved_at = app.created_at
            
            try:
                app.expires_at = app.approved_at.replace(year=app.approved_at.year + app.duration_years)
            except ValueError:
                app.expires_at = app.approved_at.replace(year=app.approved_at.year + app.duration_years, day=28)
        else:
            app.status = 'pending'
            
        app.save(update_fields=['status', 'approved_at', 'expires_at'])

def reverse_transfer(apps, schema_editor):
    MembershipApplication = apps.get_model('membership_options', 'MembershipApplication')
    for app in MembershipApplication.objects.all():
        if app.status == 'active':
            app.is_approved = True
        else:
            app.is_approved = False
        app.save(update_fields=['is_approved'])

class Migration(migrations.Migration):

    dependencies = [
        ('membership_options', '0004_membershipapplication_approved_at_and_more'),
    ]

    operations = [
        migrations.RunPython(transfer_status, reverse_transfer),
    ]
