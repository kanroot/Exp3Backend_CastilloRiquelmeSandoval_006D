from django.shortcuts import render, redirect
from .models import CreatorUser
from .forms import CreatorUserForm, CreatorUserChangeForm


def index(request):
    return render(request, 'index.html')


def catalogo(request):
    return render(request, 'catalogo.html')


def quienessomos(request):
    return 'quienessomos'


def registro(request):
    return 'registro'


def contacto(request):
    return 'contacto'


def crud_ver_usuario(request):
    users = CreatorUser.objects.all()
    data = {
        'users': users
    }

    return render(request, 'CRUD/ver_usuarios.html', data)


def crud_crear_usuario(request):
    data = {
        'form': CreatorUserForm()
    }

    if request.method == 'POST':
        formulario = CreatorUserForm(request.POST)

        if formulario.is_valid:
            formulario.save()

        data = {
            'mensaje': 'Usuario escrito satisfactoriamente'
        }

    return render(request, 'CRUD/crear_usuario.html', data)


def crud_modificar_usuario(request, username):
    user = CreatorUser.objects.get(username=username)

    data = {
        'form': CreatorUserChangeForm(instance=user)
    }

    if request.method == 'POST':
        formulario = CreatorUserChangeForm(data=request.POST, instance=user)

        if formulario.is_valid:
            formulario.save()

        data = {
            'mensaje': f'Usuario {user.username} fue modificado con éxito'
        }

    return render(request, 'CRUD/modificar_usuario.html', data)


def crud_eliminar_usuario(request, username):
    CreatorUser.objects.filter(username=username).delete()

    return redirect(crud_ver_usuario)
