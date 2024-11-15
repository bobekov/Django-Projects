from django.shortcuts import render


def index(request):
    return render(request, 'common/home-no-profile.html')


def new_profile(request):
    return render(request, 'common/home-with-profile.html')