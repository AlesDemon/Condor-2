from django.db import models

# Create your models here.

class carrera(models.Model):

    codigo = models.CharField(primary_key=True, max_length=3)
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField()

class materia(models.Model):

    codigo = models.CharField(primary_key=True, max_length=3)
    carrera = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField()
    horas_au = models.IntegerField()
    horas_cl = models.IntegerField()

class materiaFile(models.Model):

    carrera = models.CharField(max_length=3)
    materia = models.CharField(max_length=3)

class materiascarreraModel(models.Model):

    carrera = models.CharField(max_length=3)