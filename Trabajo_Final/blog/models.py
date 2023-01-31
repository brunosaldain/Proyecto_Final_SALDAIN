from django.db import models
from datetime import datetime

# Create your models here.
class ArticuloBlog(models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=256)
    fecha = models.DateTimeField()
    #imagen = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return f"{self.titulo} - {self.fecha} - {self.autor}"