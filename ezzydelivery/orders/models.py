from datetime import datetime
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from delivery import models as delivery_models
from core import models as core_models
from fleet import models as fleet_models
from client import models as client_models
from orders import models as orders_models


# Create your models here.

# orders---------------------------------------------------------------------------------------------------------------------


class Item_sku(models.Model):
    item_sku = models.CharField(max_length=100)
    item_attributes = models.CharField(
        max_length=100)
    item_variation = models.CharField(max_length=100)
    item_sku_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_sku_name

    class Meta:
        verbose_name_plural = "Item SKU"


class Items(models.Model):
    item_name = models.CharField(max_length=100)
    item_sku = models.ForeignKey(
        Item_sku, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(
        client_models.Client, on_delete=models.SET_NULL, null=True)
    item_quantity = models.IntegerField(default=0)
    item_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name_plural = "Items"


class Order(models.Model):
    order_number = models.CharField(max_length=100)
    client = models.ForeignKey(
        client_models.Client, on_delete=models.CASCADE)

    clientside_order_code = models.CharField(max_length=100)
    order_name = models.CharField(max_length=100)
    pickup_location = models.ForeignKey(
        client_models.PickupLocation, on_delete=models.SET_NULL, null=True)

    order_status = models.CharField(
        max_length=100, default='Pending for Item Confirmation',
    )

    # product details
    product_catgory = models.CharField(max_length=100, blank=True)
    product_sub_catgory = models.CharField(max_length=100, blank=True)
    product_list = models.ManyToManyField(Items, blank=True)
    cash_on_delivery = models.BooleanField(default=False)
    cod_status = models.CharField(max_length=100, blank=True)
    cod_amount = models.IntegerField(default=0)
    # costumner details
    costumer_name = models.CharField(max_length=100, blank=True)
    costumer_phone = models.CharField(max_length=100, blank=True)
    costumer_whatsapp = models.CharField(max_length=100, blank=True)
    costumer_zone_no = models.CharField(max_length=100, blank=True)
    costumer_address = models.CharField(max_length=100, blank=True)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name_plural = "Order"
