from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Empleado)
admin.site.register(models.Estado)
admin.site.register(models.Inventario)
admin.site.register(models.Labor)
admin.site.register(models.TipoRegistro)
admin.site.register(models.ManejoCafe)

