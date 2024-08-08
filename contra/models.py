from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.CharField(primary_key=True, max_length=200)
    rol = models.CharField(max_length=20)
    usuario = models.CharField(max_length=15)
    gmail = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=10)
    fecha_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'

    def actualizar_contrasena(self, nueva_contrasena):
        self.contrasena = nueva_contrasena
        self.save()