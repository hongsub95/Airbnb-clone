from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as room_model

# Register your models here.


class RoomInline(admin.TabularInline):
    model = room_model.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "custom profile",
            {
                "fields": (
                    "birthday",
                    "avatar",
                    "gender",
                    "language",
                    "currency",
                    "bio",
                    "superhost",
                )
            },
        ),
    )
    list_filter = UserAdmin.list_filter + ("superhost",)
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
    inlines = (RoomInline,)