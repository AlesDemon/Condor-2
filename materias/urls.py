from .views import carrerasAdd, materias, materiasAdd, materias_carrera, syllabusFile, carreras
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'materias/add', materiasAdd, basename="materiasAdd")
router.register(r'carreras/add', carrerasAdd, basename="carrerasAdd")
urlpatterns = [
    path('',include(router.urls)),
    path('materias/', materias.as_view()),
    path('carreras/', carreras.as_view()),
    path('syllabus/', syllabusFile.as_view()),
    path('carrera/', materias_carrera.as_view())
]