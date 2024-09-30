from django.contrib import admin
from .models import NFE, NFECartTemp, NFEInfo
# Register your models here.
class NFEAdmin(admin.ModelAdmin):
    ...

admin.site.register(NFE, NFEAdmin)


class NFECartTempAdmin(admin.ModelAdmin):
    ...

admin.site.register(NFECartTemp, NFECartTempAdmin)

class NFEInfoAdmin(admin.ModelAdmin):
    ...

admin.site.register(NFEInfo, NFEInfoAdmin)