from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida),
    path('univallunos/', views.univallunos),
    path('articulos/', views.articulos_deportivos)
]