from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import usuarios
from .forms import usuarioform
# Create your views here.

def inicio(request):
     return render(request,'paginas/index2.html')

def index(request):
    return render(request, 'paginas/index.html')


def usu(request):
    usuario_list= usuarios.objects.all()
    return render(request, 'usuarios/index2.html', {'usuario_list': usuario_list})


def crear(request):
    formulario = usuarioform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/crear.html', {'formulario': formulario})



def editar(request, Nr_doc):
    usuarios = usuarios.objects.get(Nr_doc=Nr_doc)
    formulario = usuarioform(request.POST or None, request.FILES or None, instance=usuarios)
    return render(request, 'usuarios/editar.html', {'formulario': formulario})


def eliminar(request, Nr_doc):
    usuarios = usuarios.objects.get(Nr_doc=Nr_doc)
    usuarios.delete() 
    return redirect('usuarios')



   
