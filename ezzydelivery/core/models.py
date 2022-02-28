from collections import UserDict
from email.policy import default
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


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


@ receiver(post_save, sender=UserDict)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@ receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Driver(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    driver_id = models.CharField(max_length=100)
    driver_languages_choices = (
        ('arabic', 'Arabic'),
        ('english', 'English'),
        ('hindi', 'Hindi'),
        ('philipine', 'Philipine'),
        ('other', 'Other'),
    )
    driver_languages = models.CharField(
        max_length=100, choices=driver_languages_choices)
    driver_license_number = models.CharField(max_length=100)
    driver_qid = models.CharField(max_length=11)
    driver_status = (
        ('aproval pending', 'Aproval Pending'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    driver_status = models.CharField(max_length=100, choices=driver_status)
    driver_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.driver_name

    class Meta:
        verbose_name_plural = "Driver"


class DriverJob(models.Model):
    VEHICLE_CHOICES = [
        ('none', 'None'),
        ('bike', 'Bike'),
        ('car', 'Car'),
        ('van', 'Van'),
        ('pickup', 'Pickup'),
        ('pickup_big', 'Pickup Big'),

    ]

    LICENCE_CHOICES = [
        ('none', 'None'),
        ('2wheeler', '2 Wheeler'),
        ('4wheeler', '4 Wheeler'),
        ('heavy', 'Heavy'),
    ]

    JOB_TYPE_CHOICES = [
        ('part_time', 'Part Time'),
        ('full_time', 'Full Time'),
        ('both', 'Both'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    whatsapp_no = models.IntegerField()
    landmark = models.CharField(max_length=100)
    zone_name = models.CharField(max_length=100)
    licence = models.CharField(max_length=100, choices=LICENCE_CHOICES)
    is_in_qatar = models.BooleanField(default=False, )
    job_type = models.CharField(
        max_length=100, choices=JOB_TYPE_CHOICES)
    own_vehicle = models.CharField(
        max_length=100, choices=VEHICLE_CHOICES)

    def __str__(self):
        return self.f_name

    class Meta:
        verbose_name_plural = "Driver Job"
