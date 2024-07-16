from django import forms
from gestion import models

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ['rol', 'usuario', 'gmail', 'contrasena', 'terminos_condiciones']