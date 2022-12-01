from django.shortcuts import render
from django.http import *
from Institucion.templates import *
from Institucion.static import *
from Institucion.models import *
from Institucion.forms import *

# Create your views here.
def estudiantes(request):
    return render(request, "estudiantes.html")
def inicio(request):
    return render(request, "inicio.html")
def materias(request):
    return render(request, "materias.html")
def profesores(request):
    return render(request, "profesores.html")

def estudiantesFormulario(request):
    if request.method == "POST":

        miFormulario = estudianteForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(informacion)
            nombrecito = informacion['nombre']
            apellidito = informacion['apellido']
            emailcito = informacion['email']
            estudiante = Estudiante(nombre = nombrecito, apellido = apellidito, email = emailcito)
            estudiante.save()
            return render(request, "inicio.html")
    else:

        miFormulario = estudianteForm()

    return render(request, "estudiantesFormulario.html", {"miFormulario":miFormulario})


def materiasFormulario(request):
    if request.method == "POST":

        miFormulario = materiaForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(informacion)
            nombrecito = informacion['nombre']
            materia = Materia(nombre = nombrecito)
            materia.save()
            return render(request, "inicio.html")
    else:

        miFormulario = materiaForm()

    return render(request, "materiasFormulario.html", {"miFormulario":miFormulario})

def profesoresFormulario(request):
    if request.method == "POST":

        miFormulario = profesorForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(informacion)
            nombrecito = informacion['nombre']
            apellidito = informacion['apellido']
            emailcito = informacion['email']
            materita = informacion['materiaQueDa']
            profesor = Profesor(nombre = nombrecito, apellido = apellidito, email = emailcito, materiaQueDa = materita)
            profesor.save()
            return render(request, "inicio.html")
    else:

        miFormulario = profesorForm()

    return render(request, "profesoresFormulario.html", {"miFormulario":miFormulario})

def busquedaEstudiante(request):
    return render (request, "busquedaEstudiante.html")

def resultadoBusqEst(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        estudiantes = Estudiante.objects.filter(nombre = nombre)
        return render(request, "resultadoBusqEst.html", {"estudiantes":estudiantes})
    else:
        return render(request, "busquedaNula.html")

