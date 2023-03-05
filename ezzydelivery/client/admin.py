from django.contrib import admin
from client import models as business_models

# Register your models here.


@admin.register(business_models.Business)
class businessAdmin(admin.ModelAdmin):
    list_display = ( 'business_business_name', 'business_phone', 'business_whatsapp',
                    'brand_name', 'brand_since', 'brand_product_category', 'business_code', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    list_per_page = 10


@admin.register(business_models.PickupLocation)
class PickupLocationAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'pickup_location_title', 'pickup_zone_no', 'pickup_street_no',
                    'pickup_building_no')


@admin.register(business_models.RegularDriverContacts)
class RegularDriverContactsAdmin(admin.ModelAdmin):
   
    list_per_page = 10
