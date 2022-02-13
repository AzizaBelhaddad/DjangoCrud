from account.models import Profile
from blog.models import Tag
from random import choices
from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models import BooleanField, CharField, DateTimeField, ImageField, IntegerField

# Create your models here.

class Project(models.Model):
    title = CharField(max_length=120)
    slug = CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    profile = ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="projects/")
    source_link = CharField(max_length=200, null=True,blank=True)
    demo_link = CharField(max_length=200, null=True,blank=True)
    tags = ManyToManyField(Tag)
    vote= IntegerField(default=1)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    state = BooleanField(default=False, choices=((True, 'Enabled'), (False, 'Disabled')))




    def __str__(self):
        return self.title

