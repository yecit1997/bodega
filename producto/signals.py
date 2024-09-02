# from django.dispatch import receiver
# from django.shortcuts import get_object_or_404
# from django.db.models.signals import post_save

# from .models import Estanteria, Productos
# from .capacidad import Capacidad



# @receiver(post_save, sender=Productos)
# def actualizar_capacidad(sender,instance, created, **kwargs):
#     print('elemento creado...')
#     estante = get_object_or_404(Estanteria, id=id)
#     id_estante = estante.pk
#     # estanteria = Estanteria.objects.filter(pk=id_estante)
#     productos = Productos.objects.filter(ubicacion_estanteria=estante)
#     if created:
#         capacidad = Capacidad()
#         cantidad_productos = len(productos)

#         ver = capacidad.valor_capacidad(estante=estante)
#         print('Instance total-> ',ver)

#         restar_capacidad = capacidad.restar(estante=estante, producto=cantidad_productos)
#         restar_capacidad=estante.capacidad
#         print('Instance restada -> ',restar_capacidad)
#         estanteria = Estanteria.objects.filter(pk=id_estante).update(capacidad=restar_capacidad)


#         print('Codigo -> ',id_estante)
#         print('Estanteria -> ',estanteria)
        



