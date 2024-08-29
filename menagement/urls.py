
from django.urls import path
from menagement.views import home
urlpatterns = [
    path('', home)
    
]