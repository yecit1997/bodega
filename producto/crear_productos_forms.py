from django import forms
from .models import Productos


class ProductosForms(forms.ModelForm):
    class Meta:
        model = Productos
        # fields = '__all__'
        fields = ['tipo', 'ubicacion_estanteria', 'nombre', 'cantidad', 'descripcion'] 
        
        
        