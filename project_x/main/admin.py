from django.contrib import admin
from .models import ArtisanProfile, User

# Register your models here.

admin.site.register(ArtisanProfile)
admin.site.register(User)