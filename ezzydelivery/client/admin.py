from django.contrib import admin
from client import models as client_models

# Register your models here.


@admin.register(client_models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ( 'client_business_name', 'client_phone', 'client_whatsapp',
                    'brand_name', 'brand_since', 'brand_product_category', 'client_code', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    list_per_page = 10


@admin.register(client_models.PickupLocation)
class PickupLocationAdmin(admin.ModelAdmin):
    list_display = ('client', 'id', 'pickup_location_title', 'pickup_zone_no', 'pickup_street_no',
                    'pickup_building_no')


@admin.register(client_models.RegularDriverContacts)
class RegularDriverContactsAdmin(admin.ModelAdmin):
    list_display = ('client', 'driver')
    list_per_page = 10
