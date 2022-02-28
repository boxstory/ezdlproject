from urllib import request
from django import forms
from core.models import DriverJob
from webpages.models import *
from crispy_forms.helper import FormHelper


class ContactForm(forms.Form):
    DELIVERY_REQUEST = 'dr'
    FULLFILLMENT = 'fl'
    DRIVER_JOB = 'd'
    FEEDBACK = 'fb'
    OTHER = 'o'
    purpose_choices = (
        (DELIVERY_REQUEST, 'Delivery Request'),
        (FULLFILLMENT, 'Fullfillment Request'),
        (DRIVER_JOB, 'Driver Jobs'),
        (FEEDBACK, 'Feedback'),
        (OTHER, 'Other'),
    )

    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.CharField()
    purpose = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=purpose_choices,)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 3}))

    def save(self):
        data = self.cleaned_data
        contactus = ContactUs(name=data['name'], email=data['email'],
                              mobile=data['mobile'], purpose=data['purpose'],
                              message=data['message'])
        contactus.save()
        return contactus


class DriverJobForm(forms.ModelForm):
    class Meta:
        model = DriverJob
        fields = ['full_name', 'mobile_no', 'whatsapp_no', 'landmark', 'zone_name',
                  'licence', 'is_in_qatar', 'own_vehicle', 'job_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
