from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'login3.html')

def usuario(request):
    return render(request, 'crear_usuario.html')

def contrasena(request):
    return render(request, 'contrasena.html')

@login_required
def inicio(request):
    return render(request, 'inicio.html')

def empleado(request):
    return render(request, 'empleado.html')

def inventario(request):
    return render(request, 'inventario.html')

def cafe(request):
    return render(request, 'manejo_cafe.html')

def labor(request):
    return render(request, 'labor.html')

def finca(request):
    return render(request, 'datos_finca.html')