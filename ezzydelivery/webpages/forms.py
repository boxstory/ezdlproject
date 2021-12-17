from django import forms
from webpages.models import ContactUs


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
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 3}))

    def save(self):
        data = self.cleaned_data
        contactus = ContactUs(name=data['name'], email=data['email'],
                              mobile=data['mobile'], purpose=data['purpose'],
                              message=data['message'])
        contactus.save()
        return contactus
