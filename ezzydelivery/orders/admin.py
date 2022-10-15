from atexit import register
from django.contrib import admin
from orders import models as order_models

# Register your models here.


@admin.register(order_models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'client', 'order_name', 'order_status')


