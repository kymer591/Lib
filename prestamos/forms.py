from django import forms
from datetime import datetime, timedelta
from admins.models import Lector, Bibliotecario
from libros.models import Libro

FERIADOS = [
    (1, 1),   # Año Nuevo
    (1, 22),  # Día del Estado Plurinacional
    (2, 12),  # Carnaval 
    (2, 13),  # Carnaval 
    (3, 23),  # Día del Mar
    (4, 18),  # Viernes Santo
    (5, 1),   # Día del Trabajo
    (6, 21),  # Año Nuevo Aymara
    (8, 6),   # Día de la Patria
    (11, 2),  # Día de Todos los Santos
    (12, 25), # Navidad
]

def es_dia_habil(fecha):
    if fecha.weekday() >= 5:
        return False
    
    if (fecha.month, fecha.day) in FERIADOS:
        return False
    
    return True

class NewPrestamoForm(forms.Form):
    fechaPrestamo = forms.DateField(
        label='Fecha de Préstamo',
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=datetime.now().strftime('%Y-%m-%d')
    )
    fechaDevolucion = forms.DateField(
        label='Fecha de devolución',
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial= (timedelta(days=1) + datetime.now()).strftime('%Y-%m-%d')
    )
    estadoLibro = forms.ChoiceField(
        choices=[('bueno', 'Bueno'), ('regular', 'Regular'), ('malo', 'Malo')],
        label='Estado del libro',
        initial='regular',
        widget=forms.RadioSelect,
    )
    lector = forms.ChoiceField(
        choices= [('', 'Elija una opción')] + [(l.id, l.persona) for l in Lector.objects.all()],
        widget=forms.Select,
        required=False,
    )
    libro = forms.ChoiceField(
        choices= [('', 'Elija una opción')] + [(lib.id, lib.titulo) for lib in Libro.objects.all()],
        widget=forms.Select,
        required=False,
    )

    def clean_fechaPrestamo(self):
        fechaPrestamo = self.cleaned_data['fechaPrestamo']
        if fechaPrestamo < datetime.now().date():
            self.add_error('fechaPrestamo', "La fecha de préstamo no puede ser en el pasado")
        
        if not es_dia_habil(fechaPrestamo):
            if fechaPrestamo.weekday() >= 5:
                self.add_error('fechaPrestamo', "No se pueden registrar préstamos los fines de semana")
            else:
                self.add_error('fechaPrestamo', "No se pueden registrar préstamos en días feriados")
        
        return fechaPrestamo

    def clean_fechaDevolucion(self):
        fechaPrestamo = self.cleaned_data.get('fechaPrestamo')
        fechaDevolucion = self.cleaned_data['fechaDevolucion']
        print(fechaPrestamo, fechaDevolucion)
        if fechaDevolucion <= fechaPrestamo:
            self.add_error('fechaDevolucion', "La fecha de devolución debe ser posterior a la fecha de préstamo")
        
        if not es_dia_habil(fechaDevolucion):
            if fechaDevolucion.weekday() >= 5:
                self.add_error('fechaDevolucion', "No se pueden registrar devoluciones los fines de semana")
            else:
                self.add_error('fechaDevolucion', "No se pueden registrar devoluciones en días feriados")
        
        return fechaDevolucion

    def clean_lector(self):
        lector = self.cleaned_data['lector']
        if lector == '':
            self.add_error('lector', "Debe seleccionar un lector")
        return lector