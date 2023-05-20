from datetime import datetime
from django.db import models
from django.conf import settings
import os
from core import models as core_models


# Create your models here.


# fleet---------------------------------------------------------------------------------------------------------------------
VEHICLE_CHOICES = [
    ('none', 'None'),
    ('bike', 'Bike'),
    ('car', 'Car'),
    ('van', 'Van'),
    ('pickup', 'Pickup'),
    ('pickup3ton', 'Pickup 3Ton'),
    ('pickup_big', 'Pickup Big Items'),

]


class DriverVacancyAplication(models.Model):

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


class Driver(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile = models.ForeignKey(
        core_models.Profile, on_delete=models.SET_NULL, blank=True, null=True, related_name='driver')
    driver_id = models.PositiveSmallIntegerField(primary_key=True)

    driver_code = models.CharField(max_length=100)
    driver_phone = models.CharField(max_length=100)
    driver_whatsapp = models.CharField(max_length=100)
    driver_bio = models.CharField(max_length=225, blank=True, null=True)
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
    driver_rating = models.IntegerField(default=0)
    driver_rating_count = models.IntegerField(default=0)
    driver_reviews = models.TextField(default="")
    driver_reviews_count = models.IntegerField(default=0)
    driver_status_choices = (
        ('Pending on Review', 'Pending on Review'),
        ('Processing', 'Processing'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Blocked', 'Blocked'),
    )
    driver_status = models.CharField(max_length=100, choices=driver_status_choices)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.driver_code

    class Meta:
        verbose_name_plural = "Driver"


class DriverVehicle(models.Model):
    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE, related_name='driver_vehicle')
    vehicle_type = models.CharField(
        max_length=100, choices=VEHICLE_CHOICES, default='none')
    vehicle_no = models.CharField(max_length=100, blank=True, null=True)
    vehicle_model = models.CharField(max_length=100, blank=True, null=True)
    vehicle_color = models.CharField(max_length=100, blank=True, null=True)
    VEHICLE_STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    vehicle_status = models.CharField(
        max_length=100, choices=VEHICLE_STATUS, default='Inactive')
    vehicle_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.vehicle_no)

    class Meta:
        verbose_name_plural = "Driver Vehicle"


def upload_path_handler(instance, filename):
    upload_dir = os.path.join('documents', instance.user.id)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)


class DriverDocument(models.Model):
    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE, related_name='driver_document')
    qid_no = models.CharField(max_length=100)
    qid_expirey_date = models.DateField()
    qid_photo = models.ImageField(
        upload_to=upload_path_handler, default='core/driver/qid_default.jpg', blank=True, null=True)
    license_photo = models.ImageField(
        upload_to=upload_path_handler, default='core/driver/licence_default.jpg', blank=True, null=True)

    document_no = models.CharField(max_length=100)

    document_type = models.CharField(max_length=100)
    document_date = models.DateField(auto_now_add=True)
    document_update_date = models.DateField(auto_now=True)
    document_file = models.ImageField(
        upload_to=upload_path_handler, default='core/driver/licence_default.jpg', blank=True, null=True)

    def __str__(self):
        return self.document_no

    class Meta:
        verbose_name_plural = "Driver Document"
