from django.shortcuts import render
from django.http import *
from Institucion.templates import *
from Institucion.static import *

# Create your views here.
def estudiantes(request):
    return render(request, "estudiantes.html")
def inicio(request):
    return render(request, "inicio.html")
def materias(request):
    return render(request, "materias.html")
def profesores(request):
    return render(request, "profesores.html")