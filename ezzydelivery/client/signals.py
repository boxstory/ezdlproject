
from venv import create
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import uuid
from fleet import models as fleet_models
from client import models as business_models

# @todo post pickup location while add business join
# @receiver(post_save, sender=business_models.Business)
# def order_pre_save_receiver(sender, instance, created, *args, **kwargs):
#     print("business post save receiver")
#     if created:
#         print(instance)
#         print(instance.id)
#         if instance.id not in business_models.PickupLocation.objects.values_list('business_id', flat=True):
#             business_models.PickupLocation.objects.create(
#                 business=instance,
#                 pickup_location_title='none',
#             )
#             instance.save()
