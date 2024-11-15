from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from travel_project.user_profile.models import UserProfile


UserModel = get_user_model()


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class AppUserCreationForm(UserCreationForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel
        fields = ('email',)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )

        widgets = {
            'username': forms.TextInput(attrs={
                "placeholder": 'First and Last Name',
            }),
            'info': forms.Textarea(attrs={
                "placeholder": 'Tell something about yourself',
            }),
            'profile_picture': forms.TextInput(attrs={
                "placeholder": 'URL field: http/...',
            }),
        }
