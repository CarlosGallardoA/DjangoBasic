from django.db import models

# Create your models here.

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    correo = models.EmailField(max_length=200)

    def __str__(self):
        return self.nombre