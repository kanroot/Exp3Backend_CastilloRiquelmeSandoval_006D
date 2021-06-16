from rest_framework import serializers
from .models import CreatorUser


class CreatorUserSerializador(serializers.ModelSerializer):
    class Meta:
        model = CreatorUser
        fields = ['username', 'email', 'bio']
