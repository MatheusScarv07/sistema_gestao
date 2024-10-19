
from sale.views import home, new_sale, searchsales, get_product, cart, cart_products, excluir_produto,enviar_orcamento, efetuar_venda, search_sale_by_number, search_sales_filter
from django.urls import path

urlpatterns = [
    path('sales/', home ),
    path('sale/new-sale', new_sale, name='new_sale'),
    path('sales/searchsales', searchsales ),
    path('sales/get_product/<int:product_id>/', get_product, name='get_product'),
    path('sale/salvar-carrinho/', cart),
    path('sales/cart_products', cart_products),
    path('sale/excluir_produto/<int:id>/', excluir_produto, name='excluir_produto'),
    path('sale/salvar-carrinho/sale/new_sale/concluido/', efetuar_venda),
    path('sale/salvar-carrinho/enviar_orcamento',enviar_orcamento),
    path('sale/info/<int:num_venda>', search_sale_by_number),
    path('sale/filtrar_vendas/',search_sales_filter )
]