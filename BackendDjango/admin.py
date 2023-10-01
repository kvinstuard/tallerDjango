from django.contrib import admin
from .models import Univallunos, ArticuloDeportivo, Prestamos, Multa

# Register your models here.
admin.site.register(Univallunos)
admin.site.register(ArticuloDeportivo)
admin.site.register(Prestamos)
admin.site.register(Multa)
