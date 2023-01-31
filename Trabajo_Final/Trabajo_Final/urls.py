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
from django.urls import path
from Trabajo_Final.views import saludo
from app1.views import listar_profesores, listar_cursos, crear_curso, crear_estudiante, crear_profesor, buscar_curso, buscar,  EstudianteListView
from blog.views import about_me, ArticuloListView, ArticuloCreateView, ArticuloDetailView, ArticuloDeleteView, ArticuloUpdateView, inicio
from usuario.views import login_view, registro
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('profesores/', listar_profesores, name="listar_profesores"),
    path('estudiantes/', EstudianteListView.as_view(), name="listar_estudiantes"),
    path('cursos/', listar_cursos, name="listar_cursos"),
    path('cursoFormulario/', crear_curso, name="crear_curso"),
    path('estudianteFormulario/', crear_estudiante, name="crear_estudiante"),
    path('profesorFormulario/', crear_profesor, name="crear_profesor"),
    path('buscarCurso/', buscar_curso, name="buscar_curso"),
    path('buscar/', buscar, name="buscar"),
    
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
    path('logout', LogoutView.as_view(template_name='usuario/logout.html'), name='logout')



    

]

# Para las imagenes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)