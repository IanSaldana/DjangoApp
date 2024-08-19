from rest_framework import viewsets
from .models import (
    Especie, Raza, Color, Region, Ciudad, Comuna, 
    TipoEstado, TipoUsuario, TipoPlan, Plan, Usuario, 
    Mascota, Interesado, ListaInteresados, Estado
)
from .serializers import (
    EspecieSerializer, RazaSerializer, ColorSerializer, RegionSerializer, CiudadSerializer, ComunaSerializer,
    TipoEstadoSerializer, TipoUsuarioSerializer, TipoPlanSerializer, PlanSerializer, UsuarioSerializer,
    MascotaSerializer, InteresadoSerializer, ListaInteresadosSerializer,
    EstadoSerializer
)

class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer

class RazaViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class TipoEstadoViewSet(viewsets.ModelViewSet):
    queryset = TipoEstado.objects.all()
    serializer_class = TipoEstadoSerializer

class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer

class TipoPlanViewSet(viewsets.ModelViewSet):
    queryset = TipoPlan.objects.all()
    serializer_class = TipoPlanSerializer

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class InteresadoViewSet(viewsets.ModelViewSet):
    queryset = Interesado.objects.all()
    serializer_class = InteresadoSerializer

class ListaInteresadosViewSet(viewsets.ModelViewSet):
    queryset = ListaInteresados.objects.all()
    serializer_class = ListaInteresadosSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
