from django import forms

class formulario_curso(forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class formulario_estudiante(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class formulario_profesor(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class busqueda_curso(forms.Form):
    camada = forms.IntegerField()

class busqueda_estudiante(forms.Form):
    nombre = forms.CharField(max_length=30)

class busqueda_profesor(forms.Form):
    nombre = forms.CharField(max_length=30)