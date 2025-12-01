from django.db import models
from admins.models import Autor
from datetime import date

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    editorial = models.CharField(max_length=100)
    edicion = models.IntegerField(default=date.today().year)
    volumen = models.IntegerField(default=1)
    paginas = models.IntegerField(default=100)
    autores = models.ManyToManyField(Autor, related_name="libros")

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["titulo"]
