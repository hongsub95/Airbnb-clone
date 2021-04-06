from django.contrib import admin
from . import models


@admin.register(models.reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass
