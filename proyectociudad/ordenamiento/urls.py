from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_parroquias, name='listar_parroquias'),
    path('crear_parroquia/', views.crear_parroquia, name='crear_parroquia'),
    path('editar_parroquia/<int:id>', views.editar_parroquia, name='editar_parroquia'),
]
