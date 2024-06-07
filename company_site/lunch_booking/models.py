from django.db import models
from django.contrib.auth.models import User
import random
import string
from datetime import datetime, time


class LunchBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    booked_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=7, unique=True)
    booked = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = "".join(
                random.choices(string.ascii_uppercase + string.digits, k=7)
            )
        super(LunchBooking, self).save(*args, **kwargs)

    def is_booking_allowed(self):
        now = datetime.now()
        return now.time() < time(19, 0)  # 7 PM

    def __str__(self):
        return f"{self.user.username} - {self.date}"
