from genericpath import exists
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from core import models as core_models
from core.views import profile
from fleet import models as fleet_models
from delivery import models as delivery_models
from fleet import forms as fleet_forms

# Create your views here.


# dashboard---------------------------------------------------------------------------------------------------------------------

@login_required(login_url='accounts/login/')
def fleets(request):
    fleets = fleet_models.Driver.objects.all()
    print('fleets')
    print(fleets)
    context = {
        'fleets': fleets,
    }
    return render(request, 'fleet/fleets.html', context)


@login_required(login_url='account_login')
def fleet_dashboard(request):
    try:
        driver = fleet_models.Driver.objects.get(user_id=request.user.id)
        print('dashoboard', request.user.id)
        print(driver.id)
        profile = core_models.Profile.objects.get(user_id=driver.user_id)
        print(driver)

        driver_vehicle = fleet_models.DriverVehicle.objects.get(
            driver_id=driver.id)
        print('vehicle id: ', driver_vehicle.id)

        context = {
            'profile': profile,
            'driver': driver,
            'driver_vehicle': driver_vehicle,
        }
        return render(request, 'fleet/fleet_dashboard.html', context)
    except fleet_models.Driver.DoesNotExist:

        return redirect("/join_us/")


def update_vehicle(request):
    driver = fleet_models.Driver.objects.get(user_id=request.user.id)
    print('update_vehicle', driver.id)
    driver_vehicle = fleet_models.DriverVehicle.objects.get(
        driver_id=driver.id)
    print(driver_vehicle.id)
    form = fleet_forms.DriverVehicleForm(
        request.POST or None, instance=driver_vehicle)
    if request.method == 'POST':
        form = fleet_forms.DriverVehicleForm(
            request.POST, instance=driver_vehicle)

        if form.is_valid():
            print("VehicleForm full  is valid")
            f = form.save(commit=False)

            f.save()

        return redirect('/fleet/dashboard/')
    else:
        form = fleet_forms.DriverVehicleForm(instance=driver_vehicle)
        context = {
            'form': form,
            'instance': driver_vehicle,
        }

        return render(request, 'fleet/update_vehicle.html', context)


def driver_documents(request):
    driver = fleet_models.Driver.objects.get(user_id=request.user.id)
    print('driver_documents', driver.id)
    documents = fleet_models.DriverDocument.objects.filter(
        driver_id=driver.id)
    context = {
        'documents': documents,
    }
    return render(request, 'fleet/driver_documents.html', context)


def driver_documents_upload(request):
    driver = fleet_models.Driver.objects.get(user_id=request.user.id)
    print('driver_documents_upload', driver.id)
    form = fleet_forms.DriverDocumentForm(
        request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = fleet_forms.DriverDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print("DriverDocumentForm full  is valid")
            f = form.save(commit=False)
            f.driver_id = driver.id
            f.save()
            return redirect('/fleet/documents/')
    else:
        form = fleet_forms.DriverDocumentForm()
        context = {
            'form': form,
        }

        return render(request, 'fleet/parts/upload_document.html', context)


def driver_documents_delete(request, id):
    print('delete', id)
    driver = fleet_models.Driver.objects.get(user_id=request.user.id)
    print('fleet', driver.id)
    document = fleet_models.DriverDocument.objects.filter(id=id)
    document.delete()
    return redirect('/fleet/dashboard/')
# delivery tasks ----------------------------------------------------------------------------------------------------------------------------


def all_delivery_tasks(request):
    driver = fleet_models.Driver.objects.get(user_id=request.user.id)
    print('fleet', driver.id)
    dl_tasks = delivery_models.DeliveryTask.objects.all()
    context = {
        'dl_tasks': dl_tasks,
    }
    return render(request, 'fleet/parts/all_delivery_tasks.html', context)
