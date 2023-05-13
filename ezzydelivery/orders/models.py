from datetime import datetime
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
    ('ready_to_pickup', 'Ready to pickup'),
    ('custumer_delaying', 'Customer make delaying'),
    ('custumer_cofirm', 'Customer Confirmation Pending'),
    ('out_for_delivery', 'Out for delivery'),
    ('cancelled', 'Cancelled'),
    ('delivered', 'Delivered'),
    ('dl_pending_payment', 'Pending Delivery charge Payment'),
}
COD_STATUS = {
    ('include', 'Include'),
    ('no_cod', 'No COD'),
    ('not_collected', 'Not Collected'),
    ('partially_collected', 'Partially Collected'),
    ('fully_paid', 'Fully Collected'),
    ('cod_with_driver', 'COD Collected with Driver'),
    ('cod_with_ezzy', 'COD handover to EZZY'),
    ('cod_sattled_with_business', 'COD Sattled with Business'),
}

# orders---------------------------------------------------------------------------------------------------------------------


class Order(models.Model):
    order_number = models.CharField(max_length=100)
    business = models.ForeignKey(
        business_models.Business, on_delete=models.CASCADE, related_name='order')

    businesside_order_code = models.CharField(max_length=100)
    order_name = models.CharField(max_length=100)
    pickup_location = models.ForeignKey(
        business_models.PickupLocation, on_delete=models.SET_NULL, null=True)

    order_status = models.CharField(
        max_length=100, choices=ORDER_STATUS, default='ready_to_pickup',
    )

    # product details
    product_catgory = models.CharField(max_length=100, blank=True)
    product_sub_catgory = models.CharField(max_length=100, blank=True)
    product_list = models.ManyToManyField(product_models.Product, blank=True)

    # cod details
    cash_on_delivery = models.BooleanField(default=False)
    cod_status = models.CharField(
        max_length=100, choices=COD_STATUS, blank=True)
    cod_amount = models.IntegerField(default=0)
    dl_amount = models.IntegerField(default=0)
    # costumner details
    customer_name = models.CharField(max_length=100, blank=True)
    customer_phone = models.CharField(max_length=100, blank=True)
    customer_whatsapp = models.CharField(max_length=100, blank=True)
    customer_zone_no = models.PositiveIntegerField(blank=True)
    customer_address = models.CharField(max_length=100, blank=True)
    deadline_date = models.CharField(max_length=100, blank=True)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name_plural = "Order"
