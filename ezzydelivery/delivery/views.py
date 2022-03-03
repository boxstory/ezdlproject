from multiprocessing import context
from django.forms.fields import DateTimeField
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from delivery.models import ZoneName
from webpages.forms import *
from delivery.forms import *
from orders.forms import *

from django.core.mail import mail_admins

# Create your views here.


@login_required(login_url='account_login')
def delivery_jobs(request):
    data = {

    }
    return render(request, 'delivery/delivery_jobs.html', data)


def delivery_address_details(request):
    if request.method == 'POST':
        f = DeliveryAddressForm(request.POST)
        if f.is_valid():
            print("DeliveryAddressForm full  is valid")

            dl_id = f.cleaned_data['dl_id']
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
    return render(request, 'delivery/delivery_address_details.html', {'form': f})


def dl_address(request, dl_id, mobile_no):
    if request.method == 'POST':
        print("dl_address request.POST")
        f = DeliveryAddressForm(request.POST)

        if f.is_valid():
            print("DeliveryAddressForm 2 is valid")
            dl_id = f.cleaned_data['dl_id']
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
            print(f.cleaned_data)

            return redirect('/')
    else:
        print("dl_address else")
        f = DeliveryAddressForm()

    zone_name = "Zone 1"
    context = {
        'form': f,
        'dl_id': dl_id,
        'mobile_no': mobile_no,
        'zone_name': zone_name,
    }
    return render(request, 'delivery/dl_address.html', context)


# AJAX
def get_zone_name(request):
    zone_number = request.GET.get('zone_number')
    zone_name = ZoneName.objects.filter(zone_number=zone_number).all()
    print(zone_name)
    print("get_zone_name")
    return render(request, 'delivery/zone_names.html', {'zone_name': zone_name})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
