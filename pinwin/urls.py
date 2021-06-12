from django.urls import path
from .views import (index,
                    catalogo,
                    registro,
                    contacto,
                    quienessomos,
                    crud_ver_usuario,
                    crud_crear_usuario,
                    crud_modificar_usuario,
                    crud_eliminar_usuario)
urlpatterns = [
    path('', index, name='index.html'),
    path('catalogo/', catalogo, name='catalogo.html'),
    path('registro/', registro, name='registro.html'),
    path('contacto/', contacto, name='contacto.html'),
    path('quienessomos/', quienessomos, name='quienessomos.html'),
    path('ver/usuarios', crud_ver_usuario, name='ver_usuarios.html'),
    path('crear/usuarios', crud_crear_usuario, name='crear_usuario.html'),
    path('modificar/<username>', crud_modificar_usuario, name='modificar_usuario.html'),
    path('eliminado/<username>', crud_eliminar_usuario, name='eliminar_usuario')
]