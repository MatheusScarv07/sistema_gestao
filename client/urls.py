from django.urls import path
from client.views import home, details_client, register

urlpatterns = [
    path('client/', home),
    path('client/<int:id>', details_client),
    path("client/register", register)
    
]