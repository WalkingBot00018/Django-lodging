from django.db import models

# Create your models here.
class usuarios(models.Model):
    Nombre=models.CharField(max_length= 38, null=True)
    Direccion=models.CharField(max_length= 20, null=True)
    Telefono=models.CharField(max_length= 21, null=True)
    contrasena=models.CharField(max_length=21, null=True)
