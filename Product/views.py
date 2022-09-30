from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from Product.forms import UserRegistrationForm
from .models import Posteo
from .forms import ContactoForm, PostForm


# Create your views here.

def inicio(request):
    posteos = Posteo.objects.all()
    data = {
        'posteo': posteos
    }
    return render(request, 'paginas/inicio.html', data)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "paginas/bienvenida.html", {'mensaje': f"Bienvenido {usuario}"})
            else:
                return render(request, "paginas/bienvenida.html", {'mensaje': "Error, datos incorrectos"})

        else:
            return render(request, "paginas/bienvenida.html", {'mensaje': "Error, formulario erroneo"})
    form = AuthenticationForm()

    return render(request, "paginas/login.html", {'form': form})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "paginas/bienvenida.html", {'mensaje': "Usuario Creado"})

    else:
        form = UserRegistrationForm()

    return render(request, "paginas/register.html", {"form": form})


def contacto(request):
    data = {
        'form': ContactoForm()
    }
    # valido
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'paginas/contacto.html', data)


def agregar_post(request):
    data = {
        'form': PostForm()
    }
    # validamos
    if request.method == 'POST':
        formulario = PostForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Post guardado"
        else:
            data["form"] = formulario

    return render(request, 'paginas/post.html', data)


def listar_post(request):
    publicacion = Posteo.objects.all()

    data = {
        'publicacion': publicacion
    }

    return render(request, 'paginas/listar.html', data)


def modificar_post(request, id):
    publicacion = get_object_or_404(Posteo, id=id)

    data = {
        'form': PostForm(instance=publicacion)
    }
    # Valido
    if request.method == 'POST':
        formulario = PostForm(data=request.POST, instance=publicacion)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente!")
            return redirect(to='listar_post')
        else:
            data["form"] = formulario

    return render(request, 'paginas/modificar.html', data)


def eliminar_post(request, id):
    publicacion = get_object_or_404(Posteo, id=id)
    publicacion.delete()
    messages.success(request, "Eliminado correctamente!")
    return redirect(to='listar_post')