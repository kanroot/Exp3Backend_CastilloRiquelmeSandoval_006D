from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CreatorUser(AbstractUser):
    username = models.CharField(verbose_name='Nombre de usuario', max_length=25, primary_key=True)
    email = models.EmailField(verbose_name='Correo electronico', null=False, unique=True)
    bio = models.TextField(verbose_name='Bio', max_length=280, blank=True, default='Perrito')
    banner = models.ImageField(upload_to='pinwin.ImageFile/bytes/filename/mimetype', blank=True, null=True)


class PinRelationship(models.Model):
    pinner_id = models.ForeignKey(CreatorUser, related_name='pinnedBy', on_delete=models.CASCADE)
    pinned_id = models.ForeignKey(CreatorUser, related_name='pins', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['pinner_id', 'pinned_id'], name='unique_const')
        ]

    def __str__(self):
        return 'usuario ' + self.pinner_id.username + ' sigue a '+ self.pinned_id.username


class CreatorImage(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=50, blank=True, default='Perrito')
    descr = models.TextField(blank=True, default='Perrito')
    user = models.ForeignKey(CreatorUser, on_delete=models.CASCADE)


class ImageFile(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)
