from django.contrib import admin

from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = { "slug": ("title",)}
    list_filter = ("state",)
    list_display = ("title", "profile", "slug", "state", "vote",)
    filter_horizontal = ("tags",)
    search_fields = ("title", "description")
    list_per_page = 10
    list_editable = ("state","slug",)
    list_display_list = ("title", )


admin.site.register(Project, ProjectAdmin)