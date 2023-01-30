from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    profesion = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Curso(models.Model):
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField()
    esta_entregado = models.BooleanField(default=False)