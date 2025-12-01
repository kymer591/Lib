from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Persona, User
from .forms import EditPersonaForm

# Create your views here.

def login_view(request):
    """Vista de inicio de sesión"""
    if request.user.is_authenticated:
        return redirect('inicio')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            # Configurar para que la sesión expire al cerrar el navegador
            request.session.set_expiry(0)
            return redirect('inicio')
        else:
            return render(request, 'auth/login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })
    
    return render(request, 'auth/login.html')


def logout_view(request):
    """Vista de cierre de sesión"""
    auth_logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    personas = Persona.objects.all()
    return render(request, 'personas/index.html', {
        'nombre': 'Rodrigo', 
        'edad': 58, 
        'personas': personas
    })


@login_required(login_url='login')
def saludo(request, edad, nombre):
    return HttpResponse("Hola " + nombre + " tienes " + str(edad) + " años")


@login_required(login_url='login')
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


@login_required(login_url='login')
def detalle(request, id):
    persona = Persona.objects.get(pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})


@login_required(login_url='login')
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


@login_required(login_url='login')
def inicio(request):
    return render(request, 'inicio.html')