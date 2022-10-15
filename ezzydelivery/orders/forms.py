from django import forms
from orders.models import *
from client import models as client_models

ORDER_STATUS = {
    ('pending payment', 'Pending Payment'),
    ('pending for item confirmation', 'Pending for Item Confirmation'),
    ('ready to pickup', 'ready to pickup'),
    ('Out for delivery', 'Out for delivery'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
}
COD_STATUS = {
    ('include', 'Include'),
    ('no cod', 'No COD'),
    ('not collected', 'Not Collected'),
    ('partially collected', 'Partially Collected'),
    ('fully collected', 'Fully Collected'),
    ('cod sattled', 'COD Sattled'),
}



# ORDERS FORM ---------------------------------------------------------------------------------------------------------------------


class AddOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['clientside_order_code', 'costumer_name', 'costumer_phone', 'costumer_whatsapp', 'product_list',  'cash_on_delivery', 'cod_status', 'cod_amount',
                  'costumer_zone_no', 'costumer_address',
                  'pickup_location', 'order_status', 'order_name',
                  ]
        exclude = ['order_number', 'client', 'delivery_task', 'order_date',
                   'pickup_location_id']
        widgets = {
            'order_name': forms.TextInput(attrs={'class': 'form-control'}),
            'order_status': forms.Select(attrs={'class': 'form-control'}, choices=ORDER_STATUS),
        }
        labels = {
            'order_name': 'Order Name / Note',
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
            # need to specify clients only products
            self.fields['product_list'].queryset = Items.objects.all()
            self.fields['product_list'].widget = forms.CheckboxSelectMultiple(
                attrs={'class': 'form-check-input'})

    def save(self, commit=True):
        order = super().save(commit=False)

        if commit:
            order.save()
        return order


class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['clientside_order_code', 'costumer_name', 'costumer_phone', 'costumer_whatsapp', 'product_list',  'cash_on_delivery', 'cod_status', 'cod_amount',
                  'costumer_zone_no', 'costumer_address',
                  'pickup_location', 'order_status', 'order_name',
                  ]
        exclude = ['order_number', 'client', 'delivery_task', 'order_date',
                   'pickup_location_id']
        widgets = {
            'order_name': forms.TextInput(attrs={'class': 'form-control'}),
            'order_status': forms.Select(attrs={'class': 'form-control'}, choices=ORDER_STATUS),
        }
        labels = {
            'order_name': 'Order Name / Note',
        }


# ITEMS FORM ----------------------------------------------------------------------------------------------------------------------

class AddItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        verbose_name = 'Items'
        verbose_name_plural = 'Itemss'
        fields = '__all__'

        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'item_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'item_quantity': forms.NumberInput(attrs={'class': 'form-control'}),

        }


