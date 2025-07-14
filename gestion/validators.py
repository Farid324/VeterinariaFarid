# gestion/validators.py
from django.core.exceptions import ValidationError

def validar_nombre_sin_numeros(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números.')

def validar_edad_positiva(value):
    if value < 0:
        raise ValidationError('La edad no puede ser negativa.')