from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import ArticuloBlog

# Create your views here.
def inicio(request):
    return render(
        request=request,
        template_name='blog/home.html',
    )
#@login_required
def about_me(request):
    return render(
        request=request,
        template_name='blog/about_me.html',
    )

class ArticuloListView(ListView):
    model = ArticuloBlog
    template_name = 'blog/lista_articulos.html'

class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = ArticuloBlog
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha']
    template_name = "blog/form_articulo.html"
    success_url = reverse_lazy('listar_articulos')

class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = ArticuloBlog
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha']
    template_name = "blog/form_articulo.html"
    success_url = reverse_lazy('listar_articulos')

class ArticuloDetailView(DetailView):
    model = ArticuloBlog
    template_name = "blog/detalle_articulo.html"
    success_url = reverse_lazy('listar_articulos')

class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = ArticuloBlog
    success_url = reverse_lazy('listar_articulos')