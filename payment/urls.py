from django.urls import path
from payment.views import home

urlpatterns = [
    path('payment/', home)
    
]