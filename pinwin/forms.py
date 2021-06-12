from django.forms import ModelForm
from .models import CreatorUser


class CreatorUserForm(ModelForm):
    class Meta:
        model = CreatorUser
        fields = ['username', 'email', 'bio']
        labels = {
            'username': 'Nombre usuario',
            'email': 'Correo',
            'bio': 'Biografía'
        }
