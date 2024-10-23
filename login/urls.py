
from .views import page_login
from django.urls import path

urlpatterns = [
    path('login/', page_login ),

    
]