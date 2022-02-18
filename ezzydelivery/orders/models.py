from django.conf import settings
from django.db import models

# Create your models here.


class Client(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client_id = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name_plural = "Client"


class Order(models.Model):
    order_id = models.CharField(max_length=100)
    client_id = models.ForeignKey(
        'Client', on_delete=models.CASCADE)
    order_name = models.CharField(max_length=100)

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name_plural = "Order"
