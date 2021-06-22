from django.shortcuts import render, redirect
from .models import CreatorUser
from .forms import CreatorUserForm, CreatorUserChangeForm

'''Rest services'''
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import CreatorUserSerializador


def index(request):
    return render(request, 'index.html')


def catalogo(request):
    return render(request, 'catalogo.html')


def quienessomos(request):
    return render(request, 'quienessomos.html')


def registro(request):
    return render(request, 'registro.html')


def contacto(request):
    return render(request, 'contacto.html')


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


@csrf_exempt
@api_view(['GET', 'POST'])
def lista_creatorUser(request):
    if request.method == 'GET':

        user = CreatorUser.objects.all()

        serializer = CreatorUserSerializador(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        data = JSONParser().parse(request)

        serializer = CreatorUserSerializador(data=data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
