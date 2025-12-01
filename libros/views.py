from django.shortcuts import render, redirect, HttpResponse
from .models import Libro
from .forms import NewBookForm

# Create your views here.

def index(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def nuevo_libro(request):
    if request.method == 'GET':
        form = NewBookForm()
    else:
        form = NewBookForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            libro = Libro.objects.create(
                titulo=datos['titulo'],
                editorial=datos['editorial'],
                volumen=datos['volumen'],
                paginas=datos['paginas'],
                edicion=datos['edicion'],
            )
            libro.autores.set(datos['autor'])
            return redirect('index_libro')
    return render(request, 'libros/nuevo.html', {'form': form})
