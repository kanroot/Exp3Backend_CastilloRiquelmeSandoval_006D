from django.shortcuts import render


# Create your views here.

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
