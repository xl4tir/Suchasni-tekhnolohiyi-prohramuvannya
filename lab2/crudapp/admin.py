from django.contrib import admin
from .models import Orders

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('oid', 'fname', 'lname', 'price', 'mail', 'addr')
    search_fields = ('fname', 'lname', 'mail')
    list_filter = ('price',)
    ordering = ('oid',)
