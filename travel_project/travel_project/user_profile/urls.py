from django.contrib.auth.views import LogoutView
from django.urls import path, include
from travel_project.user_profile import views

urlpatterns = [
    path('create/', views.AppUserRegisterView.as_view(), name='create-profile'),
    path('login/', views.AppUserLoginView.as_view(), name='login-to-profile'),
    path('logout/', LogoutView.as_view(), name='logout-from-profile'),
    path('profile/<int:pk>/', include([
        path('', views.ProfileDetailView.as_view(), name='details-profile'),
        path('edit/', views.ProfileEditView.as_view(), name='edit-profile'),
        path('delete/', views.ProfileDeleteView.as_view(), name='delete-profile'),
    ]))
]