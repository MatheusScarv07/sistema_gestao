from django.urls import path
from .views import home, receive_page, makePayment, search_receive, clientes_pendentes, receber_pagamento

urlpatterns = [
    path('receive/', home),
    path('receive/searchreceive', search_receive, name="search_receive"),
    path('receive/<num_venda>', receive_page, name="receive_page"),
    path('recieve/payment', makePayment, name="make_payment"),
    # URL para exibir os clientes com pagamento pendente
    path('receive/clientes-pendentes/', clientes_pendentes, name='clientes_pendentes'),

    # URL para exibir a página de recebimento de pagamento de um cliente específico
    path('receber-pagamento/<int:receive_id>/', receber_pagamento, name='receber_pagamento'),
]