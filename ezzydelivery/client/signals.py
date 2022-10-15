
from venv import create
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import uuid
from fleet import models as fleet_models
from client import models as client_models


@receiver(post_save, sender=client_models.Client)
def order_pre_save_receiver(sender, instance, created, *args, **kwargs):
    print("Client post save receiver")
    if created:
        print(instance)
        if instance.id not in client_models.PickupLocation.objects.values_list('client_id', flat=True):
            client_models.PickupLocation.objects.create(
                client=instance,
                pickup_location_title='none',
            )
            instance.save()
