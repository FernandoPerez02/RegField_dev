from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', views.nuevo_usuario, name='usuario'),
    path('registrar/', views.post_form, name='registrar'),
]