from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lunch_booking/", include("lunch_booking.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]
