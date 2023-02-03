from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from usuario.forms import UserRegisterForm, UserEditForm, AvatarFormulario
from usuario.models import Avatar

# Create your views here.
def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='usuario/login.html',
        context={'form': form},
    )

def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='usuario/register.html',
        context={'form': formulario},
    )

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "blog/home.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "usuario/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

@login_required
def editar_avatar(request):
    
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES, instance=request.user.avatar) # Aquí me llega toda la info del formulario html

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='usuario/formulario_avatar.html',
        context={'form': formulario},
    )

@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='usuario/formulario_avatar.html',
        context={'form': formulario},
    )


class PerfilDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'usuario/detalle_perfil.html'
    success_url = reverse_lazy('inicio')