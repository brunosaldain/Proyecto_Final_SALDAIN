
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from usuario.models import Avatar

class UserRegisterForm(UserCreationForm):
    # Esto es un ModelForm
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

class AvatarFormulario(forms.ModelForm):
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Avatar
        fields = ['imagen']