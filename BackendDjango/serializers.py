from rest_framework.serializers import ModelSerializer
from . import models

class PrestamoSerializer(ModelSerializer):

    class Meta:
        model = models.Prestamos
        fields = ('univalluno', 'articulo', 'fechaPrestamo', 'fechaEntrega', 'fechaVencimiento')