from django.contrib import admin
from .models import Stock
# Register your models here.
class StockAdmin(admin.ModelAdmin):
    ...

admin.site.register(Stock, StockAdmin)