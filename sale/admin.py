from django.contrib import admin
from .models import Sale
# Register your models here.
class SaleAdmin(admin.ModelAdmin):
    ...

admin.site.register(Sale, SaleAdmin)