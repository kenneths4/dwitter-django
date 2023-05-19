from django.urls import path
from django.contrib.auth import views as auth_views

from .views import dashboard, profile_list, profile, login_view

app_name = "dwitter"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path('login/', login_view, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]