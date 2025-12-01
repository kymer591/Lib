from django.shortcuts import render, redirect
from .models import Prestamo, Devolucion
from .forms import NewPrestamoForm

# Create your views here.

def index(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamos/index.html', {'prestamos': prestamos})

def prestamos(request):
    if request.method == 'GET':
        form = NewPrestamoForm()
    else:
        form = NewPrestamoForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            prestamo = Prestamo.objects.create(
                fechaPrestamo=datos['fechaPrestamo'],
                fechaDevolucion=datos['fechaDevolucion'],
                estadoLibro=datos['estadoLibro'],
                lector_id=datos['lector'],
                libro_id=datos['libro'],
                bibliotecario_id=1,  # Asignar un bibliotecario fijo por ahora
            )
            return redirect('index_prestamo')

    return render(request, 'prestamos/nuevo.html', {'form': form})