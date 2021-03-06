
from venv import create
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import uuid
from fleet import models as fleet_models


@receiver(post_save, sender=fleet_models.Driver)
def order_pre_save_receiver(sender, instance, created, *args, **kwargs):
    print("Driver post save receiver")
    if created:
        print(instance)
        if instance.id not in fleet_models.DriverVehicle.objects.values_list('driver_id', flat=True):
            fleet_models.DriverVehicle.objects.create(
                driver=instance,
                vehicle_type='none',
                vehicle_status='Inactive',
            )
            instance.save()
        if instance.id not in fleet_models.DriverDocument.objects.values_list('driver_id', flat=True):
            fleet_models.DriverDocument.objects.create(
                driver_id=instance.id,
            )
            instance.save()
