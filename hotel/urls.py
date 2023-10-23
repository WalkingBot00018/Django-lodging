from django.urls import path
from . import views

urlpatterns= [
    path('', views.inicio, name='index2'),
    path('index', views.index, name='index'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('usuarios/crear', views.crear, name='crear'),
    path('usuarios/editar', views.editar, name='editar'),
]
