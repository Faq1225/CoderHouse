from django.urls import *
from Institucion.views import *
from Institucion.static import *

urlpatterns = [
    path('estudiantes/', estudiantes, name = "estudiantes"),
    path('', inicio, name = "inicio"),
    path('materias/', materias, name = "materias"),
    path('profesores/', profesores, name = "profesores"),
]