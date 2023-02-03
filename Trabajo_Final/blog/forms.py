from django import forms
from ckeditor_uploader.fields import RichTextUploadingField 

class ArticuloBlogFormulario(forms.Form):
    titulo = forms.CharField(max_length=256)
    subtitulo = forms.CharField(max_length=256)
    cuerpo = forms.RichTextUploadingField()
    autor = forms.CharField(max_length=256)
    fecha = forms.DateTimeField()
    #imagen = forms.ImageField(upload_to='media/')

