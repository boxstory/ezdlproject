from email.policy import default
from django import forms
from delivery.models import *


class DeliveryAddressForm(forms.Form):
    dl_id = forms.CharField()
    full_name = forms.CharField(max_length=100, required=True)
    mobile_no = forms.CharField(required=True)
    zone_name = forms.CharField(max_length=100, required=False)
    zone_number = forms.CharField()
    street_no = forms.CharField()
    building_no = forms.CharField()
    unit_no = forms.CharField(required=False, max_length=100,  initial='1')
    is_villa_compound = forms.BooleanField(required=False, initial=False)
    is_flat = forms.BooleanField(required=False, initial=False)
    is_office = forms.BooleanField(required=False, initial=False)
    order_id = forms.CharField(required=False)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['zone_name'].queryset = ZoneName.objects.none()

    def save(self):
        data = self.cleaned_data
        delivery_address_details = DeliveryAddress(
            dl_id=data['dl_id'],
            full_name=data['full_name'],
            mobile_no=data['mobile_no'],
            zone_name=data['zone_name'],
            zone_number=data['zone_number'],
            street_no=data['street_no'],
            building_no=data['building_no'],
            unit_no=data['unit_no'],
            is_villa_compound=data['is_villa_compound'],
            is_flat=data['is_flat'],
            is_office=data['is_office'],
            order_id=data['order_id'],
        )
        delivery_address_details.save()
        return delivery_address_details
