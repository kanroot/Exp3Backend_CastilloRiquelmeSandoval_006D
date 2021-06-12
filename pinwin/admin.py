from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# Register your models here.

from .models import CreatorUser, CreatorImage, PinRelationship


@admin.register(CreatorUser)
class CreatorUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Datos usuario",
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password", 'bio', 'banner'),
            },
        ),
    )
    add_fieldsets = (
        (
            "Datos usuario",
            {
                "classes": ("wide",),
                "fields": ("username", "email", 'password1', 'password2')
            }
        ),
    )
    list_display = ('username', 'email')


admin.site.register(CreatorImage)
admin.site.register(PinRelationship)
admin.site.unregister(Group)
