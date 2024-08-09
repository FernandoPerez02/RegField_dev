from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import FormView
from django import forms
from django.urls import reverse
from .forms import  EmailForm, RestaForm
from django.contrib import messages
from .models import Usuario
from .tokens import custom_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from .functions import send_mail_google
from django.contrib.auth.models import User
from django.utils.encoding import force_str
from django.http import JsonResponse






# Create your views here.




def base(request):
    return render(request, 'base_contra.html')

def enviar(request):
    return render(request, 'enviar.html')
class EmailForm(forms.Form):
    gmail = forms.EmailField(label='Correo Electrónico')

class EnviarMensaje(FormView):
    template_name = 'enviar.html'
    form_class = EmailForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        email = form.cleaned_data['gmail']
        try:
            user = Usuario.objects.get(gmail=email)
        except Usuario.DoesNotExist:
            messages.error(self.request, '')
            return self.form_invalid(form)

        token = custom_token_generator.make_token(user)
        reset_url = self.request.build_absolute_uri(reverse('resta', kwargs={
            'id_usuario': user.id_usuario,
            'token': token,
        }))
        message_text = f'Para restablecer tu contraseña haz click en el siguiente enlace: {reset_url}'

        sent = send_mail_google(email, 'Restablecer contraseña', message_text)
        if sent:
            return JsonResponse({'success': 'Te hemos enviado un mensaje a tu correo electrónico.'})
        else:
            return JsonResponse({'error': 'Hubo un problema al enviar el correo.'})

def resta(request, id_usuario, token):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            # Actualizar la contraseña del usuario
            usuario.contrasena = password
            usuario.save()

            # Mostrar mensaje de éxito
            messages.success(request, '')

            # Redirigir al login
            return redirect('login')
        else:
            # Mostrar mensaje de error si las contraseñas no coinciden
            messages.error(request, '.')
            return redirect('resta', id_usuario=id_usuario, token=token)
    
    # Renderizar la página de restablecimiento de contraseña si es una solicitud GET
    return render(request, 'resta.html', {'id_usuario': id_usuario, 'token': token})
