import random
from django.forms.fields import DateTimeField
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from webpages.forms import *
from django.core.mail import mail_admins
from client import models as business_models
from fleet import models as fleet_models
# Create your views here.


def index(request):
    data = {

    }
    return render(request, 'webpages/index.html', data)


def delivery_pricing(request):
    data = {

    }
    return render(request, 'webpages/3pl_pricing.html', data)


def about(request):

    brands = list(business_models.Business.objects.all())
    # brands = list(fleet_models.Driver.objects.all())

    print(len(brands))
    if len(brands) > 5:
        brands = random.sample(brands, 6)
    else:
        brands = random.sample(brands, len(brands))

    print(brands)

    data = {
        'brands': brands,

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


def contactus(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
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


def page_not_found(request, exception):
    return render(request, 'webpages/page_not_found.html', status=404)


def server_error(request):
    return render(request, 'webpages/server_error.html', status=500)
