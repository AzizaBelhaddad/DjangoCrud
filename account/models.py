from enum import unique
from random import choices
from uuid import uuid4
from django.db import models
from django.db.models import BooleanField, CharField, DateTimeField, EmailField, ImageField, TextField
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField, ManyToManyField
from blog.models import Tag


# Create your models here.

class Profile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = CharField(max_length=80, null=True, blank=True)
    username = CharField(max_length=80, null= True, blank=True, unique=True)
    email = EmailField(max_length=80, null= True, blank=True, unique=True)
    head_line = CharField(max_length=200, null=True, blank=True) 
    Bio = TextField( null=True, blank=True) 
    image =ImageField(null=True, blank=True, upload_to="profiles/", default="profiles/default.png")
    resume_link= CharField(max_length=200, null=True, blank=True) 
    insta_link= CharField(max_length=200, null=True, blank=True) 
    facebook_link= CharField(max_length=200, null=True, blank=True) 
    linkedin_link= CharField(max_length=200, null=True, blank=True) 
    state = BooleanField(default=False, choices=((True, 'Enabled'), (False, 'Disabled')))
    tags = ManyToManyField(Tag)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)


    def __str__(self):
        return self.username







