from logging import raiseExceptions
from catalogoPensum.settings import BASE_DIR
from .serializers import materiaSerializer, materiaFileSerializer, carreraSerializer, materiascarreraSerializer
from rest_framework import viewsets
from .models import materia, materiaFile, carrera, materiascarreraModel
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import os

# Create your views here.

class carrerasAdd(viewsets.ModelViewSet):
    
    serializer_class = carreraSerializer
    queryset = carrera.objects.all()

class carreras(APIView):
    def get(self, request, *args, **kwargs):
        carreras = carrera.objects.all()
        return Response(
            [{
                "codigo" : carrera.codigo,
                "nombre" : carrera.nombre,
                "creditos" : carrera.creditos
            } for carrera in carreras]
        )

class materiasAdd(viewsets.ModelViewSet):
    
    serializer_class = materiaSerializer
    queryset = materia.objects.all()

class materias(APIView):
    def get(self, request, *args, **kwargs):
        materias = materia.objects.all()
        return Response(
            [{
                "codigo" : materia.codigo,
                "carrera" : materia.carrera,
                "nombre" : materia.nombre,
                "creditos" : materia.creditos,
                "horas autonomas" : materia.horas_au,
                "horas de clase" : materia.horas_cl
            } for materia in materias]
        )

class syllabusFile(APIView):
    
    serializer_class = materiaFileSerializer
    queryset = materiaFile.objects.all()

    def get(self, request, *args, **kwargs):
        materias = materia.objects.all()
        return Response(
            [{
                "codigo" : materia.codigo,
                "carrera" : materia.carrera,
                "nombre" : materia.nombre,
                "creditos" : materia.creditos,
                "horas autonomas" : materia.horas_au,
                "horas de clase" : materia.horas_cl
            } for materia in materias]
        )

    def post(self,request,*args,**kwargs):
        
        carrera = request.data.get("carrera" , "")
        codigo = request.data.get("materia", "")

        ruta = os.path.join(BASE_DIR,"src","syllabus", carrera, carrera+codigo+".pdf")

        try:
            return FileResponse(open(ruta,"rb"))
        except:
            return raiseExceptions

class materias_carrera(APIView):

    serializer_class = materiascarreraSerializer
    queryset = materiascarreraModel.objects.all()

    def get(self,request,*args,**kwargs):
        carreras = carrera.objects.all()
        return Response(
            [{
                "codigo" : carrera.codigo,
                "nombre" : carrera.nombre,
                "creditos" : carrera.creditos
            } for carrera in carreras]
        )

    def post(self,request,*args,**kwargs):
        carrera=request.data.get("carrera", "")
        materias = materia.objects.filter(carrera=carrera)
        return Response(
            [{
                "codigo" : materia.codigo,
                "carrera" : materia.carrera,
                "nombre" : materia.nombre,
                "creditos" : materia.creditos,
                "horas autonomas" : materia.horas_au,
                "horas de clase" : materia.horas_cl
            } for materia in materias]
        )