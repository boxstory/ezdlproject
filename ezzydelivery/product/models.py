from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from client import models as business_models
from product import models as product_models
# Create your models here.


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100)
    sub_category = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)
    discription = models.CharField(max_length=100)
    product_category_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Product Category"


class ColorVariant(models.Model):
    color_variant = models.CharField(max_length=100)
    short_code = models.CharField(max_length=5, null=True, blank=True)
    discription = models.CharField(max_length=100)
    color_variants_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.color_variant

    class Meta:
        verbose_name_plural = "Color Variants"


class SizeVariant(models.Model):
    size_variant = models.CharField(max_length=100)
    short_code = models.CharField(max_length=5, null=True, blank=True)
    discription = models.CharField(max_length=100)
    size_variants_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.size_variant

    class Meta:
        verbose_name_plural = "Size Variants"


class UnitVariant(models.Model):
    unit_variant = models.CharField(max_length=100)
    short_code = models.CharField(max_length=5, null=True, blank=True)
    discription = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.uni_variant

    class Meta:
        verbose_name_plural = "Uni Variants"


class ItemSku(models.Model):
    item_sku = models.CharField(max_length=100)
    color = models.ForeignKey(
        ColorVariant, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.ForeignKey(
        SizeVariant, on_delete=models.SET_NULL, null=True, blank=True)
    unit = models.ForeignKey(
        UnitVariant, on_delete=models.SET_NULL, null=True, blank=True)
    item_price = models.PositiveIntegerField(_("Price"), default=0)
    created_at = models.DateField(auto_now_add=True)

    business = models.ForeignKey(
        business_models.Business, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.item_sku

    class Meta:
        verbose_name_plural = "Item SKU"


class ProductInventory(models.Model):
    item_sku = models.ForeignKey(
        product_models.ItemSku, on_delete=models.SET_NULL, null=True, related_name='product_inventory')
    item_quantity = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_sku

    class Meta:
        verbose_name_plural = "Product Inventory"


class Product(models.Model):
    item_name = models.CharField(max_length=100)
    item_sku = models.ForeignKey(
        ItemSku, on_delete=models.SET_NULL, null=True)
    business = models.ForeignKey(
        business_models.Business, on_delete=models.SET_NULL, null=True, related_name='product')
    product_category = models.ForeignKey(
        product_models.ProductCategory, on_delete=models.SET_NULL, null=True)
    inventory = models.ForeignKey(
        product_models.ProductInventory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name_plural = "Items"
