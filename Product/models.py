from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Familiar(models.Model):

    nombre = models.CharField(max_length=30)
    numpreferido = models.IntegerField()
    fechanac = models.DateField()