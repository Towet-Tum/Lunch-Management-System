from django.urls import path
from . import views

# 3ET1BQP8EQFYR8734SYJNAEM

urlpatterns = [
    path("", views.home, name="home"),
    path("book/", views.book_lunch, name="book_lunch"),
    path("success/", views.booking_success, name="booking_success"),
    path("admin/bookings/", views.lunch_booking_list, name="lunch_booking_list"),
    path("my-bookings/", views.user_bookings, name="user_bookings"),
    path("custom_logout/", views.custom_logout, name="logout"),
    path("ajax/my-view/", views.ajax_view, name="my_ajax_view"),
]
