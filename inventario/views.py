from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from producto.models import Productos, Estanteria, Tipo
from django.db.models import Count


@login_required()
def inventario(request):
    total_productos = Productos.objects.count()
    total_productos_estanteria = Estanteria.objects.annotate(total_productos=Count('productos'))
    total_productos_tipo = Tipo.objects.annotate(total_productos=Count('productos'))
    # total_tipo_estante = 
    context = {
       'total_productos':total_productos,
       'total_productos_estanteria':total_productos_estanteria,
       'total_productos_tipo':total_productos_tipo
    }
    return render(request, 'inventario/inventario.html', context=context)
    
