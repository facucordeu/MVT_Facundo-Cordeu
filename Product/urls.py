from django.urls import path
from Product.views import *

urlpatterns = [
    path('', home, name ="Inicio"),
    path('formulariocurso/', formulariocurso, name ="AppCurso"),
    path('formularioestudiante/', formularioestudiante, name ="AppEstudiante"),
    path('formularioprofesor/', formularioprofesor, name ="AppProfesor"),
    path('buscarcurso/', busquedacurso, name ="AppBuscarCurso"),
    path('buscarcurso_post/', busqueda_curso_post, name ="AppBuscarCurso_POST"),
    path('buscarestudiante/', busquedaestudiante, name ="AppBuscarEstudiante"),
    path('buscarestudiante_post/', busquedaestudiante_post, name ="AppBuscarEstudiante_POST"),
    path('buscarprofesor/', busquedaprofesor, name="AppBuscarProfesor"),
    path('buscarprofesor_post/', busquedaprofesor_post, name="AppBuscarProfesor_POST"),

]