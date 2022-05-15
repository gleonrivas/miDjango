from django.db import models


class Libro(models.Model):
    id = models.IntegerField(primary_key=True)
    img = models.TextField()
    nombre = models.TextField()
    autor = models.TextField()
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.nombre

class Recomendado(models.Model):
    id = models.IntegerField(primary_key=True)
    img = models.TextField()
    nombre = models.TextField()
    autor = models.TextField()
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.nombre

# Create your models here.
