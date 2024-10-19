from django.contrib import admin
from .models import PaymentType, PaymentHistory, Receive
# Register your models here.
class PaymentTypeAdmin(admin.ModelAdmin):
    ...
admin.site.register(PaymentType, PaymentTypeAdmin)


class ReceiveAdmin(admin.ModelAdmin):
    ...
admin.site.register(Receive, ReceiveAdmin)

class PaymentHistoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(PaymentHistory, PaymentHistoryAdmin)