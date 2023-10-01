from django.db import models
from datetime import datetime, date

class ArticuloDeportivo(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.CharField(max_length=100)
    descripcion = models.TextField()
    valor = models.IntegerField()

class Univallunos(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    esEstudiante = models.BooleanField(default=False)
    tipoDocumento = models.CharField(max_length=100)
    numeroDocumento = models.IntegerField()
    codigoEstudiante = models.IntegerField(unique=True, default="2023000000", blank=True, null=True)
    correo = models.CharField(max_length=100)

    class Meta:
        unique_together = (("numeroDocumento","tipoDocumento"),)

class Multa(models.Model):
    univalluno = models.ForeignKey(Univallunos, on_delete=models.CASCADE, null=True)
    fechaMulta = models.DateField(default=datetime.today())
    valor = models.IntegerField()
    fechaPago = models.DateTimeField(null=True)
    pagado = models.BooleanField(default=False)

class Prestamos(models.Model):
    univalluno = models.OneToOneField(Univallunos, on_delete=models.CASCADE, null=True)
    articulo = models.OneToOneField(ArticuloDeportivo, on_delete=models.CASCADE, null=True)
    fechaPrestamo = models.DateTimeField(default=datetime.today())
    fechaEntrega = models.DateTimeField()
    fechaVencimiento = models.DateTimeField(default=f'{date.today()} 20:00:00', editable=False)