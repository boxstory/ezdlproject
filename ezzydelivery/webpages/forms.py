from urllib import request
from django import forms
from django.forms import ModelForm
from webpages.models import *
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.bootstrap import InlineCheckboxes
from fleet import models as fleet_models


class ContactForm(forms.Form):
    DELIVERY_REQUEST = 'dr'
    FULLFILLMENT = 'fl'
    AFFLILIATE = 'af'
    DRIVER_JOB = 'd'
    FEEDBACK = 'fb'
    OTHER = 'o'
    purpose_choices = (
        (DELIVERY_REQUEST, 'Delivery Request'),
        (FULLFILLMENT, 'Fullfillment Request'),
        (AFFLILIATE, 'Affiliate Marketing Program'),
        (DRIVER_JOB, 'Driver Jobs'),
        (FEEDBACK, 'Feedback'),
        (OTHER, 'Other'),
    )

    full_name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.CharField()
    purpose = forms.MultipleChoiceField(choices=purpose_choices,
                                        widget=forms.CheckboxSelectMultiple())
    message = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 3}))

    def save(self):
        data = self.cleaned_data
        contactus = ContactUs(full_name=data['full_name'], email=data['email'],
                              mobile=data['mobile'], purpose=data['purpose'],
                              message=data['message'])
        contactus.save()
        return contactus


class CareersForm(ModelForm):
    class Meta:
        model = Careers
        fields = '__all__'

    def clean_qid(self):
        qid = self.cleaned_data.get('qid')
        print(type(qid))
        qid = str(qid)
        # Check if qid is 10 digits and starts with 2 or 3
        if not (len(qid) == 11 and qid.isdigit() and (qid.startswith('2') or qid.startswith('3'))):
            raise forms.ValidationError("The qid should be real")

        return qid

    

  
