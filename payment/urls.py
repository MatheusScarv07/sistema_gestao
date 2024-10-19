from django.urls import path
from payment.views import home, search_payment,new_payment

urlpatterns = [
    path('payment/', home, name='home_payment'),  # Adiciona um nome à URL
    path('new_payment/', new_payment, name='new_payment'),
    path('search_payment/', search_payment, name='search_payment'),  # Adiciona um nome à URL
]