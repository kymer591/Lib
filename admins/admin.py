from django.contrib import admin
from .models import Persona, User, Lector, Autor, Bibliotecario

# Register your models here.

admin.site.register([
    Persona,
    User,
    Lector,
    Autor,
    Bibliotecario,
])
