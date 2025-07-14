# gestion/admin.py
from django.contrib import admin
from .models import Dueno, Mascota, Cita, Tratamiento

@admin.register(Dueno)
class DuenoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'direccion', 'dni')
    search_fields = ('nombre', 'correo', 'dni')


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'edad', 'sexo', 'fecha_nacimiento', 'peso', 'dueno')
    list_filter = ('especie', 'sexo')
    search_fields = ('nombre', 'raza')


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'fecha', 'motivo', 'veterinario', 'estado')
    list_filter = ('estado', 'fecha')


@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'descripcion', 'costo', 'fecha_inicio', 'fecha_fin', 'observaciones')
    search_fields = ('mascota__nombre', 'descripcion')