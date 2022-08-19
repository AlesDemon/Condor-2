from rest_framework import serializers
from .models import materia, materiaFile, carrera, materiascarreraModel

class carreraSerializer(serializers.ModelSerializer):

    class Meta:
        model = carrera
        fields = (
            'codigo', 'nombre', 'creditos'
        )

class materiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = materia
        fields = (
            'codigo', 'carrera', 'nombre', 'creditos',  'horas_au', 'horas_cl'
        )

class materiaFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = materiaFile
        fields = (
            'carrera', 'materia'
        )

class materiascarreraSerializer(serializers.ModelSerializer):

    class Meta:
        model = materiascarreraModel
        fields = (
            "__all__"
        )