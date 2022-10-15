
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from core import models as core_models
from fleet import models as fleet_models
from client import models as client_models


# SELLER FORM ---------------------------------------------------------------------------------------------------------------------


CLIENT_LANGUAGE_CHOICES = (
    ('arabic', 'Arabic'),
    ('english', 'English'),
    ('hindi', 'Hindi'),
    ('philipine', 'Philipine'),
    ('other', 'Other'),
)

# Client FORM ---------------------------------------------------------------------------------------------------------------------


class ClinetRegisterForm(forms.ModelForm):
    class Meta:
        model = client_models.Client
        fields = '__all__'
        exclude = ['user', 'client_status', 'client_code']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'client_languages': forms.Select(
                choices=CLIENT_LANGUAGE_CHOICES),
            'brand_name': forms.TextInput(attrs={'placeholder': 'List your major brands'}),

        }
        labels = {
            "client_business_name": "Business Name",
            "client_phone": "Business Phone No",
            "client_whatsapp": "Business Whatsapp No",
            "brand_name": "Brand Lists",
            "client_qid": "Client QID No",

        }

 # PICKUP LOCATIONS FORM ----------------------------------------------------------------------------------------------------------------------


class PickupLocationsAddForm(forms.ModelForm):
    class Meta:
        model = client_models.PickupLocation
        fields = '__all__'
        exclude = ['client']
