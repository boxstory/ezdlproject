from django.db import models

# Create your models here.


class ZoneName(models.Model):
    zone_name = models.CharField(max_length=100)
    zone_number = models.CharField(max_length=2)

    def __str__(self):
        return self.zone_name

    class Meta:
        verbose_name_plural = "Zone Name"


class DeliveryTask(models.Model):
    dl_task_status = (
        ('Pending', 'Pending'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
        ('Costumer Not Confirmed', 'Costumer Not Confirmed'),
        ('Cancelled', 'Cancelled'),
    )

    dl_task_id = models.CharField(max_length=100)
    dl_task_name = models.CharField(max_length=100)
    dl_task_description = models.CharField(max_length=100)
    dl_task_status = models.CharField(max_length=100, choices=dl_task_status)
    dl_task_date = models.DateField(auto_now_add=True)
    order_id = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    driver_id = models.ForeignKey('core.Driver', on_delete=models.CASCADE)
    dl_category_choices = (
        ('Food', 'Food'),
        ('Regular', 'Regular'),
        ('Electronics', 'Electronics'),
        ('Others', 'Others'),
    )
    dl_category = models.CharField(max_length=100, choices=dl_category_choices)
    dl_speed_choices = (
        ('Normal', 'Normal'),
        ('Same Day', 'Same Day'),
        ('On Demand',   'On Demand'),

    )
    dl_speed = models.CharField(max_length=100, choices=dl_speed_choices)

    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name_plural = "Delivery Task"


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

   
