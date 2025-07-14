# gestion/views.py
from rest_framework import viewsets
from .models import Dueno, Mascota, Cita, Tratamiento
from .serializers import DuenoSerializer, MascotaSerializer, CitaSerializer, TratamientoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class DuenoViewSet(viewsets.ModelViewSet):
    queryset = Dueno.objects.all()
    serializer_class = DuenoSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

@api_view(['GET'])
def mascotas_de_dueno(request, dueno_id):
    try:
        dueno = Dueno.objects.get(id=dueno_id)
        mascotas = Mascota.objects.filter(dueno=dueno)
        serializer = MascotaSerializer(mascotas, many=True)
        return Response({
            "dueno": dueno.nombre,
            "cantidad": mascotas.count(),
            "mascotas": serializer.data
        }, status=status.HTTP_200_OK)
    except Dueno.DoesNotExist:
        return Response({"error": "Dueño no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
