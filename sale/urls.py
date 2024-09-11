from sale.views import home, new_sale, searchsales, get_product, cart, cart_products
from django.urls import path

urlpatterns = [
    path('sales/', home ),
    path('sale/new-sale', new_sale),
    path('sales/searchsales', searchsales ),
    path('sales/get_product/<int:product_id>/', get_product, name='get_product'),
    path('sale/salvar-carrinho', cart),
    path('sales/cart_products', cart_products)
]