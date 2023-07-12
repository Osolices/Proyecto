from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(primary_key=True,max_length=45)
    foto = models.ImageField(upload_to='categorias',null=True)
    
    def __str__(self) -> str:
        return self.nombre
    
class Tecnica(models.Model):
    nombre = models.CharField(primary_key=True,max_length=45)        

    def __str__(self) -> str:
        return self.nombre

class Obra(models.Model):
    id_obra= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=100)
    historia = models.TextField( default='')
    descripcion = models.TextField(default='')
    tecnica= models.ForeignKey(Tecnica, on_delete=models.CASCADE)
    precio = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='obras', null=True, default='')
    estado= models.BooleanField(default=False)
    comentario= models.TextField(default='Sin Comentarios')
    autor= models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return str(self.id_obra) +"-"+ str(self.nombre)
    
class Galeria(models.Model):
    id= models.AutoField(primary_key=True)
    foto_1= models.ImageField(upload_to='galeria')
    foto_2= models.ImageField(upload_to='galeria')
    foto_3= models.ImageField(upload_to='galeria')
    obra= models.ForeignKey(Obra, on_delete=models.CASCADE)
    angulo_1 = models.CharField(default='Frontal', max_length=100)
    angulo_2 = models.CharField(default='Lateral', max_length=100)
    angulo_3 = models.CharField(default='Trasero', max_length=100)
    def __str__(self) -> str:
        return f'{self.obra.nombre} Galeria'
 
class Perfiles(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', null=True, default='avatar.png')
    grupo = models.CharField(default='Artista Novato',max_length=100)
    descripcion = models.TextField(default='Sin descripcion')
    def __str__(self):
        return f'{self.user.username} Perfil'

class Contacto(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(default='', max_length=100)
    rut = models.CharField(default='', max_length=100)
    correo = models.CharField(default='', max_length=100)
    telefono = models.CharField(default='', max_length=100)
    descripcion = models.TextField(default='')


    def __str__(self) -> str:
        return super().__str__()    

class Compra(models.Model):
    id= models.AutoField(primary_key=True)
    productos = models.JSONField()
    
    def __str__(self) -> str:
        return super().__str__() 