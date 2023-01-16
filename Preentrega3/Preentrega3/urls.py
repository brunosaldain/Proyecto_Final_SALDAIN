"""Preentrega3 URL Configuration

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
from django.contrib import admin
from django.urls import path
from Preentrega3.views import saludo
from app1.views import listar_profesores, listar_estudiantes, listar_cursos, crear_curso, crear_estudiante, crear_profesor


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('profesores/', listar_profesores, name="listar_profesores"),
    path('estudiantes/', listar_estudiantes, name="listar_estudiantes"),
    path('cursos/', listar_cursos, name="listar_cursos"),
    path('cursoFormulario/', crear_curso, name="crear_curso"),
    path('estudianteFormulario/', crear_estudiante, name="crear_estudiante"),
    path('profesorFormulario/', crear_profesor, name="crear_profesor")
    

]