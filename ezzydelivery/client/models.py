import os
from django.conf import settings
from django.db import models


# Create your models here.




# client---------------------------------------------------------------------------------------------------------------------


class Client(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client_business_name = models.CharField(
        max_length=100, blank=True, null=True)
    client_phone = models.CharField(max_length=100, blank=True, null=True)
    client_whatsapp = models.CharField(
        max_length=100, blank=True, null=True)
    brand_name = models.CharField(max_length=100)
    client_code = models.CharField(max_length=100, blank=True, null=True)

    client_languages = models.CharField(
        max_length=100,  default='english')
    client_qid = models.CharField(max_length=11, blank=True, null=True)
    client_status = {
        ('aproval pending', 'Aproval Pending'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    }
    client_status = models.CharField(
        max_length=100, choices=client_status, default='aproval pending')

    class Meta:
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.user.username


class PickupLocation(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='pickup_location')
    pickup_location_title = models.CharField(max_length=100)
    pickup_zone_no = models.CharField(max_length=100, blank=True)
    pickup_street_no = models.CharField(max_length=100, blank=True)
    pickup_building_no = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.pickup_location_title

    class Meta:
        verbose_name_plural = "Pickup Location"


def upload_path_handler(instance, filename):
    upload_dir = os.path.join('documents', instance.user.id)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)