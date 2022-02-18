from django import forms
from webpages.models import *


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


class DriverJobForm(forms.Form):
    vehicle_choices = (
        ('none', 'None'),
        ('bike', 'Bike'),
        ('car', 'Car'),
        ('van', 'Van'),
        ('pickup', 'Pickup'),
        ('pickup_big', 'Pickup Big'),

    )
    licence_choices = (
        ('none', 'None'),
        ('2wheeler', '2 Wheeler'),
        ('4wheeler', '4 Wheeler'),
        ('heavy', 'Heavy'),
    )
    job_type_choices = (
        ('part_time', 'Part Time'),
        ('full_time', 'Full Time'),
        ('both', 'Both'),
    )
    user_id = forms.CharField()
    f_name = forms.CharField()
    l_name = forms.CharField()
    mobile_no = forms.CharField()
    landmark = forms.CharField()
    zone_name = forms.CharField()
    is_in_qatar = forms.BooleanField(required=False)
    own_vehicle_choices = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=vehicle_choices,)

    licence_choices = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=licence_choices,)
    job_type_choices = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=job_type_choices,)

    def save(self):
        data = self.cleaned_data
        driverjob = DriverJob(user_id=data['user_id'],
                              f_name=data['f_name'], l_name=data['l_name'],
                              mobile=data['mobile'], landmark=data['landmark'],
                              zone_name=data['zone_name'],
                              is_own_vehicle=data['is_own_vehicle'],
                              own_vehicle_choices=data['own_vehicle_choices'],
                              licence_choices=data['licence_choices'],
                              job_type_choices=data['job_type_choices'],
                              )
        driverjob.save()
        return driverjob
