from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('usuario/', views.usuario, name='usuario'),
    path('contrasena/', views.contrasena, name='contrasena'),
    path('inicio/', views.inicio, name='inicio'),
    path('empleado/', views.empleado, name = 'empleado'),
    path('labor/', views.labor, name = 'labor'),
    path('inventario/', views.inventario, name = 'inventario'),
    path('cafe/', views.cafe, name='cafe'),
    path('finca/', views.finca, name='finca'),
]