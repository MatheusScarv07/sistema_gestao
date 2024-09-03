from sale.views import home
from django.urls import path

urlpatterns = [
    path('sales/', home )
]