from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_libro'),
    path('nuevolibro', views.nuevo_libro, name='nuevo_libro'),
]