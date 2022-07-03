from distutils.command import upload
from tkinter.tix import Tree
from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to="imagenes/",null=True, verbose_name="Foto", blank=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre", null= True)
    documento = models.CharField(max_length=100, verbose_name="Cédula", null=True)
    correo = models.CharField(max_length=100, verbose_name="Email", null = True)
    compañia = models.CharField(max_length=100, verbose_name="Empresa", null= True)

    def __str__(self):
        fila = "Nombre:" + self.nombre + "-" + "Correo:" + self.correo
        return fila

    def delete(self,using=None,keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()
