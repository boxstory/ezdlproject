from email.policy import default
import os
from django.conf import settings
from django.db import models
from core import models as core_models
from fleet import models as fleet_models


# Create your models here.


def upload_path_handler(instance, filename):
    upload_dir = os.path.join('business', instance.business.business_code, 'logo')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)
# business---------------------------------------------------------------------------------------------------------------------


class Business(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='business')
    profile = models.ForeignKey(
        core_models.Profile, on_delete=models.SET_NULL, blank=True, null=True, related_name='business')
    business_id = models.PositiveIntegerField(primary_key=True)
    business_business_name = models.CharField(
        max_length=100, blank=True, null=True)
    business_bio = models.CharField(max_length=225, blank=True, null=True)
    business_phone = models.CharField(max_length=100, blank=True, null=True)
    business_logo = models.ImageField(
        upload_to=upload_path_handler, default="business/avathar.png", blank=True, null=True)
    business_whatsapp = models.CharField(
        max_length=100, blank=True, null=True)
    brand_name = models.CharField(max_length=100)
    brand_since = models.DateField(max_length=100, blank=True, null=True)
    brand_product_category = models.CharField(
        max_length=100, blank=True, null=True)
    business_code = models.CharField(max_length=100, blank=True, null=True)
    business_languages = models.CharField(
        max_length=100,  default='english')
    business_qid = models.CharField(max_length=11, blank=True, null=True)
    business_status = models.CharField(
        max_length=100, default='aproval pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "business"

    def __str__(self):
        return self.user.username


class PickupLocation(models.Model):
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name='pickup_location')
    pickup_location_title = models.CharField(max_length=100)
    pickup_zone_no = models.PositiveIntegerField(blank=True)
    pickup_street_no = models.PositiveIntegerField(blank=True)
    pickup_building_no = models.PositiveIntegerField(
        blank=True)

    def __str__(self):
        return self.pickup_location_title

    class Meta:
        verbose_name_plural = "Pickup Location"



class RegularDriverContacts(models.Model):
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name='regular_driver_contact')
    driver = models.ForeignKey(
        fleet_models.Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.driver.driver_code

    class Meta:
        verbose_name_plural = "Regular Drivers Contacts"