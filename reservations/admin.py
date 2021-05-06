from django.contrib import admin
from . import models


@admin.register(models.reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_filter = ("status",)
    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )
    list_filter = ("status",)

    @admin.register(models.BookedDay)
    class BookedDayAdmin(admin.ModelAdmin):
        list_display = ("day", "reservation")
