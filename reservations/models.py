from django.db import models
from django.utils import timezone
from core import models as core_models


class reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    # 예약상태
    STATUS_PENDING = "pending"  # 예약보류
    STATUS_CONFIRMED = "confirmed"  # 예약확정
    STATUS_CANCELED = "canceled"  # 예약취소

    STATUS_CHOICE = (
        (STATUS_PENDING, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCELED, "canceled"),
    )
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICE, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True