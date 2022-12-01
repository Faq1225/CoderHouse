from django.urls import *
from Institucion.views import *
from Institucion.static import *

urlpatterns = [
    path('estudiantes/', estudiantes, name = "estudiantes"),
    path('', inicio, name = "inicio"),
    path('materias/', materias, name = "materias"),
    path('profesores/', profesores, name = "profesores"),
    path('estudiantesFormulario/', estudiantesFormulario, name = "estudiantesFormulario"),
    path('profesoresFormulario/', profesoresFormulario, name = "profesoresFormulario"),
    path('materiasFormulario/', materiasFormulario, name = "materiasFormulario"),
    #path('buscarEstudiante', buscarEstudiante, name = "buscarEstudiante"),
]