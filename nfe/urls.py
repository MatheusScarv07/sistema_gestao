
from nfe.views import home, new_NFE,get_product, cart, excluir_produto, efetuar_venda
from django.urls import path

urlpatterns = [
    path('nfe/', home ),
    path('nfe/new-nfe', new_NFE),
    path('nfe/get_product/<int:product_id>/', get_product, name='get_product'),
    path('nfe/salvar-carrinho/', cart),
    path('nfe/excluir_produto/<int:id>/', excluir_produto, name='excluir_produto'),
    path('nfe/salvar-carrinho/nfe/new_nfe/concluido/', efetuar_venda),

    
]