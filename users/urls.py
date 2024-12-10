from django.urls import path
from .views import criar_usuario_view, listar_usuarios_view

urlpatterns = [
    path('criar-usuario/', criar_usuario_view, name='criar_usuario'),
    path('usuarios/', listar_usuarios_view, name='listar_usuarios'),
]