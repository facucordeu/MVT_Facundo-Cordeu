from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request, 'index.html', context={})


def formulariocurso(request):

    if request.method == 'POST':
        mi_formulario = formulario_curso(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            cursos = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
            cursos.save()

            return redirect('Inicio')

    context = {'form': formulario_curso()}

    return render(request, "formularios/formulariocurso.html", context)

def formularioestudiante(request):

    if request.method == 'POST':
        mi_formulario = formulario_estudiante(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            estudiantes = Estudiante(nombre=data.get('nombre'), apellido=data.get('apellido'), email = data.get('email'))
            estudiantes.save()

            return redirect('Inicio')

    context = {'form': formulario_estudiante()}

    return render(request, "formularios/formularioestudiante.html", context)

def formularioprofesor(request):

    if request.method == 'POST':
        mi_formulario = formulario_profesor(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            profesores = Profesor(nombre=data.get('nombre'), apellido=data.get('apellido'), email = data.get('email'))
            profesores.save()

            return redirect('Inicio')

    context = {'form': formulario_profesor()}

    return render(request, "formularios/formularioprofesor.html", context)


def busquedacurso(request):

    context = {
        'form': busqueda_curso(),


    }

    return render(request, 'formularios/buscarcurso.html', context)


def busqueda_curso_post(request):

    camada = request.GET.get('camada')

    curso = Curso.objects.filter(camada__icontains = camada)
    context = {
        'curso': curso,


    }

    return render(request, 'formularios/cursofiltrado.html', context)

def busquedaestudiante(request):

    context = {
        'form': busqueda_estudiante(),


    }

    return render(request, 'formularios/buscarestudiante.html', context)


def busquedaestudiante_post(request):

    nombre = request.GET.get('nombre')

    nombres = Estudiante.objects.filter(nombre__icontains=nombre)
    context = {
        'nombres': nombres,


    }

    return render(request, 'formularios/estudiantefiltrado.html', context)


def busquedaprofesor(request):

    context = {
        'form': busqueda_profesor(),


    }

    return render(request, 'formularios/buscarprofesor.html', context)


def busquedaprofesor_post(request):

    nombre = request.GET.get('nombre')

    nombres = Profesor.objects.filter(nombre__icontains=nombre)
    context = {
        'nombres': nombres,


    }

    return render(request, 'formularios/profesorfiltrado.html', context)