# gestion/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DuenoViewSet, MascotaViewSet, CitaViewSet, TratamientoViewSet
from .views import mascotas_de_dueno

router = DefaultRouter()
router.register(r'duenos', DuenoViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'citas', CitaViewSet)
router.register(r'tratamientos', TratamientoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('duenos/<int:dueno_id>/mascotas/', mascotas_de_dueno, name='mascotas-de-dueno'),
]