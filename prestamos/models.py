from django.db import models
from datetime import date
from admins.models import Lector, Bibliotecario
from libros.models import Libro

# Create your models here.

class Prestamo(models.Model):
    fechaPrestamo = models.DateField(default=date.today())
    fechaDevolucion = models.DateField()
    estadoLibro = models.CharField(max_length=10)
    lector = models.ForeignKey(Lector, on_delete=models.PROTECT, related_name='prestamos')
    bibliotecario = models.ForeignKey(Bibliotecario, on_delete=models.PROTECT, related_name='prestamos')
    libro = models.ForeignKey(Libro, on_delete=models.PROTECT, related_name='prestamos')

    def __str__(self):
        return f"Préstamo {self.libro.titulo}"

    class Meta:
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'
        ordering = ['-fechaPrestamo']


class Devolucion(models.Model):
    fechaDevolucion = models.DateField(default=date.today())
    estadoLibro = models.CharField(max_length=10)
    prestamo = models.OneToOneField(Prestamo, on_delete=models.PROTECT)

    def __str__(self):
        return f"Devolución {self.prestamo.libro.titulo}"

    class Meta:
        verbose_name = 'Devolución'
        verbose_name_plural = 'Devoluciones'
