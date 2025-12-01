from django.shortcuts import render, HttpResponse, redirect
from .models import Persona, User
from .forms import EditPersonaForm

# Create your views here.

def index(request):
    personas = Persona.objects.all()
    #return HttpResponse(personas)
    return render(request, 'personas/index.html', {'nombre': 'Rodrigo', 'edad': 58, 'personas': personas})

def saludo(request, edad, nombre):
    return HttpResponse("Hola " + nombre + " tienes " + str(edad) + " años")

def nueva_persona(request):
    if request.method == 'GET':
        return render(request, 'personas/nueva.html')
    else:
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        ci = request.POST['ci']
        fechaNacimiento = request.POST['fechaNacimiento']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        
        persona = Persona.objects.create(
            nombres = nombres,
            apellidos = apellidos,
            ci = ci,
            fechaNacimiento = fechaNacimiento,
            direccion = direccion,
            telefono = telefono,
            user = user
        )

        return redirect('admin_index')

def detalle(request, id):
    persona = Persona.objects.get(pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})

def editar_persona(request, id):
    # Edicion de persona
    persona = Persona.objects.get(pk=id)
    datos = {'direccion': persona.direccion, 'telefono': persona.telefono, 'email': persona.user.email}
    if request.method == 'GET':
        form = EditPersonaForm(initial=datos)
        return render(request, 'personas/editar.html', { 'persona': persona, 'form': form })
    else:
        persona.telefono = request.POST["telefono"]
        persona.direccion = request.POST["direccion"]
        persona.save();
        user = User.objects.get(pk=persona.user.id)
        user.email = request.POST["email"]
        user.save()
        return redirect('detalle_persona', id)
    
def inicio(request):
    return render(request, 'inicio.html')  