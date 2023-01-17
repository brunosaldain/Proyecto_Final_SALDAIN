from django.shortcuts import render, redirect
from app1.models import Profesor, Curso, Estudiante
from app1.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario
from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(
        request=request,
        template_name='app1/inicio.html',
    )

def listar_estudiantes(request):
    ## Aqui iria la validacion del permiso lectura estudiantes
    contexto = {
        'estudiantes': Estudiante.objects.all()
    }
    return render(
        request=request,
        template_name='app1/lista_estudiantes.html',
        context=contexto,
    )


def listar_profesores(request):
    contexto = {
        'profesores': Profesor.objects.all()
    }
    return render(
        request=request,
        template_name='app1/lista_profesores.html',
        context=contexto,
    )


def listar_cursos(request):
    contexto = {
        'cursos': Curso.objects.all()
    }
    return render(
        request=request,
        template_name='app1/lista_cursos.html',
        context=contexto,
    )

def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(nombre=data['nombre'], comision=data['comision'])
            curso.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = CursoFormulario()
    return render(
        request=request,
        template_name='app1/form_curso.html',
        context={'formulario': formulario},
    )

def crear_estudiante(request):
    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            estudiante = Estudiante(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            estudiante.save()
            url_exitosa = reverse('listar_estudiantes')
            return redirect(url_exitosa)
    else:  # GET
        formulario = EstudianteFormulario()
    return render(
        request=request,
        template_name='app1/form_estudiante.html',
        context={'formulario': formulario},
    )

def crear_profesor(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], profesion=data['profesion'])
            profesor.save()
            url_exitosa = reverse('listar_profesores')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ProfesorFormulario()
    return render(
        request=request,
        template_name='app1/form_profesor.html',
        context={'formulario': formulario},
    )

def buscar_curso(request):
    return render(request, 'app1/buscar_curso.html')

def buscar(request):
    if request.GET['comision']:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(Q(comision__contains=comision))
        return render(request, 'app1/resultadosBusqueda.html', {'cursos':cursos, 'comision':comision})
    else:
        respuesta = "No enviaste datos"

    #respuesta = f"estoy buscando la comision {request.GET['comision']}"
    return HttpResponse(respuesta)