from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError


from . models import Usuario
from .forms_user import UserForms, EditUserForms, EditPerfilUserForms

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


def admin_user(request):
    usuarios = Usuario.objects.all()
    return render(request, 'registration/user.html',{'usuarios':usuarios})


def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        form_edit = EditUserForms(request.POST, request.FILES, instance=usuario)
        if form_edit.is_valid():
            try:
                form_edit.save()
                messages.success(request, "Usuario editado con éxito")
                return redirect("admin_user")
            except ValidationError as e:
                messages.error(request, str(e))
    else:
        # No incluye el campo de contraseña en el formulario
        form_edit = EditUserForms(instance=usuario)

    context = {
        'form_edit': form_edit
    }
    return render(request, 'registration/editar.html', context=context)


def editar_perfil(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        form_edit = EditPerfilUserForms(request.POST, request.FILES, instance=usuario)
        if form_edit.is_valid():
            # Excluye el campo de contraseña para evitar su modificación accidental
            # form_edit.fields.pop('password', None)  # Elimina el campo 'password'
            try:
                form_edit.save()
                messages.success(request, "Usuario editado con éxito")
                return redirect("admin_user")
            except ValidationError as e:
                messages.error(request, str(e))
    else:
        # No incluye el campo de contraseña en el formulario
        form_edit = EditPerfilUserForms(instance=usuario)

    context = {
        'form_edit': form_edit,
        'usuario':usuario
    }
    # print(usuario.id)
    return render(request, 'registration/editar_perfil.html', context=context)









