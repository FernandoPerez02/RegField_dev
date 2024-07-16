from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from .forms import LoginForm
from gestion.models import Usuario


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            contrasena = form.cleaned_data['contrasena']
            try:
                user = Usuario.objects.get(usuario=usuario, contrasena=contrasena)
                # Si se encuentra al usuario y la contraseña coincide
                # Almacena la información del usuario en la sesión
                request.session['user_id'] = user.id_usuario
                request.session['user_role'] = user.rol
                return redirect('inicio')  # Redirige a la página de inicio o cualquier otra página
            except Usuario.DoesNotExist:
                messages.error(request, 'Usuario o contraseña inválidos')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

from django.shortcuts import redirect




