from django.urls import path
from client.views import home, details_client, register, get_endereco, cadastrar

urlpatterns = [
    path('client/', home),
    path('client/<int:id>', details_client),
    path("client/register", register),
    path('client/get_endereco/<cep>/', get_endereco, name='get_endereco'),
    path('client/client/new/cadastro', cadastrar  )
]