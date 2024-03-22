
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
        # instance.order_number = instance.business_id.business_code + \
        #     '-' + str(instance.client_order_code) + '-' + str(instance.id)
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
                dl_task_description=instance.order_notes,
                dl_task_status='for_review',
                pickup_location_id=instance.pickup_location.id,
            )
            instance.save()
        if instance.order_number not in DlAddressUpdate.objects.values_list('dl_task_number', flat=True):
            DlAddressUpdate.objects.create(
                full_name=instance.customer_name,
                dl_task_number=instance.order_number,
                mobile_no=instance.customer_phone,
                dl_zone=instance.dl_zone,
                dl_street=instance.dl_street,
                dl_building=instance.dl_building,
                dl_longitude='0',
                dl_latitude = '0',

            )
            instance.save()
        if instance.id not in OrderProductList.objects.values_list('order', flat=True):
            OrderProductList.objects.create(
                order_id=instance.id,
                
            )
            instance.save()
