from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField 

# Create your models here.
class ArticuloBlog(models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = RichTextUploadingField() # CKEditor Rich Text Field
    autor = models.CharField(max_length=256)
    fecha = models.DateTimeField()
    imagen = models.ImageField(upload_to='imagenes_articulos', null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.titulo} - {self.fecha} - {self.autor}"