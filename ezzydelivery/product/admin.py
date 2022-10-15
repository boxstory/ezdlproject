from django.contrib import admin
from product import models as product_models

# Register your models here.


@admin.register(product_models.ItemSku)
class Item_skuAdmin(admin.ModelAdmin):
    list_display = ('item_sku', 'color', 'size', 'unit', 'item_price')


@admin.register(product_models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_sku', 'client',
                    'product_category', 'inventory')


@admin.register(product_models.ProductInventory)
class Product_inventoryAdmin(admin.ModelAdmin):
    list_display = ('item_sku', 'item_quantity','created_at',  'updated_at')


@admin.register(product_models.ProductCategory)
class Product_categoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'sub_category', 'discription')


@admin.register(product_models.ColorVariant)
class Color_variantAdmin(admin.ModelAdmin):
    list_display = ('color_variant', 'short_code', 'discription')


@admin.register(product_models.SizeVariant)
class Size_variantAdmin(admin.ModelAdmin):
    list_display = ('size_variant', 'short_code', 'discription')


@admin.register(product_models.UnitVariant)
class Unit_variantAdmin(admin.ModelAdmin):
    list_display = ('unit_variant', 'short_code', 'discription')
