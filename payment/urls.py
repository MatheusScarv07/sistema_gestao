from django.urls import path
from payment.views import home, new_payment, search_payment

app_name = 'payment'

urlpatterns = [
    path('payment/', home, name='home'),  # URL para a página inicial
    path('new-payment/', new_payment, name='new_payment'),
    path('search-payment/', search_payment, name='search_payment'),
]
