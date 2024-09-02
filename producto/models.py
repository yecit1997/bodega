from django.db import models
from django.utils import timezone
from django.db import transaction
from django.core.exceptions import ValidationError



# Create your models here.


TIPOS = [
    ("Llantas y Rines", "Llantas y Rines"),
    ("Guayas y Kit de arrastre", "Guayas y Kit de arrastre"),
    ("Luces y Estacionarias", "Luces y Estacionarias"),
    ("Bocinas", "Bocinas"),
    ("Motores", "Motores"),
    ("Cojines", "Cojines"),
    ("Espejos", "Espejos"),
]
class Tipo(models.Model):
    tipo = models.CharField(max_length=100, unique=True, choices=TIPOS)
    limite = models.IntegerField(editable=False, default=600)
    activo = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ["tipo"]

    def __str__(self) -> str:
        return self.tipo


CODIGOS = [
    ("A1", "A1"),
    ("A2", "A2"),
    ("A3", "A3"),
    ("A4", "A4"),
    ("A5", "A5"),
    ("A6", "A6"),
    ("A7", "A7"),
    ("A8", "A8"),
]
class Estanteria(models.Model):
    codigo = models.CharField(max_length=20, unique=True, choices=CODIGOS)
    capacidad = models.IntegerField()
    llena = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Estanteria"
        verbose_name_plural = "Estanterias"
        ordering = ["codigo"]

    def __str__(self) -> str:
        return self.codigo
    
    # Con este metodo reducimos la capacidad de la Estanteria, en base a la cantidad de productos
    def reducir_capacidad(self, cantidad):
        if self.capacidad < cantidad:
            raise ValidationError("No hay suficiente capacidad en la estantería para agregar el producto.")
        self.capacidad -= cantidad
        self.save()  # Guardar el cambio en la base de datos
        
    def aumentar_capacidad(self, cantidad):
        self.capacidad += cantidad
        self.save()
    
    
class Productos(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    ubicacion_estanteria = models.ForeignKey(Estanteria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    # imagen = models.ImageField(upload_to='producto/')
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    agotado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-fecha_creacion"]

    def __str__(self) -> str:
        return f"{self.tipo} -> {self.nombre}"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            # Verifica si el producto ya existe
            if self.pk is not None:
                # Si el producto ya existe, obtén el objeto original
                producto_original = Productos.objects.get(pk=self.pk)
                # Si la ubicación de la estantería ha cambiado, actualiza la capacidad
                if producto_original.ubicacion_estanteria != self.ubicacion_estanteria:
                    # Aumenta la capacidad de la estantería original
                    producto_original.ubicacion_estanteria.capacidad += producto_original.cantidad
                    producto_original.ubicacion_estanteria.save()
                    # Reduce la capacidad de la nueva estantería
                    self.ubicacion_estanteria.reducir_capacidad(self.cantidad)
            else:
                # Si es un nuevo producto, reduce la capacidad de la estantería
                self.ubicacion_estanteria.reducir_capacidad(self.cantidad)

            # Llamar al método save del padre (guardar el producto)
            super().save(*args, **kwargs)
                       
    def delete(self, *args, **kwargs):
        # Aumentar la capacidad de la estantería antes de eliminar el producto
        self.ubicacion_estanteria.aumentar_capacidad(self.cantidad)
        # Llamar al método delete del padre (eliminar el producto)
        super().delete(*args, **kwargs)



