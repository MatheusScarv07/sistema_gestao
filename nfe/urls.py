
from nfe.views import home, new_NFE,get_product, cart, excluir_produto, efetuar_entrada, search_nfes, info_nfe
from django.urls import path

urlpatterns = [
    path('nfe/', home ),
    path('nfe/new-nfe/', new_NFE, name='entrada_de_nota'),
    path('nfe/get_product/<int:product_id>/', get_product, name='get_product'),
    path('nfe/salvar-carrinho/', cart),
    path('nfe/excluir_produto/<int:id>/', excluir_produto, name='excluir_produto'),
    path('nfe/new_nfe/concluido/', efetuar_entrada, name='entrada_efetuada'),
    path('nfe/searchnfe/',search_nfes, name='search_nfes' ),
    path('nfe/info/<int:numero_nota>/', info_nfe )

    
]