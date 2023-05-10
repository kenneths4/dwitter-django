from django.shortcuts import render
from .models import Profile
from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, "base.html")

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})
