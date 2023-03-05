from multiprocessing import context
from django.forms.fields import DateTimeField
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from core import models as core_models
from fleet import models as fleet_models
from client import models as business_models
from delivery import models as delivery_models
from orders import models as order_models

from webpages import forms as webpages_forms
from orders import forms as order_forms
from delivery import forms as delivery_forms
from fleet import forms as fleet_forms


# Create your views here.


# requst to user update address before delivery


def dl_address_update(request, dl_task_number, mobile_no):
    instance = delivery_models.DlAddressUpdate.objects.get(
        dl_task_number=dl_task_number)
    form = delivery_forms.DlAddressUpdateForm(
        request.POST or None, instance=instance)
    if request.method == 'POST':
        print("dl_address request.POST")

        f = delivery_forms.DlAddressUpdateForm(
            request.POST)

        if f.is_valid():
            print("DlAddressUpdateForm 2 is valid")
            form = f.save(commit=False)
            form.dl_task_number = dl_task_number
            form.mobile_no = mobile_no

            print(form)
            form.save()

            return redirect('/')
    else:
        print("dl_address else")

    context = {
        'form': form,
        'dl_task_number': dl_task_number,
        'mobile_no': mobile_no,
    }
    return render(request, 'delivery/dl_address.html', context)


# AJAX
def get_zone_name(request):
    zone_number = request.GET.get('zone_number')
    zone_name = delivery_models.ZoneName.objects.filter(
        zone_number=zone_number).all()
    print(zone_name)
    print("get_zone_name")
    return render(request, 'delivery/zone_names.html', {'zone_name': zone_name})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


# delivery details -------------------------------------------------------------------------


def all_delivery_tasks(request):
    driver = fleet_models.Driver.objects.get(user_id=request.user.id)
    print('fleet', driver.driver_id)
    dl_tasks = delivery_models.DeliveryTask.objects.all()
    print(dl_tasks)

    context = {
        'cards': dl_tasks,
    }
    return render(request, 'delivery/parts/tasks_all.html', context)
    # return render(request, 'delivery/all_delivery_tasks.html', context)


def assign_driver_to_task(request, dl_task_number):
    print("assign_driver_to_task")

    return redirect('/delivery/all_delivery_tasks')

# business side delivery data --------------------------------------------------------------


def delivery_business_update(request):
    data = {

    }
    return render(request, 'delivery/delivery_list.html', data)
