from django.shortcuts import render
from .models import Profile
from .forms import DweetForm

def dashboard(request):
    dweet_form = DweetForm()
    return render(request, "dwitter/dashboard.html", {"dweet_form": dweet_form})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})

def profile(request, pk):

    # if user does not have profile create it
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        # gets value from html element
        action = data.get("follow")
        if action == "follow":
            
            current_user_profile.follows.add(profile)

        elif action == "unfollow":
            current_user_profile.follows.remove(profile)

        current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile})
