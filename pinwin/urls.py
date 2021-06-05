from django.urls import path
from .views import index, catalogo, registro, contacto, quienessomos
urlpatterns = [
    path('', index, name='index.html'),
    path('catalogo/', catalogo, name='catalogo.html'),
    path('registro/', registro, name='registro.html'),
    path('contacto/', contacto, name='contacto.html'),
    path('quienessomos/', quienessomos, name='quienessomos.html')
]