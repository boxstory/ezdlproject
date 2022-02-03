from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"


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
    order_id = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Delivery Address"
