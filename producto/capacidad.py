
from django.core.exceptions import ValidationError


class Capacidad:
    def __init__(self, *args, **kwargs):
        pass
        # self.request = request
        # self.session = request.session
        # capacidad = self.session.get('capacidad')
        
        # if not capacidad:
        #     capacidad = self.session['capacidad'] = {}
        
        # self.capacidad = capacidad
        
        
    def guardar_cantidad(self):
        self.session["capacidad"] = self.capacidad
        self.session.modified = True
        
    
    def valor_capacidad(self, estante):
        self.capacidad = estante.capacidad
        return self.capacidad
    

    def restar(self, estante, producto):
        if estante.capacidad <= 0:
            raise ValidationError("No hay suficiente capacidad en la estantería para agregar el producto.")
        self.capacidad = estante.capacidad - producto
        return self.capacidad



