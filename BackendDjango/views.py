from django.shortcuts import render
from django.http import HttpResponse
from . import models
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
   multas = models.Multa.objects.filter(pagado=False)
   contexto = {'multas': multas}
   print("contexto",contexto)
   return render(request, 'multas.html', contexto)

def reportes(request):
   return render(request, 'reportes.html')

def bienvenida(request):
   return render(request, 'index.html')