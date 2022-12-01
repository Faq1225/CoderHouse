from django.db import models
from Institucion.models import *

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    email = models.EmailField()
    materiaQueDa = models.CharField(max_length = 40)


class Materia(models.Model):
    nombre = models.CharField(max_length = 40)