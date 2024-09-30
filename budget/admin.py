from django.contrib import admin
from .models import Budget, CartTempBudget


# Register your models here.
class BudgetAdmin(admin.ModelAdmin):
    ...

admin.site.register(Budget, BudgetAdmin)

class CartTempBudgetAdmin(admin.ModelAdmin):
    ...

admin.site.register(CartTempBudget, CartTempBudgetAdmin)