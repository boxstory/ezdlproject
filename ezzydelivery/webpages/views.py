from django.forms.fields import DateTimeField
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from webpages.forms import *
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


@login_required(login_url='account_login')
def join_driver(request):
    if request.method == 'POST':
        f = DriverJobForm(request.POST)
        if f.is_valid():
            print("form is valid")

            f_name = f.cleaned_data['f_name']
            l_name = f.cleaned_data['l_name']
            mobile_no = f.cleaned_data['mobile_no']
            landmark = f.cleaned_data['landmark']

            is_own_vehicle = f.cleaned_data['is_own_vehicle']
            own_vehicle_choices = f.cleaned_data['own_vehicle_choices']
            licence_choices = f.cleaned_data['licence_choices']
            job_type_choices = f.cleaned_data['job_type_choices']
            f.save()
            return redirect('/')

    else:
        f = DriverJobForm()
    return render(request, 'webpages/join_driver.html', {'form': f})


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


def privacy(request):
    data = {

    }
    return render(request, 'webpages/privacy.html', data)
