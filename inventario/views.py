from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from producto.models import Productos, Estanteria, Tipo
from django.db.models import Sum


@login_required()
def inventario(request):
   total_productos_categoria = Tipo.objects.annotate(total_productos=Sum('productos__cantidad'))
   total_productos_estanteria = Estanteria.objects.annotate(total_cantidad=Sum('productos__cantidad'))   
   distribucion = {}
   for estante in Estanteria.objects.all():
       distribucion[estante.codigo] = {}
       for producto in Productos.objects.filter(ubicacion_estanteria=estante):
           tipo = producto.tipo.tipo
           if tipo not in distribucion[estante.codigo]:
               distribucion[estante.codigo][tipo] = 0
           distribucion[estante.codigo][tipo] += producto.cantidad 

 
   context = {
      'distribucion':distribucion,
      'total_productos_estanteria':total_productos_estanteria.order_by('codigo'),
      'total_productos_categoria':total_productos_categoria.order_by('tipo')
   }
   return render(request, 'inventario/inventario.html', context=context)
    
