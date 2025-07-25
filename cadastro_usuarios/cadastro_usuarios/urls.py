from django.urls import path
from app_cadastro_usuarios import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # usuarios.com
    path('', views.home, name='home'),
    # usuarios.com/usuarios
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    # usuarios.com/editar
    path('editar/<uuid:id>/', views.editar_usuario, name='editar_usuario'),
    # usuarios.com/excluir
    path('excluir/<uuid:id>/', views.excluir_usuario, name='excluir_usuario'),
]
