from rest_framework import serializers
from .models import (
    Especie, Raza, Color, Region, Ciudad, Comuna, 
    TipoEstado, TipoUsuario, TipoPlan, Plan, Usuario, 
    Mascota, Interesado, ListaInteresados, Estado
)

class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = '__all__'

class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = '__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'

class TipoEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEstado
        fields = '__all__'

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = '__all__'

class TipoPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPlan
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    

class MascotaSerializer(serializers.ModelSerializer):
     class Meta:
        model = Mascota
        fields = ['id', 'usuario', 'raza', 'color', 'nombre', 'edad', 'descripcion', 'vacunado', 'foto', 'video']



class InteresadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interesado
        fields = '__all__'

class ListaInteresadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaInteresados
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'
