from django.contrib import admin
from .models import Univallunos, ArticuloDeportivo, Prestamos, Multa
from BackendDjango import forms

# Register your models here.
admin.site.register(Univallunos, forms.UnivallunosAdmin)
admin.site.register(ArticuloDeportivo)
admin.site.register(Prestamos)
admin.site.register(Multa)

