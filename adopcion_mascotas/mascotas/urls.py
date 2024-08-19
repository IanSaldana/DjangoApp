from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EspecieViewSet, RazaViewSet, ColorViewSet, RegionViewSet, CiudadViewSet, ComunaViewSet,
    TipoEstadoViewSet, TipoUsuarioViewSet, TipoPlanViewSet, PlanViewSet, UsuarioViewSet,
    MascotaViewSet, InteresadoViewSet, ListaInteresadosViewSet,
    EstadoViewSet
)

router = DefaultRouter()
router.register(r'especies', EspecieViewSet)
router.register(r'razas', RazaViewSet)
router.register(r'colores', ColorViewSet)
router.register(r'regiones', RegionViewSet)
router.register(r'ciudades', CiudadViewSet)
router.register(r'comunas', ComunaViewSet)
router.register(r'tipos_estado', TipoEstadoViewSet)
router.register(r'tipos_usuario', TipoUsuarioViewSet)
router.register(r'tipos_plan', TipoPlanViewSet)
router.register(r'planes', PlanViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'interesados', InteresadoViewSet)
router.register(r'listas_interesados', ListaInteresadosViewSet)
router.register(r'estados', EstadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
