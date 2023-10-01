from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Univallunos, Multa, Prestamos, ArticuloDeportivo
import json

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
   multas = Multa.objects.filter(pagado=False)
   contexto = {'multas': multas}
   print("contexto",contexto)
   return render(request, 'multas.html', contexto)

def reportes(request):
   return render(request, 'reportes.html')

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