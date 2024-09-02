from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from . models import Usuario
from .forms_user import UserForms

# Create your views here.



def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Inicio correcto')
                return redirect('productos')
            else:
                messages.success(request, 'El usuario no esta activo')
                return redirect('login')
        else:
            messages.success(request, 'Usuario o contraseña incorrectos')
            return redirect('login')
    return render(request, 'registration/login.html')


def register_user(request):
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            user = Usuario.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['contrasena']))
            user.save()
            messages.success(request, 'Usaurio creado con exito ✅')
            return redirect('login')
        else:
            messages.error(request, 'Los datos no son correctos 😞❌')
    else:
        form = UserForms()
    context = {
        'form': form
    }
        
    return render(request, 'registration/register.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')

