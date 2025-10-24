from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculaAluno,CustomApiRootView,ListaMatriculaAlunoView
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matricula', MatriculasViewSet, basename='Matrículas')
router.root_view_name = 'custom-api-root'

schema_view = get_schema_view(
    openapi.Info(
        title="Django API Escola",
        default_version="v1",
        description="Documentação da API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomApiRootView.as_view(), name='custom-api-root'),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculaAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaMatriculaAlunoView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  
]