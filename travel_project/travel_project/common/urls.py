from django.urls import path
from travel_project.common.views import index, new_profile

urlpatterns = [
    path('', index, name='index'),
    path('profile/', new_profile, name='profile-home'),
]