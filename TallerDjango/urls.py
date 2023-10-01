"""
URL configuration for TallerDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from BackendDjango.views import generar_multa, pagar_multa


urlpatterns = [
    path('', include('BackendDjango.urls')),
    path('admin/', admin.site.urls),
    path('univallunos/', views.univallunos),
    path('articulos/', views.articulos_deportivos),
    path('prestamos/', views.prestamos),
    path('multas/', views.multas),
    path('reportes/', views.reportes),
    path('multar/<int:no_documento>', generar_multa, name = "agregar multa"),
    path('pagar/<int:no_documento>', pagar_multa, name = "pagar multa"),
]
