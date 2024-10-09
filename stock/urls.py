from stock.views import home, cadastrar_produto, product, editar_produto
from django.urls import path

urlpatterns = [
    path('stock/', home, name='home'),
    path('stock/product/', product, name='product'),
    path('stock/new_product/', cadastrar_produto, name='new_product'),
    path('stock/edit_product/<int:id>/', editar_produto, name='editar_produto')
]
