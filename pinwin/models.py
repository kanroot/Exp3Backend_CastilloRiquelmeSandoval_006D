from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CreatorUser(AbstractUser):
    username = models.CharField(verbose_name='Nombre de usuario', max_length=25, primary_key=True)
    email = models.EmailField(verbose_name='Correo electronico', unique=True)
    bio = models.TextField(verbose_name='Bio', max_length=280, blank=True, default='Perrito')
    pin = models.IntegerField(verbose_name='Pins', blank=True, default=0)
    banner = models.ImageField(blank=True, null=True)


class CreatorImage(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=50, blank=True, default='Perrito')
    descr = models.TextField(blank=True, default='Perrito')
    user = models.ForeignKey(CreatorUser, on_delete=models.CASCADE)

