from django.urls import path, include
from travel_project.country import views

urlpatterns = [
    path('details_country/', views.details_country, name='details-country'),
    path('add_country/', views.add_new_country, name='add-country'),
    path('<int:pk>/', include([
        path('edit_country/', views.edit_country, name='edit-country'),
        path('delete_country/', views.delete_country, name='delete-country'),
    ])),
]