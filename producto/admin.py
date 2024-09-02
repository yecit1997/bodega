from django.contrib import admin
from . models import Tipo, Estanteria, Productos

admin.site.register(Tipo)
admin.site.register(Estanteria)



@admin.register(Productos,)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['tipo','nombre','cantidad','descripcion','ubicacion_estanteria','fecha_creacion','agotado']
    list_filter = ['tipo','nombre','cantidad','ubicacion_estanteria','fecha_creacion']
    # search_fields = ['tipo','nombre']
    # readonly_fields = ('limite',)
    # readonly_fields = ['limite']
    

  
    
    