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
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='id_estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'
    
    def __str__(self):
        return self.nombre


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'estado'


class Inventario(models.Model):
    id_producto = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    unidad_medida = models.CharField(max_length=45)
    categoria = models.CharField(max_length=45)
    fecha = models.DateField()
    id_tipo_registro = models.ForeignKey('TipoRegistro', models.DO_NOTHING, db_column='id_tipo_registro')
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario'


class Labor(models.Model):
    id_labor = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    lote = models.IntegerField()
    fecha_labor = models.DateField()
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labor'

class ManejoCafe(models.Model):
    id_cafe = models.AutoField(primary_key=True)
    peso = models.IntegerField()
    fecha = models.DateField()
    id_tipo_registro = models.ForeignKey('TipoRegistro', models.DO_NOTHING, db_column='id_tipo_registro', blank=True, null=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manejo_cafe'


class Multimedia(models.Model):
    id_imagen = models.IntegerField(primary_key=True)
    imagen = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'multimedia'


class TipoRegistro(models.Model):
    id_tipo_registro = models.AutoField(primary_key=True)
    tipo_registro = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'tipo_registro'
        
    def __str__(self):
        return self.tipo_registro


class Usuario(models.Model):
    id_usuario = models.CharField(primary_key=True, max_length=200)
    rol = models.CharField(max_length=20)
    usuario = models.CharField(max_length=15)
    gmail = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=10)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    terminos_condiciones = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'
        
class DatosFinca(models.Model):
    id_configuracion = models.IntegerField(primary_key=True)
    nit_finca = models.IntegerField()
    nombre_finca = models.CharField(max_length=45)
    nombre_responsable = models.CharField(max_length=50)
    telefono_responsable = models.IntegerField()
    direccion = models.CharField(max_length=45)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datos_finca'