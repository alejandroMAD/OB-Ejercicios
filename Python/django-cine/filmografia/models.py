from django.db import models

# Create your models here.


class Director(models.Model):
    nombre = models.CharField(max_length=60, help_text='Nombre y apellidos del director')
    pais = models.CharField(max_length=30, help_text='País de origen')
    fecha_nacimiento = models.DateField()
    fecha_fallecimiento = models.DateField(null=True, blank=True)
    biografia = models.TextField()

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=60)
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    pais = models.CharField(max_length=30, help_text='País de producción')
    resumen = models.TextField(max_length='255', help_text='Sinopsis de la película')
    duracion = models.PositiveIntegerField(help_text='Duración de la película en minutos')
    agno = models.PositiveIntegerField()

    GENERO = (
        ('ACC', 'Acción'),
        ('ANI', 'Animación'),
        ('BIO', 'Biografía'),
        ('BEL', 'Bélico'),
        ('CFI', 'Ciencia Ficción'),
        ('COM', 'Comedia'),
        ('DES', 'Desastres'),
        ('DIS', 'Distopía'),
        ('DOC', 'Documental'),
        ('DRA', 'Drama'),
        ('ESP', 'Espías'),
        ('FAN', 'Fantasía'),
        ('HIS', 'Historia'),
        ('LEG', 'Legal'),
        ('MAF', 'Mafia'),
        ('MUS', 'Musical'),
        ('TER', 'Terror'),
        ('MIS', 'Misterio'),
        ('PEN', 'Penitenciario'),
        ('POL', 'Policíaco'),
        ('ROM', 'Romántico'),
        ('SUS', 'Suspense'),
        ('WES', 'Western'),
    )

    genero = models.CharField(
        max_length=3,
        choices=GENERO,
        blank=True,
        help_text='Género/s cinematográficos'
    )

    def __str__(self):
        return f'{self.titulo} ({self.director}, {self.agno})'
