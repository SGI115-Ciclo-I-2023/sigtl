from django.db import models
from django.contrib.postgres.fields import ArrayField

class Categoria(models.Model):
    id_categoria = models.BigAutoField(unique=True, primary_key=True, blank=False, null=False)
    nombre_categoria = models.CharField(max_length=30, blank=False, null=False)
    descripcion_categoria = models.TextField(blank=False, null=False)
    # is_active = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return '%s, %s' % (self.id_categoria, self.nombre_categoria)

class Producto(models.Model):
    id_producto = models.BigAutoField(unique=True, primary_key=True, null=False, blank=False)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    precio = models.FloatField(blank=False, null=False)
    descripcion_producto = models.TextField(blank=True, null=True)
    descuento = models.FloatField(blank=False, null=False, default=0.0)
    cantidad_disponible = models.IntegerField(
        blank=False, null=False, default=0)
    valorInv = models.FloatField(blank=False, null=False, default=0)
    # is_active = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return '%s, %s' % (self.nombre, self.descripcion_producto)

class Sucursal(models.Model):
    id_sucursal = models.BigAutoField(unique=True, primary_key=True, blank=False, null=False)
    nombre_sucursal = models.CharField(max_length=50, blank=False, null=False)
    direccion = models.TextField(blank=False, null=False)
    # is_active = models.BooleanField(null=False, blank=False, default=True)
    
    def __str__(self):
        return '%s, %s' % (self.nombre_sucursal, self.direccion)

class Movimiento(models.Model):
    ACTIVO = 'ACT'
    INACTIVO = 'NAC'
    ACTUALIZADO = 'UPD'
    ELIMINADO = 'DEL'
    ESTADOS = [
        (ACTIVO, 'Activo'),
        (INACTIVO, 'Inactivo'),
        (ACTUALIZADO, 'Actualizado'),
        (ELIMINADO, 'Eliminado'),
    ]
    id_movimiento = models.BigAutoField(unique=True, blank=False, null=False, primary_key=True)
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="movs")
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(blank=False, null=False)
    detalle = models.CharField(max_length=30, blank=False, null=False)
    valorUnitario = models.FloatField(blank=False, null=False)
    cantidad = models.IntegerField(blank=False, null=False)
    total = models.FloatField(blank=False, null=False)
    tipo = models.CharField(max_length=1, blank=False, null=False)

class ProductoDanado(models.Model):
    id_productoDanado = models.BigAutoField(unique=True, blank=False, null=False, primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_registro = models.DateField(blank=False, null=False)
    detalle = models.CharField(max_length=100, blank=False, null=False)
    cantidad = models.IntegerField(blank=False, null=False)
    
class Configuracion(models.Model):
    variable=models.TextField(primary_key=True)
    value=models.BooleanField(default=False)