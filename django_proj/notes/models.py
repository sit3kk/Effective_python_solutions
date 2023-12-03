from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel


from mptt.models import MPTTModel, TreeForeignKey


class Topic(MPTTModel):
    
    name = models.CharField(max_length=100) 
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    public = models.BooleanField(default=True) 

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Note (TimeStampedModel):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


