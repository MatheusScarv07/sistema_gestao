
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('client.urls')),
    path('', include('main.urls')),
    path('', include('stock.urls')),
    path('', include('budget.urls')),
    path('', include('sale.urls')),
    path('', include('nfe.urls')),
    path('', include('employee.urls')),
    path('', include('receive.urls')),
    path('', include('payment.urls')),
    path('', include('supplier.urls')),
    path('', include('login.urls')),
    path('', include('users.urls'))
]
