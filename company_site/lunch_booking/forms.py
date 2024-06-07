# lunch_booking/forms.py

from django import forms
from .models import LunchBooking


class LunchBookingForm(forms.ModelForm):
    class Meta:
        model = LunchBooking
        fields = []
