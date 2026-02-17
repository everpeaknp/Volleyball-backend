from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import NoticePage

@admin.register(NoticePage)
class NoticePageAdmin(ModelAdmin):
    list_display = ('__str__', 'status', 'updated_at')
