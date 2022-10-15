from django.conf import settings
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.IntegerField(blank=True)
    whatsapp = models.IntegerField(blank=True)
    zone_name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    nationlity = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to='core/user/', default='core/user/avatar.png', blank=True, null=True)
    is_seller = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    update_time = models.DateTimeField(auto_now=True)
