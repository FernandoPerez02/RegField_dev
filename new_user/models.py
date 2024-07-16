from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=15, unique=True)
    gmail = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=10)
    terminos_condiciones = models.BooleanField(default=False)
    fecha_registro = models.DateField(blank=True, null=True, default= timezone.now)
    
    
    def save(self, *args, **kwargs):
        if not self.id_usuario:
            max_id = Usuario.objects.aggregate(max_id=models.Max('id_usuario'))['max_id']
            max_id_num = int(max_id.split('-')[-1]) if max_id else 0
            new_id_num = str(max_id_num + 1).zfill(3)
            
            inicials = ''.join([word[0] for word in self.rol.split()]).upper()
            
            self.id_usuario = f"US-{inicials}-{new_id_num}"
            
        super().save(*args, **kwargs) 
        
    class Meta:
        managed = True
        db_table = 'usuario'
        
    def __str__(self):
        return self.usuario
    
    class AuthUser(models.Model):
     SELECCIONAR = 'Seleccionar'
    ADMINISTRADOR = 'Administrador'
    ENCARGADO = 'Encargado'
    
    ROL_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (ENCARGADO, 'Encargado'),
    ]
    rol = models.CharField(max_length=20, choices = ROL_CHOICES, default=ENCARGADO)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
    
    
        
    