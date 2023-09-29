from django.db import models

class ArticuloDeportivo(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.CharField(max_length=100)
    descripcion = models.TextField()
    valor = models.IntegerField()
    prestado = models.BooleanField(default=False)

class Univallunos(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    esEstudiante = models.BooleanField(default=False)
    tipoDocumento = models.CharField(max_length=100)
    numeroDocumento = models.IntegerField()
    codigoEstudiante = models.IntegerField()
    correo = models.CharField(max_length=100)
    tieneArticulo = models.BooleanField(default=False)

class Prestamos(models.Model):
    univalluno = models.OneToOneField(Univallunos, null=True, on_delete=models.CASCADE)
    articulo = models.OneToOneField(ArticuloDeportivo, null=True, on_delete=models.CASCADE)
    fechaPrestamo = models.DateTimeField().auto_now_add
    fechaEntrega = models.DateTimeField()

class Multa(models.Model):
    fechaMulta = models.DateField().auto_now_add
    valor = models.IntegerField()
    fechaPago = models.DateTimeField()
    pagado = models.BooleanField(default=False)




