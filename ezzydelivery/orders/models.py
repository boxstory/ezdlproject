from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from delivery import models as delivery_models
from core import models as core_models
from fleet import models as fleet_models
from client import models as business_models
from orders import models as orders_models
from webpages import models as webpages_models
from product import models as product_models


# Create your models here.

ORDER_STATUS = {
    ('to_review', 'To Review'),
    ('ready_to_pickup', 'Ready to pickup'),
    ('out_for_delivery', 'Out for delivery'),
    ('delivered', 'Delivered'),
    ('customer _cofirm', 'Customer Confirmation Pending'),
    ('customer _delaying', 'Customer make delaying'),
    ('cancelled', 'Cancelled'),
    ('dl_pending_payment', 'Pending Delivery charge Payment'),
}
COD_STATUS_BY_CLIENT = {
    ('no_cod', 'No COD'),
    ('include', 'Include'),
}
COD_STATUS_BY_STAFF = {
    ('not_collected', 'Not Collected'),
    ('partially_collected', 'Partially Collected'),
    ('fully_paid', 'Fully Collected'),
    ('cod_with_driver', 'COD Collected & with Driver'),
    ('cod_with_ezzy', 'COD handover to EZZY'),
    ('cod_sattled_with_business', 'COD Sattled with Business'),
}

# orders---------------------------------------------------------------------------------------------------------------------


class Order(models.Model):
    order_number = models.CharField(max_length=64, unique=True)
    business = models.ForeignKey(
        business_models.Business, on_delete=models.CASCADE, related_name='order')
    client_order_code = models.CharField(max_length=64, unique=True)
    order_notes = models.CharField(max_length=100)
    order_status = models.CharField(
        max_length=100, choices=ORDER_STATUS, default='to_review',
    )

    # pickup details
    pickup_location = models.ForeignKey(
        business_models.PickupLocation, on_delete=models.SET_NULL, null=True)

    # cod details
    cash_on_delivery = models.BooleanField(default=False)
    cod_status_by_client = models.CharField(
        max_length=100, choices=COD_STATUS_BY_CLIENT, blank=True, null=True)
    cod_status_by_staff = models.CharField(
        max_length=100, choices=COD_STATUS_BY_STAFF, blank=True, null=True)
    cod_amount = models.IntegerField(default=0)
    dl_included = models.BooleanField(default="True")
    dl_amount = models.IntegerField(default=0)

    # Delivery customer details
    customer_name = models.CharField(max_length=100, blank=True)
    customer_phone = models.CharField(max_length=100, blank=True)
    customer_whatsapp = models.CharField(max_length=100, blank=True)
    customer_address = models.CharField(max_length=100, blank=True)
    deadline_date = models.CharField(max_length=100, blank=True)
    order_date = models.DateField(auto_now_add=True)
    dl_zone = models.PositiveIntegerField(blank=True)
    dl_building = models.PositiveIntegerField(blank=True)
    dl_street = models.PositiveIntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.order_number}-{self.client_order_code})'

    class Meta:
        verbose_name_plural = "Order"


class OrderProductList(models.Model):
    order =  models.ForeignKey(
        orders_models.Order, on_delete=models.CASCADE, related_name='order_product_list')
    product01_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product01_qty = models.PositiveIntegerField(blank=True, null=True, default=0)
    product02_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product02_qty = models.PositiveIntegerField(blank=True, null=True, default=0)
    product03_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product03_qty = models.PositiveIntegerField(blank=True, null=True, default=0)
    product04_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product04_qty = models.PositiveIntegerField(blank=True, null=True, default=0)
    product05_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product05_qty = models.PositiveIntegerField(blank=True, null=True, default=0)
    product06_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product06_qty = models.PositiveIntegerField(blank=True, null=True, default=0)
    product07_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product07_qty = models.PositiveIntegerField(blank=True, null=True, default=0)
    product08_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product08_qty = models.PositiveIntegerField(blank=True, null=True, default=0)
    product09_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product09_qty = models.PositiveIntegerField(blank=True, null=True, default=0)
    product10_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product10_qty = models.PositiveIntegerField(blank=True, null=True, default=0)
    product11_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product11_qty = models.PositiveIntegerField(blank=True, null=True, default=0)
    product12_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product12_qty = models.PositiveIntegerField(blank=True, null=True, default=0)
    product13_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product13_qty = models.PositiveIntegerField(blank=True, null=True, default=0)
    product14_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product14_qty = models.PositiveIntegerField(blank=True, null=True, default=0)
    product15_name = models.ForeignKey(product_models.Product, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    product15_qty = models.PositiveIntegerField(blank=True, null=True, default=0)

    
    def __str__(self):
        return self.order

    class Meta:
        verbose_name_plural = "Order product lists"