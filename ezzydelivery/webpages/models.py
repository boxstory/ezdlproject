from django.conf import settings
from django.db import models

# Create your models here.


class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    purpose = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Contact Us"


class Careers(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    qid = models.BigIntegerField()
    job = models.CharField(max_length=100)
    self_intro = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Careers"