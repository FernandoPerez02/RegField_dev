from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
     list_display = ['usuario', 'rol', 'gmail', 'fecha_registro']