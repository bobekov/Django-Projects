from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from travel_project.user_profile.forms import AppUserCreationForm, ProfileEditForm
from travel_project.user_profile.models import UserProfile


UserModel = get_user_model()


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'user_profile/create-profile.html'
    success_url = reverse_lazy('profile-home')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class AppUserLoginView(LoginView):
    template_name = 'user_profile/login-to-profile.html'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'user_profile/details-profile.html'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = ProfileEditForm
    template_name = 'user_profile/edit-profile.html'

    def get_success_url(self):
        return reverse_lazy(
            'details-profile',
            kwargs={
                'pk': self.object.pk,
            }
        )


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserProfile
    template_name = 'user_profile/delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        confirmation = request.POST.get('confirmation')
        if confirmation == 'Yes':
            self.get_object().delete()
            return redirect(self.success_url)
        else:
            return redirect('details-profile', self.get_object().pk)




