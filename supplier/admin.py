from django.contrib import admin
from .models import Supplier
# Register your models here.
class SupllierAdmin(admin.ModelAdmin):
    ...

admin.site.register(Supplier, SupllierAdmin)