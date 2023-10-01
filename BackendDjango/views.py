from django.shortcuts import render
from django.http import HttpResponse

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
   return HttpResponse("<script src='univallunos.js'></script>")

def articulos_deportivos(request):
   return HttpResponse("<script src='articulos_deportivos.js'></script>")

def prestamos(request):
   return HttpResponse("<script src='prestamos.js'></script>")

def multas(request):
   return HttpResponse("<script src='multas.js'></script>")

def reportes(request):
   return HttpResponse("<script src='reportes.js'></script>")

def bienvenida(request):
   return render(request, 'index.html')