from django.contrib import admin
from .models import NFE
# Register your models here.
class NFEAdmin(admin.ModelAdmin):
    ...

admin.site.register(NFE, NFEAdmin)