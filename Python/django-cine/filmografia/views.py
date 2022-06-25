from django.shortcuts import render

# Create your views here.

from django.views import generic

from .models import Director, Pelicula


class IndexView(generic.ListView):
    template_name = 'cine/directores.html'
    model = Director


class DirectorView(generic.DetailView):
    template_name = 'cine/director.html'
    model = Director


class PeliculaView(generic.DetailView):
    template_name = 'cine/pelicula.html'
    model = Pelicula
