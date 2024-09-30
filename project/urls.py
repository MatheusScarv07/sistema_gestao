
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('client.urls')),
    path('', include('main.urls')),
    path('', include('stock.urls')),
    path('', include('budget.urls')),
    path('', include('sale.urls')),
    path('', include('nfe.urls'))
    
]
