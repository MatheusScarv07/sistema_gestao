from django.urls import path
from .views import home, page_register, register, details_client,listar_fornecedores

urlpatterns = [
    path('supplier/', home),
    path('supplier/register/', page_register),
    path('supplier/register_new', register ),
    path('supplier/supplier/details_supplier/<int:id>', details_client),
    path('fornecedores/', listar_fornecedores, name='listar_fornecedores')
]