from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travel_project.common.urls')),
    path('booking/', include('travel_project.booking.urls')),
    path('country/', include('travel_project.country.urls')),
    path('destination/', include('travel_project.destination.urls')),
    path('flight/', include('travel_project.flight.urls')),
    path('hotel/', include('travel_project.hotel.urls')),
    path('review/', include('travel_project.review.urls')),
    path('room/', include('travel_project.room.urls')),
    path('user_profile/', include('travel_project.user_profile.urls')),
]
