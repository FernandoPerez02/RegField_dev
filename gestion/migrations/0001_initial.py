# Generated by Django 5.0.6 on 2024-07-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosFinca',
            fields=[
                ('id_configuracion', models.AutoField(primary_key=True, serialize=False)),
                ('nit_finca', models.IntegerField()),
                ('nombre_finca', models.CharField(max_length=45)),
                ('nombre_responsable', models.CharField(max_length=50)),
                ('telefono_responsable', models.IntegerField()),
                ('direccion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'datos_finca',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=45)),
                ('documento', models.IntegerField()),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'estado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('unidad_medida', models.CharField(max_length=45)),
                ('categoria', models.CharField(max_length=45)),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'inventario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id_labor', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('lote', models.IntegerField()),
                ('fecha_labor', models.DateField()),
            ],
            options={
                'db_table': 'labor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ManejoCafe',
            fields=[
                ('id_cafe', models.AutoField(primary_key=True, serialize=False)),
                ('peso', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'manejo_cafe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id_imagen', models.IntegerField(primary_key=True, serialize=False)),
                ('imagen', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'multimedia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoRegistro',
            fields=[
                ('id_tipo_registro', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_registro', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'tipo_registro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=20)),
                ('usuario', models.CharField(max_length=15)),
                ('gmail', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=10)),
                ('fecha_registro', models.DateTimeField(blank=True, null=True)),
                ('terminos_condiciones', models.IntegerField()),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]
