from django import forms


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
    purpose = forms.ChoiceField(choices=purpose_choices)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))


