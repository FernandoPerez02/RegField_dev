from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')


class RestaForm(forms.Form):
    nueva_contrasena = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)
    confrimar_contrasena = forms.CharField(label='Confirmar nueva contraseña', widget=forms.PasswordInput)