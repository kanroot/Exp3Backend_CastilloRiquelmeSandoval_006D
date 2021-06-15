from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CreatorUser
from django import forms


class CreatorUserForm(UserCreationForm):
    class Meta:
        model = CreatorUser
        fields = ['username', 'email', 'bio']
        labels = {
            'username': 'Nombre usuario',
            'email': 'Correo',
            'bio': 'Biografía'
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'validate',
                }),
            'email': forms.TextInput(
                attrs={
                    'type': 'email',
                    'class': 'validate',
                }
            )
        }


class CreatorUserChangeForm(UserChangeForm):
    class Meta:
        model = CreatorUser
        fields = ['username', 'email', 'bio']
        labels = {
            'username': 'Nombre usuario',
            'email': 'Correo',
            'bio': 'Biografía'
        }