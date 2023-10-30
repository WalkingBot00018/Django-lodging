from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns= [
    path('', views.inicio, name='index2'),
    path('index', views.index, name='index'),
    path('usuarios', views.usu, name='usuarios'),
    path('usuarios/crear', views.crear, name='crear'),
    path('usuarios/editar', views.editar, name='editar'),
    path('eliminar/<int:Nr_doc>', views.eliminar, name='eliminar'),
    path('usuarios/editar/<int:Nr_doc>',views.editar, name='editar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
