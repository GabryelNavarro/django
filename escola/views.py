from rest_framework import viewsets,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse
from escola.models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer,ListaMatriculaAlunoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


    
class MatriculasViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class ListaMatriculaAluno(generics.ListAPIView):
    serializer_class = ListaMatriculaAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Matricula.objects.none()
        return Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    




class CustomApiRootView(APIView):
    
    def get(self, request, format=None):
        return Response({
            'alunos': request.build_absolute_uri(reverse('Alunos-list')),
            'cursos': request.build_absolute_uri(reverse('Cursos-list')),
            'matricula': request.build_absolute_uri(reverse('Matrículas-list')),
            'swagger': request.build_absolute_uri(reverse('schema-swagger-ui')),
        })


class ListaMatriculaAlunoView(generics.ListAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaAlunoSerializer