from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .functions import send_mail_google

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
            message_text = 'Bienvenido a Regfield.  Acabas de registrar un nuevo usuario en el aplicativo'
            sent = send_mail_google(gmail, 'Registro Exitoso', message_text)
            return redirect('login')
        else:
            print(form.errors)
            return redirect('usuario')