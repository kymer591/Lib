from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    ROL_CHOICES = [
        ('lector', 'Lector'),
        ('bibliotecario', 'Bibliotecario'),
        ('admin', 'Administrador'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)

    def __str__(self):
        return self.username


class Persona(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    ci = models.CharField(max_length=9, unique=True)
    fechaNacimiento = models.DateField(default=timezone.now)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=8, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.apellidos} {self.nombres}"

    class Meta:
        ordering = ['apellidos', 'nombres']


class Autor(models.Model):
    nacionalidad = models.CharField(max_length=20)
    biografia = models.TextField(blank=True, null=True)
    persona = models.OneToOneField(Persona, on_delete=models.PROTECT)

    def __str__(self):
        return f"Autor: {self.persona.apellidos} {self.persona.nombres}"

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Lector(models.Model):
    ru = models.CharField(max_length=7, unique=True)
    persona = models.OneToOneField(Persona, on_delete=models.PROTECT)

    def __str__(self):
        return f"Lector: {self.persona.apellidos} {self.persona.nombres}"


class Bibliotecario(models.Model):
    item = models.CharField(max_length=5, unique=True)
    persona = models.OneToOneField(Persona, on_delete=models.PROTECT)

    def __str__(self):
        return f"Bibliotecario: {self.persona.apellidos} {self.persona.nombres}"