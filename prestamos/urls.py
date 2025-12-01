from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_prestamo'),
    path('nuevoprestamo', views.prestamos, name='nuevo_prestamo'),
]