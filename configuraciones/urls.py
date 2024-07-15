from django.urls import path
from . import views

urlpatterns = [
    path('confi/', views.config, name='confi'),
    path('agregarfinca/', views.agregarconfi, name='agregarfinca')
]