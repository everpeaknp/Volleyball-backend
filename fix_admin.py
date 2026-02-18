#!/usr/bin/env python3
import os
import re

def fix_admin_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Fix broken class definitions
    content = re.sub(r'class class (\w+)\(ModelAdmin\)\(admin\.ModelAdmin\):', r'class \1(ModelAdmin):', content)
    content = re.sub(r'class class (\w+)\(TabularInline\)\(admin\.TabularInline\):', r'class \1(TabularInline):', content)
    content = re.sub(r'class class (\w+)\(StackedInline\)\(admin\.StackedInline\):', r'class \1(StackedInline):', content)
    
    # Fix imports - add unfold imports if not present
    if 'unfold.admin import' not in content:
        content = re.sub(r'from django\.contrib import admin', 'from django.contrib import admin\nfrom unfold.admin import ModelAdmin, TabularInline, StackedInline', content)
    
    # Remove duplicate imports
    content = re.sub(r'from django\.contrib import admin\nfrom django\.contrib import admin', 'from django.contrib import admin', content)
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Fixed {filepath}")

# Fix all admin files
admin_files = [
    'apps/events_options/admin.py',
    'apps/news_options/admin.py', 
    'apps/team_options/admin.py',
    'apps/committee_options/admin.py',
    'apps/gallery_options/admin.py',
    'apps/about_options/admin.py',
    'apps/membership_options/admin.py',
    'apps/contact_options/admin.py',
    'apps/core/admin.py',
    'apps/pages/admin.py'
]

for filepath in admin_files:
    if os.path.exists(filepath):
        fix_admin_file(filepath)