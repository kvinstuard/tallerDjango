from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def univallunos(request):
   return HttpResponse("<h1>seccion univallunos en desarrollo</h1>")

def articulos_deportivos(request):
   return HttpResponse("<h1>seccion articulos deportivos en desarrollo</h1>")

def bienvenida(request):
   return HttpResponse("<h1>seccion bienvenida en desarrollo</h1>")