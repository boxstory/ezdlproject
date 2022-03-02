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


def terms(request):
    data = {

    }
    return render(request, 'webpages/terms.html', data)


def test(request):
    data = {

    }
    return render(request, 'webpages/test.html', data)


def fullfillment(request):
    data = {

    }
    return render(request, 'webpages/fullfillment.html', data)


def fleets(request):
    data = {

    }
    return render(request, 'webpages/fleets.html', data)


@login_required(login_url='account_login')
def join_driver(request):
    print("join driver")
    if request.method == 'POST':
        print("POST")
        driverjobform = DriverJobForm(request.POST or None)

        print('driverjobform valid checking')
        print(driverjobform.is_valid())
        print(driverjobform.errors)
        if driverjobform.is_valid():

            print("driverjobform is valid")
            form = driverjobform.save(commit=False)
            form.user_id = request.user.id
            form.save()

            return redirect('/')

    else:
        print("load form")
        driverjobform = DriverJobForm()
    return render(request, 'webpages/join_driver.html', {'driverjobform': driverjobform})


def contactus(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            print("form is valid")

            full_name = f.cleaned_data['full_name']
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
