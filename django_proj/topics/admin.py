from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Topic

@admin.register(Topic)
class TopicAdmin(DjangoMpttAdmin):
    list_display = ['title', 'is_public']
    list_editable = ['is_public']