from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
     return render(request,'paginas/index2.html')

def index(request):
    return render(request, 'paginas/index.html')


def usuarios(request):
    return render(request, 'usuarios/index2.html')


def crear(request):
    return render(request, 'usuarios/crear.html')



def editar(request):
    return render(request, 'usuarios/editar.html')


   
