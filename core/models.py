from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre_cat = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nombre_cat
    
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.PositiveIntegerField()
    stock = models.IntegerField()
    desc = models.CharField(max_length=400)
    imagen = models.CharField(max_length=300)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.nombre