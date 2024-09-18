from django.contrib import admin
from .models import Sale, CartTemp, SaleInfo

# Verificar se Sale já está registrado antes de registrar
if not admin.site.is_registered(Sale):
    class SaleAdmin(admin.ModelAdmin):
        # Defina as configurações do SaleAdmin aqui
        pass

    admin.site.register(Sale, SaleAdmin)

# Verificar se CartTemp já está registrado antes de registrar
if not admin.site.is_registered(CartTemp):
    class CartTempAdmin(admin.ModelAdmin):
        # Defina as configurações do CartTempAdmin aqui
        pass

    admin.site.register(CartTemp, CartTempAdmin)

if not admin.site.is_registered(SaleInfo):
    class SaleInfoAdmin(admin.ModelAdmin):
        # Defina as configurações do SaleInfoAdmin aqui
        pass

    admin.site.register(SaleInfo, SaleInfoAdmin)