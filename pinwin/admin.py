from django.contrib import admin

# Register your models here.

from .models import CreatorUser, CreatorImage

admin.site.register(CreatorUser)
admin.site.register(CreatorImage)