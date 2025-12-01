from django.contrib import admin
from .models import Prestamo, Devolucion

# Register your models here.

admin.site.register([
    Prestamo,
    Devolucion,
])
