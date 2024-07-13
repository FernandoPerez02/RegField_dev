from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def nuevo_usuario(request):
    return render(request, 'crear_usuario.html')

def post_form(request):
    if request.method == 'POST':
        
        rol = request.POST['rol']
        usuario = request.POST['usuario']
        gmail = request.POST['gmail']
        contrasena = request.POST['contrasena']
        terminos_condiciones = request.POST['terminos_condiciones']
        
        form_data = {
            'rol': rol,
            'usuario': usuario,
            'gmail': gmail,
            'contrasena':contrasena,
            'terminos_condiciones': terminos_condiciones
            }
        
        form = forms.UsuarioForm(form_data)
        
        if form.is_valid():
            form.save()
            return HttpResponse('Registro exitoso')
        else:
            return HttpResponse('Registro Fallido')

    


""" def addRegistro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el formulario si es válido
            return HttpResponse('Registro exitoso')  # Puedes cambiar esto por una redirección a otra URL o mostrar un mensaje diferente
        else:
            return render(request, 'tu_template.html', {'form': form})  # Renderiza el formulario con errores si no es válido
    else:
        form = UsuarioForm()  # Crea una instancia del formulario para mostrarlo en GET

    return render(request, 'tu_template.html', {'form': form}) """
