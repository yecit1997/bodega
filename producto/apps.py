from django.apps import AppConfig
# from producto.signals import actualizar_capacidad #Nombre de la funcion


class ProductoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'producto'
    
    # def ready(self):
    #     import producto.signals 
    
    
