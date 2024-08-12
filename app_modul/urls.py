from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('base/', views.base, name='base'),
    path('obtener_fechas/', views.obtener_fechas, name='obtener_fechas'),

]