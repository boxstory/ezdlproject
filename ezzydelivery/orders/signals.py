
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from orders.models import *
from delivery.models import *
import uuid


@receiver(pre_save, sender=Order)
def order_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.order_number:
        instance.order_number = str(uuid.uuid4()).replace('-', '').upper()[:10]
        # instance.order_number = instance.client_id.client_code + \
        #     '-' + str(instance.clientside_order_code) + '-' + str(instance.id)
        print(instance.order_number)


@ receiver(post_save, sender=Order)
def order_post_save_receiver(sender, instance,  created, *args, **kwargs):
    print('order_post_save_receiver')
    if created:
        print(instance)
        if instance.id not in DeliveryTask.objects.values_list('order_id', flat=True):
            DeliveryTask.objects.create(
                order_id=instance.id,
                dl_task_number=instance.order_number,
                dl_task_name=instance.order_name,
                dl_task_description="na",
                dl_task_status='for_review',
                pickup_location_id=instance.pickup_location.id,
            )
            instance.save()
        if instance.order_number not in DlAddressUpdate.objects.values_list('dl_task_number', flat=True):
            DlAddressUpdate.objects.create(
                full_name=instance.costumer_name,
                dl_task_number=instance.order_number,
                mobile_no=instance.costumer_phone,
                zone_number=instance.costumer_zone_no,
                dl_price=instance.dl_amount,

            )
            instance.save()
