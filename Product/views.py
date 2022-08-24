from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Familiar


# Create your views here.
def home(request):
    return render(request, 'index.html', context={})


def crear_familiar(request, nombre):
    familiar1 = Familiar.objects.create(nombre=nombre, numpreferido=54, fechanac="1990-01-27")

    context = {'familiar1': familiar1,}

    return render(request, "index.html", context)

def ver_familiar(request):
    familiares = Familiar.objects.all()
    context = {'familiares': familiares, }
    return render(request, "verfamilia.html", context)

