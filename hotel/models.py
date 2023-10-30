from typing import Any
from django.db import models

# Create your models here.
class usuarios(models.Model):
    Nr_doc=models.IntegerField(primary_key=True)
    Nombre=models.CharField(max_length=38, null=True)
    Contraseña=models.CharField(max_length=38, null=True)
    Id_rol=models.CharField(max_length=38, null=True)    

    def __str__(self):
        fila= "Nombre: " + self.Nombre + " - " + "Id_rol: " + self.Id_rol
        return fila
    def delete(self, using: None, keep_parents=False):
        self.Nombre.storage.delete(self.Nombre)
        super().delete()
