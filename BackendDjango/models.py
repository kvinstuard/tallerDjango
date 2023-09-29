from django.db import models

class ArticuloDeportivo(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.CharField(max_length=100)
    descripcion = models.TextField()
    valor = models.CharField(max_length = 100)

class Univallunos(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    esEstudiante = models.BooleanField(default=False)
    tipoDocumento = models.CharField(max_length=100)
    numeroDocumento = models.CharField(max_length=100)
    codigoEstudiante = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)



