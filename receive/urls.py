from django.urls import path
from client.views import home, details_client, register

urlpatterns = [
    path('receive/', home)
    
]