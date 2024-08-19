from django.contrib import admin
from .models import (
    Especie, Raza, Color, Region, Ciudad, Comuna, 
    TipoEstado, TipoUsuario, TipoPlan, Plan, Usuario, 
    Mascota, Interesado, ListaInteresados, Estado
)

# Registrar los modelos en el admin
admin.site.register(Especie)
admin.site.register(Raza)
admin.site.register(Color)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(TipoEstado)
admin.site.register(TipoUsuario)
admin.site.register(TipoPlan)
admin.site.register(Plan)
admin.site.register(Usuario)
admin.site.register(Mascota)
admin.site.register(Interesado)
admin.site.register(ListaInteresados)
admin.site.register(Estado)