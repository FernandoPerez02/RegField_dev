from django.db import models

# Create your models here.



   



class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=45)
    documento = models.IntegerField()
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=50)
    fecha = models.DateField()
    id_estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='id_estado')

    class Meta:
        managed = False
        db_table = 'empleado'


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'estado'





