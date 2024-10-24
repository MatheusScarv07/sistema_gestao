from django.urls import path
from .views import home, receive_page, makePayment, search_receive

urlpatterns = [
    path('receive/', home),
    path('receive/searchreceive', search_receive, name="search_receive"),
    path('receive/<num_venda>', receive_page, name="receive_page"),
    path('recieve/payment', makePayment, name="make_payment")
]