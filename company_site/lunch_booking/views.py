from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import LunchBookingForm
from .models import LunchBooking
from datetime import time, date
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "lunch_booking/home.html")


@login_required
def book_lunch(request):
    if not LunchBooking.objects.filter(
        user=request.user, date=timezone.now().date()
    ).exists():
        if request.method == "POST":
            form = LunchBookingForm(request.POST)
            if form.is_valid():
                booking = LunchBooking(
                    user=request.user, date=timezone.now().date(), booked=True
                )
                booking.save()
                messages.success(request, "Lunch booked successfully!")
                return redirect("booking_success")
        else:
            form = LunchBookingForm()

        return render(request, "lunch_booking/book_lunch.html", {"form": form})
    else:
        messages.error(request, "You have already booked lunch for tomorrow.")
        return redirect("home")


@login_required
def booking_success(request):
    return render(request, "lunch_booking/booking_success.html")


@staff_member_required
def lunch_booking_list(request):
    # Get today's date
    today = date.today()
    # Query for all bookings for today
    bookings = LunchBooking.objects.filter(booked=True, date=today)
    context = {"bookings": bookings, "today": today}
    return render(request, "lunch_booking/lunch_booking_list.html", context)


@login_required
def user_bookings(request):
    # Retrieve bookings for the logged-in user ordered by most recent booking time
    user = request.user
    bookings = LunchBooking.objects.filter(user=user).order_by("-booked_at")

    return render(request, "lunch_booking/user_bookings.html", {"bookings": bookings})


def custom_logout(request):
    logout(request)
    return redirect("/lunch_booking")


@csrf_exempt
def ajax_view(request):
    if request.method == "POST":
        data = request.POST.get("data", None)
        response_data = {
            "message": "Data received successfully!",
            "received_data": data,
        }
        return JsonResponse(response_data)
    return JsonResponse({"error": "Invalid request"}, status=400)
