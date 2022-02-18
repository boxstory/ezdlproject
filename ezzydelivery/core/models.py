from django.conf import settings
from django.db import models

# Create your models here.


class Driver(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    driver_id = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    driver_email = models.EmailField()
    driver_mobile = models.CharField(max_length=100)
    driver_area = models.CharField(max_length=100)
    driver_address = models.CharField(max_length=100)
    driver_nationality = models.CharField(max_length=100)
    driver_languages_choices = (
        ('arabic', 'Arabic'),
        ('english', 'English'),
        ('hindi', 'Hindi'),
        ('philipine', 'Philipine'),
        ('other', 'Other'),
    )

    driver_languages = models.CharField(
        max_length=100, choices=driver_languages_choices)
    driver_password = models.CharField(max_length=100)
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
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=11)
    landmark = models.CharField(max_length=100)
    zone_name = models.CharField(max_length=100)
    licence_choices = models.CharField(max_length=100)
    is_in_qatar = models.BooleanField(default=False)
    vehicle_choices = models.CharField(max_length=100)

    job_type_choices = models.CharField(max_length=100)

    def __str__(self):
        return self.f_name

    class Meta:
        verbose_name_plural = "Driver Job"
