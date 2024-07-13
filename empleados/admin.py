from django.contrib import admin

# Register your models here.

from .models import Empleado, Estado

admin.site.register(Empleado)
admin.site.register(Estado)