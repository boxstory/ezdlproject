from django.db import models

from core import models as core_models
from orders import models as orders_models
from delivery import models as delivery_models
from client import models as client_models
from fleet import models as fleet_models


# Create your models here.

# drivers---------------------------------------------------------------------------------------------------------------------



# Task---------------------------------------------------------------------------------------------------------------------

class DeliveryTask(models.Model):
    dl_task_status = (
        ('for_review', 'For Review'),
        ('Pending', 'Pending'),
        ('Costumer Not Confirmed', 'Costumer Not Confirmed'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

    dl_task_number = models.CharField(max_length=100)
    dl_task_name = models.CharField(max_length=100)
    dl_task_description = models.CharField(max_length=100)
    dl_task_status = models.CharField(max_length=100, choices=dl_task_status)
    dl_task_date = models.DateField(auto_now_add=True)
    order = models.ForeignKey(orders_models.Order, on_delete=models.CASCADE)
    driver = models.ForeignKey(
        fleet_models.Driver, on_delete=models.CASCADE, blank=True, null=True)
    dl_task_time_slot = models.TimeField(auto_now_add=True)
    pickup_location = models.ForeignKey(
        client_models.PickupLocation, on_delete=models.CASCADE, blank=True, null=True)

    dl_category_choices = (
        ('Food', 'Food'),
        ('Regular', 'Regular'),
        ('Electronics', 'Electronics'),
        ('Others', 'Others'),
    )
    dl_category = models.CharField(
        max_length=100, choices=dl_category_choices, blank=True)
    dl_speed_choices = (
        ('Normal', 'Normal'),
        ('Same Day', 'Same Day'),
        ('On Demand',   'On Demand'),

    )
    dl_speed = models.CharField(
        max_length=100, choices=dl_speed_choices, blank=True)

    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name_plural = "Delivery Task"
        app_label = 'delivery'


class DeliveryAddress(models.Model):
    full_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=11)
    zone_name = models.CharField(max_length=100)
    zone_number = models.CharField(max_length=2)
    street_no = models.CharField(max_length=3)
    building_no = models.CharField(max_length=2)
    unit_no = models.CharField(max_length=2)
    is_villa_compound = models.BooleanField(default=False)
    is_flat = models.BooleanField(default=False)
    is_office = models.BooleanField(default=False)
    dl_id = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Delivery Address"
        app_label = 'delivery'


class ZoneName(models.Model):
    zone_name = models.CharField(max_length=100)
    zone_number = models.CharField(max_length=2)

    def __str__(self):
        return self.zone_name

    class Meta:
        verbose_name_plural = "Zone Name"
        app_label = 'delivery'
