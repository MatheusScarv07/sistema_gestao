from django.urls import path
from client.views import home, details_client, register, get_endereco, cadastrar,delete_client, edit_client

urlpatterns = [
    path('client/', home, name='consultar_cliente'),
    path('client/<int:id>', details_client),
    path("client/register", register),
    path('client/get_endereco/<cep>/', get_endereco, name='get_endereco'),
    path('client/new/cadastro', cadastrar, name='cadastrar'  ),
    path('client/delete/<int:id>/', delete_client, name='delete_client'),
    path('client/edit/<int:id>/', edit_client, name='edit_client'),
]