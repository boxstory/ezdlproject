
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from core import models as core_models
from fleet import models as fleet_models
from client import models as business_models


# BUSINESS FORM ---------------------------------------------------------------------------------------------------------------------


business_LANGUAGE_CHOICES = (
    ('arabic', 'Arabic'),
    ('english', 'English'),
    ('hindi', 'Hindi'),
    ('philipine', 'Philipine'),
    ('other', 'Other'),
)
business_STATUS_CHOICES = (
    ('aproval pending', 'Aproval Pending'),
    ('active', 'Active'),
    ('inactive', 'Inactive'),
)

# business FORM ---------------------------------------------------------------------------------------------------------------------


class businessRegisterForm(forms.ModelForm):
    class Meta:
        model = business_models.Business
        fields = '__all__'
        exclude = ['profile', 'business_id', 'user',
                   'business_status', 'business_code']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'business_languages': forms.Select(
                choices=business_LANGUAGE_CHOICES),
            'business_status': forms.Select(
                choices=business_STATUS_CHOICES),
            'brand_name': forms.TextInput(attrs={'placeholder': 'List your major brands'}),

        }
        labels = {
            "business_business_name": "business Name",
            "business_phone": "business Phone No",
            "business_whatsapp": "business Whatsapp No",
            "brand_name": "Brand Lists",
            "business_qid": "Passport/QID No",

        }

 # PICKUP LOCATIONS FORM ----------------------------------------------------------------------------------------------------------------------


class PickupLocationsAddForm(forms.ModelForm):
    class Meta:
        model = business_models.PickupLocation
        fields = '__all__'
        exclude = ['business']


class RegularDriverContactsAddForm(forms.ModelForm):
    class Meta:
        model = business_models.RegularDriverContacts
        fields = '__all__'
        exclude = ['business']
