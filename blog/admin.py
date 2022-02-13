from unicodedata import category
from django.contrib import admin
from django.test import tag

from blog.models import Article, Category,Tag

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "state", "category", "created")
    list_filter = ("state", "category")
    # prepopulated_fields = {slug: ("title,")}
    prepopulated_fields = { "slug": ("title",)}
    list_per_page = 2

admin.site.register(Article,ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "state",)

    list_editable = ("state",)

admin.site.register(Category,CategoryAdmin)




admin.site.register([ Tag])
