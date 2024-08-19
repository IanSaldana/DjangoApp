from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Especie(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Especies"


class Raza(models.Model):
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, related_name="razas")
    nombre = models.CharField(max_length=255, verbose_name="Nombre raza")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Razas"


class Color(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Colores"


class Region(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Regiones"


class Ciudad(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="ciudades")
    nombre = models.CharField(max_length=50, verbose_name="Nombre Ciudad")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Ciudades"


class Comuna(models.Model):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name="comunas")
    nombre = models.CharField(max_length=50, verbose_name="Nombre Comuna")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Comunas"


class TipoEstado(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Estado"


class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Usuario"


class TipoPlan(models.Model):
    nombre = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Plan"


class Plan(models.Model):
    tipo_plan = models.ForeignKey(TipoPlan, on_delete=models.CASCADE, null=True, related_name="planes")
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Planes"


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil_tesis")
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, related_name="usuarios")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True, related_name="usuarios")
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name="usuarios")
    foto_perfil = models.ImageField(upload_to='profile_pics/')  
    descripcion_perfil = models.TextField()
    preferencias_mascotas = models.TextField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Usuarios"


class Mascota(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mascotas")
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE, related_name="mascotas")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name="mascotas")
    nombre = models.CharField(max_length=255)
    edad = models.PositiveIntegerField()
    descripcion = models.TextField()
    vacunado = models.BooleanField(default=False)  # Campo para indicar si la mascota está vacunada
    foto = models.ImageField(upload_to='fotos_mascotas/', null=True, blank=True)  # Campo opcional para una foto
    video = models.FileField(upload_to='videos_mascotas/', null=True, blank=True)  # Campo opcional para un video

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Mascotas"


class Interesado(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Interesados"


class ListaInteresados(models.Model):
    interesado = models.ForeignKey(Interesado, on_delete=models.CASCADE, related_name="listas")
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="listas_de_interes")
    fecha_interes = models.DateField()
    hora_interes = models.TimeField()

    def __str__(self):
        return f"Interesado: {self.interesado.nombre}, Mascota: {self.mascota.nombre}"

    class Meta:
        verbose_name_plural = "Listas de Interesados"


class Estado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="estados")
    tipo_estado = models.ForeignKey(TipoEstado, on_delete=models.CASCADE, related_name="estados")
    interesado = models.ForeignKey(Interesado, on_delete=models.CASCADE, related_name="estados")
    descripcion = models.TextField()

    def __str__(self):
        return f"Estado de {self.usuario.user.username} para {self.interesado.nombre}"

    class Meta:
        verbose_name_plural = "Estados"