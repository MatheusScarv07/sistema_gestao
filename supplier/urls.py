from django.urls import path
from .views import home, page_register, get_dados, register

urlpatterns = [
    path('supplier/', home),
    path('supplier/register/', page_register),
    path('supplier/get_dados/<str:cnpj>/', get_dados, name='get_endereco'),
    path('supplier/register_new', register ),
]