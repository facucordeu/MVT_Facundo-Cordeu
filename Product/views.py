from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from Product.forms import  UserEditForm, UserRegistrationForm , ContactoForm
from .models import Posteo
from .forms import ContactoForm, PostForm
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import DeleteView , UpdateView, CreateView


# Create your views here.

def inicio(request):
    posteos = Posteo.objects.all()
    context = {'posts': posteos}
    template2 = loader.get_template('paginas/inicio.html')
    documento = template2.render(context)
    return HttpResponse(documento)

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
                return render(request, "paginas/bienvenida.html", {'mensaje': "Error, el usuario o contraseña es incorrecto"})

        else:
            return render(request, "paginas/bienvenida.html", {'mensaje': "Error, el usuario o contraseña es incorrecto"})
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




@login_required
def perfil(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'paginas/perfil.html', args)

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data

            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.last_name = info['last_name']
            usuario.first_name = info['first_name']
            usuario.save()

            return render(request,"paginas/bienvenida.html")

    else:
        form = UserEditForm(initial = {'email':usuario.email})

    return render(request, "paginas/editarPerfil.html", {"form":form , "usuario":usuario})


class BlogList(ListView):
    model = Posteo
    template_name = "paginas/inicio.html"

class BlogDetail(LoginRequiredMixin,DetailView):
    model = Posteo
    template_name = "paginas/detalleblog.html"



class BlogPost(LoginRequiredMixin,CreateView):
    model = Posteo
    template_name = "paginas/post.html"
    success_url = "/"
    fields = ['titulo' , 'fecha' , 'texto' , 'autor']


class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Posteo
    template_name = "paginas/confirmborrar.html"
    success_url = "/"

class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Posteo
    template_name = "paginas/modificar.html"
    success_url = "/"
    fields = ['titulo' , 'fecha' , 'texto' , 'autor']


def about(self):

    template1 = loader.get_template('paginas/about.html')
    documento = template1.render()

    return HttpResponse(documento)

