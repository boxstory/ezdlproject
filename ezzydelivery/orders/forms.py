from django import forms
from django.utils.translation import gettext_lazy as _
from requests import request
from orders.models import *
from client import models as business_models
from product import models as product_models

ORDER_STATUS = {
    ('dl_pending_payment', 'Pending Delivery charge Payment'),
    ('pending_for_item_confirmation', 'Pending for Item Confirmation'),
    ('ready_to_pickup', 'Ready to pickup'),
    ('custumer_cofirm', 'Customer Confirmation Pending'),
    ('custumer_delaying', 'Customer make delaying'),
    ('out_for_delivery', 'Out for delivery'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
}

COD_STATUS = {
    ('include', 'Include'),
    ('no_cod', 'No COD'),
    ('not_collected', 'Not Collected'),
    ('partially_collected', 'Partially Collected'),
    ('fully_paid', 'Fully Collected'),
    ('cod_with_driver', 'COD Collected with Driver'),
    ('cod_with_ezzy', 'COD handover to EZZY'),
    ('cod_sattled_with_business', 'COD Sattled with Business'),
}


# ORDERS FORM ---------------------------------------------------------------------------------------------------------------------


class AddOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['businesside_order_code', 'order_name', 'costumer_name', 'costumer_phone', 'costumer_whatsapp', 'product_list',  'cash_on_delivery', 'cod_status', 'cod_amount',
                  'costumer_zone_no', 'costumer_address',
                  'pickup_location', 'order_status',
                  ]
        exclude = ['order_number', 'business', 'delivery_task', 'deadline_date',
                   'pickup_location_id']
        widgets = {
            'order_name': forms.TextInput(attrs={'class': 'form-control'}),
            'order_status': forms.Select(attrs={'class': 'form-control'}, choices=ORDER_STATUS),
        }
        labels = {
            'order_name': _('Order Title/Short description'),
            'cod_amount': 'Balance COD with Delivery charge'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control'})
            self.fields['cash_on_delivery'].widget = forms.CheckboxInput(
                attrs={'class': 'form-check-input '})
            self.fields['order_status'].widget = forms.RadioSelect(
                choices=ORDER_STATUS)
            self.fields['cod_status'].widget = forms.RadioSelect(
                choices=COD_STATUS)
            # need to specify business only products

            self.fields['product_list'].widget = forms.CheckboxSelectMultiple()

    def save(self, commit=True):
        order = super().save(commit=False)

        if commit:
            order.save()
        return order


class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['businesside_order_code', 'costumer_name', 'costumer_phone', 'costumer_whatsapp', 'product_list',  'cash_on_delivery', 'cod_status', 'cod_amount',
                  'costumer_zone_no', 'costumer_address',
                  'pickup_location', 'order_status', 'order_name',
                  ]
        exclude = ['order_number', 'business', 'delivery_task', 'order_date',
                   'pickup_location_id']
        labels = {
            'order_name': 'Order Name / Notes',
            'cod_amount': 'Balance COD with Delivery charge'
        }
        widgets = {
            'order_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cod_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'order_status': forms.Select(attrs={'class': 'form-control'}, choices=ORDER_STATUS),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control'})
            self.fields['cash_on_delivery'].widget = forms.CheckboxInput(
                attrs={'class': 'form-check-input '})
            self.fields['order_status'].widget = forms.RadioSelect(
                choices=ORDER_STATUS)
            self.fields['cod_status'].widget = forms.RadioSelect(
                choices=COD_STATUS)
            # need to specify business only products
            self.fields['product_list'].attr = forms.ModelMultipleChoiceField(
                queryset=product_models.Product.objects.all(), widget=forms.CheckboxSelectMultiple())
