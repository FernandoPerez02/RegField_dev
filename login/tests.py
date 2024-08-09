from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.test import Client
from gestion.models import Usuario
from django.contrib.messages import get_messages

class LoginViewTests(TestCase):
    def setUp(self):
        # Crea un usuario de prueba
        self.usuario = Usuario.objects.create(
            usuario='Luis Perez',
            contrasena='1234A*',
            rol='Administrador',
            id_usuario= 'US-A-001'
        )
        self.client = Client()

    def test_login_success(self):
        # Simula una solicitud POST con datos válidos
        response = self.client.post(reverse('login_view'), {
            'usuario': 'Luis Perez',
            'contrasena': '1234A*'
        })
        # Verifica que el inicio de sesión redirige a la página de inicio
        self.assertRedirects(response, reverse('inicio'))
        # Verifica que la información del usuario se almacena en la sesión
        self.assertEqual(self.client.session['user_id'], self.usuario.id_usuario)
        self.assertEqual(self.client.session['user_role'], self.usuario.rol)
        self.assertEqual(self.client.session['user_name'], self.usuario.usuario)

    def test_login_failure(self):
        # Simula una solicitud POST con datos inválidos
        response = self.client.post(reverse('login_view'), {
            'usuario': 'invaliduser',
            'contrasena': 'invalidpassword'
        })
        # Verifica que la respuesta es la página de login
        self.assertEqual(response.status_code, 200)
        # Verifica que se muestra el mensaje de error
        messages_list = list(get_messages(response.wsgi_request))
        self.assertTrue(any(msg.message == 'Usuario o contraseña inválidos' for msg in messages_list))

    def test_login_get(self):
        # Simula una solicitud GET
        response = self.client.get(reverse('login_view'))
        # Verifica que la respuesta es la página de login
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
