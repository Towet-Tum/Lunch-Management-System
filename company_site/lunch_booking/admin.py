from django.contrib import admin
from .models import LunchBooking


# Register your models here.
class LunchAdmin(admin.ModelAdmin):
    list_display = ["user", "date", "booked_at", "code", "booked"]


admin.site.register(LunchBooking, LunchAdmin)
