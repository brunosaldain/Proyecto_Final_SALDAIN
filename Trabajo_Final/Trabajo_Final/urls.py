"""Trabajo_Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path

from blog.views import about_me, ArticuloListView, ArticuloCreateView, ArticuloDetailView, ArticuloDeleteView, ArticuloUpdateView, inicio
from usuario.views import login_view, registro, editarPerfil, editar_avatar, PerfilDetailView, agregar_avatar
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', inicio, name='inicio'),
    path('admin/', admin.site.urls),
    #blog
    path('about/', about_me, name="about_me"),
    path('pages/', ArticuloListView.as_view(), name="listar_articulos"),
    path('crearArticulo/', ArticuloCreateView.as_view(), name="crear_articulo"),
    path('pages/<int:pk>', ArticuloDetailView.as_view(), name="ver_articulo"),
    path('eliminarArticulo/<int:pk>', ArticuloDeleteView.as_view(), name="eliminar_articulo"),
    path('editarArticulo/<int:pk>', ArticuloUpdateView.as_view(), name="editar_articulo"),
    #usuarios
    path('login/', login_view, name="login"),
    path('register/', registro, name='register'),
    path('logout', LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
    path('editarPerfil/', editarPerfil, name="editar_perfil"),
    path('editar-avatar/', editar_avatar, name="editar_avatar"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
    path('perfil/<int:pk>', PerfilDetailView.as_view(), name="ver_perfil"),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # The CKEditor path




    

]

# Para las imagenes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)