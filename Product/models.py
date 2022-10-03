from pyexpat import model
from django.db import models

# Create your models here.

class Posteo(models.Model):
    titulo = models.CharField(max_length=40)
    texto = models.TextField()
    fecha = models.DateField()
    autor = models.CharField(max_length=40)

    def __str__(self):
        return self.titulo + "|" + self.autor

opciones_consultas = [
    [0, "Consulta"],
    [1,"Reclamo"],
    [2,"Sugerencia"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre