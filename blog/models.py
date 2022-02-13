from django.urls import reverse
from django.db import models
from django.db.models import ImageField
from django.db.models.fields import SlugField, CharField, DateTimeField, TextField, IntegerField, BooleanField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.utils.text import slugify


# Create your models here.
LIST_STATE = (
    {0, "disable"},
    {1, "enable"}
)
class Article(models.Model):

    title = CharField(max_length=120, unique=True)
    slug = SlugField( unique=True, db_index=True,null=True, blank=True)
    description = TextField(null=True)
    category = ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    state = IntegerField(default=0, choices= LIST_STATE)
    tags = ManyToManyField('Tag')
    picture = ImageField(null=True, upload_to="articles/")
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    deleted = BooleanField(default=False, null=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kargs):
        if  self.slug is None:
            self.slug = slugify(self.title)

        super().save(*args, **kargs)

    def get_absolute_url(self):
        return reverse("show_article", kwargs= {"slug ": self.slug})

    def delete(self, *args, **kargs):
        self.deleted =True
        super().save(*args, **kargs)


class Category(models.Model):
    class Meta:
            verbose_name = "categorie"

    name = CharField(max_length=20 )
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    state = IntegerField(default=0, choices= LIST_STATE)



    def __str__(self):
        return self.name


class Tag(models.Model):
    name = CharField(max_length=20)


    def __str__(self):
        return self.name


