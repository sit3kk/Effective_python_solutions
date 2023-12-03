from django.contrib import admin

# Register your models here.


# Path: notes/admin.py
from django.contrib import admin

from .models import Note


from mptt.admin import MPTTModelAdmin
from .models import Topic




admin.site.register(Note)


class TopicAdmin(MPTTModelAdmin):
    list_editable = ['public']


#admin.site.register(Topic, TopicAdmin)

