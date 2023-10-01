from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.db.models import Count, Sum
from django.db.models.functions import TruncDate
from rest_framework.views import APIView
from . import serializers

from .models import Univallunos, Multa, Prestamos, ArticuloDeportivo
import json
from datetime import date

miscrip = """<div class="dropdown">
  <button class="dropbtn">Dropdown</button>
  <div class="dropdown-content">
    <a href="#">Link 1</a>
    <a href="#">Link 2</a>
    <a href="#">Link 3</a>
  </div>
</div>"""

# Create your views here.

def univallunos(request):
   return render(request, 'univallunos.html')

def articulos_deportivos(request):
   return render(request, 'articulos_deportivos.html')

def prestamos(request):
   return render(request, 'prestamos.html')

def multas(request):
   # Obtener las multas por día
   multas = Multa.objects.filter(fechaMulta__range=('2001-01-01', datetime.today()))
   data = multas.annotate(dia=TruncDate('fechaMulta')).values('fechaMulta').annotate(total=Sum('valor'))
   contexto = {
                'multas': data
            }
   print("contexto_multas:",data)
   return render(request, 'multas.html', contexto)

def reportes(request):
   # obtener prestamos por deportes
   prestamos_deportes = Prestamos.objects.filter(fechaPrestamo__range=('2001-01-01', datetime.today()))
   prestamos_por_articulo = prestamos_deportes.values('articulo__nombre').annotate(total=Count('id'))
   # obtener prestamos por día
   prestamos = Prestamos.objects.filter(fechaPrestamo__range=('2001-01-01', datetime.today()))
   data = prestamos.annotate(dia=TruncDate('fechaPrestamo')).values('dia').annotate(total=Count('id'))
   # creamos el contexto
   contexto = {
        "nombres_articulos": [articulo['articulo__nombre'] for articulo in prestamos_por_articulo],
        "cantidades": [articulo['total'] for articulo in prestamos_por_articulo],
        "dias_articulos": [dia['dia'].strftime('%Y-%m-%d') for dia in data],
        "cantidades_dias": [dia['total'] for dia in data],
       }
   print("contexto:", contexto)
   return render(request, 'reportes.html', contexto)

def bienvenida(request):
   return render(request, 'index.html')

import json

from datetime import date, datetime

# Vista para generar multa a Univalluno

def generar_multa(request, no_documento):
    try:
        univalluno = Univallunos.objects.get(numeroDocumento=no_documento)
    except Exception:
        error_data = {
        'error': f'el univalluno con codigo: {no_documento} no pudo ser encontrado.'
        }
        response_data = json.dumps(error_data)
        return HttpResponse(response_data, content_type='application/json', status=500)

    if univalluno.tipoDocumento == 'c.c':
        try:
            prestamo = Prestamos.objects.get(univalluno=univalluno)
        except Exception:
            error_data = {
            'error': 'el univalluno no tiene un articulo.'
            }
            response_data = json.dumps(error_data)
            return HttpResponse(response_data, content_type='application/json', status=500)
        
        # Se crea la multa y se asocia al univalluno
        multa = Multa.objects.create(
            univalluno=univalluno,
            valor=round(prestamo.articulo.valor * 0.15),
            fechaPago=None,
            pagado=False
        )
        multa_data = {
            'id': multa.id,
            'valor': multa.valor,
            'fechaPago': multa.fechaPago,
            'pagado': multa.pagado
        } 
        response_data = json.dumps(multa_data)
        return HttpResponse(response_data, content_type='application/json', status=200)
    else:
        error_data = {
            'error': 'tipo de documento invalido, debe ser: "c.c"'
        }
        response_data = json.dumps(error_data)
        return HttpResponse(response_data, content_type='application/json', status=500)

# Vista para pagar las multas

def pagar_multa(request, no_documento):
    try:
        univalluno = Univallunos.objects.get(numeroDocumento=no_documento)
    except Exception:
        error_data = {
        'error': f'el univalluno con codigo: {no_documento} no pudo ser encontrado.'
        }
        response_data = json.dumps(error_data)
        return HttpResponse(response_data, content_type='application/json', status=500)

    try:
        prestamo = Prestamos.objects.get(univalluno=univalluno)
    except Exception:
        error_data = {
        'error': 'el univalluno no tiene un articulo.'
        }
        response_data = json.dumps(error_data)
        return HttpResponse(response_data, content_type='application/json', status=500)
    
    # se paga la primera multa (si tiene varias)
    
    multas = Multa.objects.filter(univalluno=univalluno, pagado=False)
    n_multas = len(multas)
    if n_multas == 0:
        message_data = {
            'mensaje': f'el univalluno con codigo: {no_documento} no presenta multas por pagar por el/los articulo/s.'
        }
        response_data = json.dumps(message_data)
        return HttpResponse(response_data, content_type='application/json', status=200)
    multas[0].fechaPago = datetime.today()
    multas[0].pagado = True 
    multas[0].save()

    # se libera al univalluno y el articulo deportivo en caso de haber pagado todas
    # las multass

    if n_multas == 1:
        prestamo.delete()
        message_data = {
            'mensaje': f'el univalluno con codigo: {no_documento} pago la multa con id: {multas[0].id}. Y queda a paz y salvo!'
        }
        response_data = json.dumps(message_data)
        return HttpResponse(response_data, content_type='application/json', status=200)
    else:
        message_data = {
            'mensaje': f'el univalluno con codigo: {no_documento} pago la multa con id: {multas[0].id}. Pero quedan otras pendientes.'
        }
        response_data = json.dumps(message_data)
        return HttpResponse(response_data, content_type='application/json', status=200)
    
# Vista para ver todos los prestamos
def viewAllPrestamos(request):
    prestamos = Prestamos.objects.all()
    prestamos_serializer = serializers.PrestamoSerializer(prestamos, many=True).data
    return HttpResponse(json.dumps(prestamos_serializer), content_type='application/json', status=200)