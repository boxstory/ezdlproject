from django import forms
from webpages.models import ContactUs, DeliveryAddress


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
    purpose = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=purpose_choices,)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 3}))

    def save(self):
        data = self.cleaned_data
        contactus = ContactUs(name=data['name'], email=data['email'],
                              mobile=data['mobile'], purpose=data['purpose'],
                              message=data['message'])
        contactus.save()
        return contactus

class DeliveryAddressForm(forms.Form):
    full_name = forms.CharField()
    mobile_no = forms.CharField()
    zone_name = forms.CharField()
    zone_number = forms.CharField()
    street_no = forms.CharField()
    building_no = forms.CharField()
    unit_no = forms.CharField()
    is_villa_compound = forms.BooleanField()
    is_flat = forms.BooleanField()

    def save(self):
        data = self.cleaned_data
        delivery_address_details = DeliveryAddress(
            full_name=data['full_name'],
            mobile_no=data['mobile_no'],
            zone_name=data['zone_name'],
            zone_number=data['zone_number'],
            street_no=data['street_no'],
            building_no=data['building_no'],
            unit_no=data['unit_no'],
            is_villa_compound=data['is_villa_compound'],
            is_flat=data['is_flat'],
        )
        delivery_address_details.save()
        return delivery_address_details