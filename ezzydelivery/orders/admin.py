from atexit import register
from django.contrib import admin
from orders import models as order_models
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(order_models.Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('order_number', 'business', 'order_notes', 'order_status')
