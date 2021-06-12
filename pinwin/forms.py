from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CreatorUser


class CreatorUserForm(UserCreationForm):
    class Meta:
        model = CreatorUser
        fields = ['username', 'email', 'bio']
        labels = {
            'username': 'Nombre usuario',
            'email': 'Correo',
            'bio': 'Biografía'
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