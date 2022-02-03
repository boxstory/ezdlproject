from django.forms.fields import DateTimeField
from django.shortcuts import redirect, render
from webpages.forms import ContactForm, DeliveryAddressForm
from django.core.mail import mail_admins

# Create your views here.


def index(request):
    data = {

    }
    return render(request, 'webpages/index.html', data)


def about(request):
    data = {

    }
    return render(request, 'webpages/about.html', data)


def services(request):
    data = {

    }
    return render(request, 'webpages/services.html', data)


def fullfillment(request):
    data = {

    }
    return render(request, 'webpages/fullfillment.html', data)


def join_driver(request):
    data = {

    }
    return render(request, 'webpages/join_driver.html', data)


def contactus(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            print("form is valid")

            name = f.cleaned_data['name']
            email = f.cleaned_data['email']
            mobile = f.cleaned_data['mobile']
            purpose = f.cleaned_data['purpose']

            message = f.cleaned_data['message']

            f.save()

            return redirect('/')

    else:
        f = ContactForm()

    return render(request, 'webpages/contactus.html', {'form': f})


def delivery_address_details(request):
    if request.method == 'POST':
        f = DeliveryAddressForm(request.POST)
        if f.is_valid():
            print("form is valid")

            full_name = f.cleaned_data['full_name']
            mobile_no = f.cleaned_data['mobile_no']
            zone_name = f.cleaned_data['zone_name']
            zone_number = f.cleaned_data['zone_number']
            street_no = f.cleaned_data['street_no']
            building_no = f.cleaned_data['building_no']
            unit_no = f.cleaned_data['unit_no']
            is_villa_compound = f.cleaned_data['is_villa_compound']
            is_flat = f.cleaned_data['is_flat']

            f.save()

            return redirect('/')

    else:
        f = DeliveryAddressForm()

    return render(request, 'webpages/delivery_address_details.html', {'form': f})


def privacy(request):
    data = {

    }
    return render(request, 'webpages/privacy.html', data)
