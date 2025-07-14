# gestion/models.py

from django.db import models
from django.core.exceptions import ValidationError
from .validators import validar_nombre_sin_numeros, validar_edad_positiva

class Dueno(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_nombre_sin_numeros])
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField(blank=True)
    dni = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True)
    edad = models.IntegerField(validators=[validar_edad_positiva])
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE, related_name='mascotas')
    sexo = models.CharField(max_length=10, choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')])
    fecha_nacimiento = models.DateField(null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

class Cita(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateTimeField()
    motivo = models.TextField()
    veterinario = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Atendida', 'Atendida')])

    def __str__(self):
        return f"Cita de {self.mascota.nombre} el {self.fecha.strftime('%d/%m/%Y %H:%M')}"

class Tratamiento(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='tratamientos')
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Tratamiento de {self.mascota.nombre} - ${self.costo}"