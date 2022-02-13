from .models import Profile
from django.contrib import admin

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name","username", "email", "state", "created",)
    # list_display = ("username",)

    list_filter = ("state",)
    list_per_page = 10




admin.site.register(Profile, ProfileAdmin)


