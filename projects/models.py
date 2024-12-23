from django.db import models

# Create your models here.
class Riego(models.Model):
    frecuencia = models.TextField()

    def __str__(self):
        return self.frecuencia


class Ambientes(models.Model):
    ambiente = models.CharField(max_length=255)

    def __str__(self):
        return self.ambiente


class Macetas(models.Model):
    maceta = models.CharField(max_length=255)
    tamanio = models.IntegerField()

    def __str__(self):
        return self.maceta


class Plantas(models.Model):
    nombre = models.CharField(max_length=100)
    cuidados_esp = models.TextField(null=True, blank=True)
    riego = models.ForeignKey(Riego, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambientes, on_delete=models.CASCADE)
    maceta = models.ForeignKey(Macetas, on_delete=models.CASCADE)
    imagen = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre