from urllib import request
from django import forms
from core.models import *
from crispy_forms.helper import FormHelper

YEARS = [i for i in range(1930, 2020)]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone', 'address',
                  'whatsapp', 'zone_name', 'nationlity', 'date_of_birth', 'profile_pic']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['profile_pic'].required = False
        self.helper = FormHelper()
        self.helper.form_show_labels = False
