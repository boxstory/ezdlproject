from django import forms


class ContactForm(forms.Form):
    DRIVER_JOB = 'd'
    FEEDBACK = 'fb'
    NEW_FEATURE = 'nf'
    DELIVERY_REQUEST = 'dr'
    OTHER = 'o'
    purpose_choices = (
        (FEEDBACK, 'Feedback'),
        (NEW_FEATURE, 'Feature Request'),
        (DELIVERY_REQUEST, 'Delivery Request'),
        (DRIVER_JOB, 'Driver Jobs'),
        (OTHER, 'Other'),
    )

    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.CharField()
    purpose = forms.ChoiceField(choices=purpose_choices)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))
