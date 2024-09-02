from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.core.exceptions import ValidationError
from .models import Productos, Tipo, Estanteria
from .crear_productos_forms import ProductosForms

@login_required()
def registrar_producto(request):
    if request.method == 'POST':
        crear_productos_forms = ProductosForms(request.POST, request.FILES)
        if crear_productos_forms.is_valid():
            try:
                crear_productos_forms.save()
                messages.success(request, ("Producto registrado con éxito"))
                return redirect("productos")
            except ValidationError as e:
                messages.error(request, str(e))
        else:
            messages.error(request, ("El producto no se pudo registrar"))
    else:
        crear_productos_forms = ProductosForms()
    context = {
        'crear_productos_forms': crear_productos_forms
    }
    return render(request, 'productos/registrar_producto.html', context=context)


@login_required()
def productos(request):
    productos = Productos.objects.all()
    context = {"productos": productos}
    return render(request, "productos/productos.html", context=context)


@login_required()
def lista_tipos(request, nombre_tipo):
    try:
        tipo: str = get_object_or_404(Tipo, tipo=nombre_tipo)
        productos = Productos.objects.filter(tipo=tipo)

        if not productos.exists():
            messages.info(request, "No se encontraron productos para este tipo.")
            return redirect("productos")

        context = {"tipo": tipo, "productos": productos}
        return render(request, "productos/tipos.html", context=context)
    except:
        messages.success(request, ("El tipo no existe"))
        return redirect("productos")


@login_required()
def estantes(request):
    estantes = Estanteria.objects.all()
    context = {'estantes':estantes}
    return render(request, 'estantes/estantes.html', context=context)


@login_required()
def ver_contenido_de_estantes(request, id):
    try:
        estante = get_object_or_404(Estanteria, id=id)
        productos = Productos.objects.filter(ubicacion_estanteria=estante)
        
        try: 
            if not productos.exists():
                    messages.info(request, f"No se encontraron productos en el estante. {estante}")
                    return redirect("estantes")
        except Exception as e:
            print('ERROR: ',e)
            
        context = {'estante':estante, 'productos':productos}
        return render(request, 'estantes/ver_contenido_de_estantes.html', context=context)
    except Exception as e:
        print('ERROR: ',e)
        messages.success(request, ("Código de estante no existe"))
        return redirect("estantes")


def detalle(request, id):
    producto = get_object_or_404(Productos, pk=id)
    context = {'producto':producto}
    return render(request, 'productos/detalle.html', context=context)


def editar(request, id):
    producto = get_object_or_404(Productos, pk=id)

    if request.method == 'POST':
        form_edit = ProductosForms(request.POST, request.FILES, instance=producto)
        if form_edit.is_valid():
            try:
                form_edit.save()
                messages.success(request, ("Producto editado con éxito"))
                return redirect("productos")
            except ValidationError as e:
                messages.error(request, str(e))
    else:
        form_edit = ProductosForms(instance=producto)

    context = {
        'form_edit': form_edit
    }
    return render(request, 'productos/editar.html', context=context)



def eliminar(request, id):
    producto = get_object_or_404(Productos, pk=id)
    producto.delete()
    messages.success(request, 'Producto eliminado')
    print('Respuesta -> ',id)
    return redirect("productos")

