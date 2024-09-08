from django.contrib import admin
from .models import Employee
# Register your models here.
class employeeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Employee, employeeAdmin)