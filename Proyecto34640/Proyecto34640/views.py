from django.http import *

def saludo(request):
    return HttpResponse("Probando")