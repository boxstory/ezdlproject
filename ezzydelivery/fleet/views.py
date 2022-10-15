from genericpath import exists
from multiprocessing import context
from django.db import connection
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from core import models as core_models
from core.views import profile
from fleet import models as fleet_models
from delivery import models as delivery_models
from fleet import forms as fleet_forms

# Create your views here.


# dashboard---------------------------------------------------------------------------------------------------------------------

@login_required(login_url='/accounts/login/')
def fleets(request):
    fleets = fleet_models.Driver.objects.all()
    print(fleets)
    driver_vehicle = fleet_models.DriverVehicle.objects.all()
    ft = fleet_models.Driver.objects.raw('''SELECT fleet_driver.driver_id, fleet_driver.driver_code, fleet_drivervehicle.id, fleet_drivervehicle.vehicle_type FROM fleet_driver INNER JOIN fleet_drivervehicle
ON fleet_driver.driver_id = fleet_drivervehicle.driver_id;''')
    vehicle_list = []

    for driver in fleets:
        driver_vehicle = fleet_models.DriverVehicle.objects.filter(
            driver_id=driver.driver_id).values_list('vehicle_type', flat=True)
        print('driver_vehicle ', driver_vehicle)
        vehicle_list.append(driver_vehicle)
    print(vehicle_list)
    print(driver_vehicle)
    # print(connection.queries)
    context = {
        'fleets': fleets,
        'vehicle_list': vehicle_list,
        'driver_vehicle': driver_vehicle,
    }
    return render(request, 'fleet/fleets.html', context)


@login_required(login_url='/accounts/login/')
def fleet_dashboard(request):
    try:
        driver = fleet_models.Driver.objects.get(user_id=request.user.id)
        profile = core_models.Profile.objects.get(user_id=driver.user_id)
        driver_vehicle = fleet_models.DriverVehicle.objects.filter(
            driver_id=driver.driver_id)
        print('vehicle id: ', driver_vehicle)

        context = {
            'profile': profile,
            'driver': driver,
            'driver_vehicle': driver_vehicle,
        }
        return render(request, 'fleet/fleet_dashboard.html', context)

    except fleet_models.Driver.DoesNotExist:
        print('driver does not exist')
        return redirect('core:main_dashboard')

# document---------------------------------------------------------------------------------------------------------------------


def driver_documents(request):
    driver = fleet_models.Driver.objects.get(user_id=request.user.id)
    print('driver_documents', driver.driver_id)
    documents = fleet_models.DriverDocument.objects.filter(
        driver_id=driver.driver_id)
    context = {
        'documents': documents,
    }
    return render(request, 'fleet/parts/document_all.html', context)


def driver_documents_upload(request):
    driver = fleet_models.Driver.objects.get(user_id=request.user.id)
    print('driver_documents_upload', driver.driver_id)
    form = fleet_forms.DriverDocumentForm(
        request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = fleet_forms.DriverDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print("DriverDocumentForm full  is valid")
            f = form.save(commit=False)
            f.driver_id = driver.driver_id
            f.save()
            return redirect('/fleet/documents/')
    else:
        form = fleet_forms.DriverDocumentForm()
        context = {
            'form': form,
        }

        return render(request, 'fleet/parts/document_upload.html', context)


def driver_documents_update(request, fleet_id, doc_id):
    print('update', id)
    if fleet_id != request.user.id:
        return redirect('/fleet/documents/')
    driver = fleet_models.Driver.objects.get(user_id=fleet_id)
    print('fleet', driver.driver_id)
    document = fleet_models.DriverDocument.objects.get(id=doc_id)
    form = fleet_forms.DriverDocumentForm(
        request.POST or None, instance=document)
    if request.method == 'POST':

        if form.is_valid():
            print("DriverDocumentForm full  is valid")
            f = form.save(commit=False)
            f.driver_id = driver.driver_id
            f.save()
            return redirect('/fleet/documents/')
    else:
        form = fleet_forms.DriverDocumentForm(instance=document)
        context = {
            'form': form,
        }

    return render(request, 'fleet/parts/document_update.html', context)


def driver_documents_delete(request, fleet_id, doc_id):
    print('delete', id)
    if fleet_id != request.user.id:
        return redirect('/fleet/documents/')
    driver = fleet_models.Driver.objects.get(user_id=fleet_id)
    print('fleet', driver.driver_id)
    document = fleet_models.DriverDocument.objects.filter(id=doc_id)
    document.delete()
    return redirect('/fleet/dashboard/')


# vehicle---------------------------------------------------------------------------------------------------------------------

def vehicle_own(request):
    driver = fleet_models.Driver.objects.get(user_id=request.user.id)
    print('vehicle_own', driver.driver_id)
    vehicles = fleet_models.DriverVehicle.objects.filter(
        driver_id=driver.driver_id)
    print('vehicle_own', vehicles)
    context = {
        'vehicles': vehicles,
    }
    return render(request, 'fleet/parts/vehicle_own.html', context)


def vehicle_add(request):
    print('vehicle_add')
    form = fleet_forms.VehicleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print("VehicleForm full  is valid")
            f = form.save(commit=False)
            f.save()
            return redirect('/fleet/vehicles/')
    else:
        form = fleet_forms.VehicleForm()
        context = {
            'form': form,
        }

    return render(request, 'fleet/parts/vehicle_add.html', context)


def vehicle_delete(request, fleet_id, vehicle_id):
    print('vehicle_delete', id)
    if fleet_id != request.user.id:
        return redirect('/fleet/vehicles/')
    vehicle = fleet_models.Vehicle.objects.filter(id=vehicle_id)
    vehicle.delete()
    return redirect('/fleet/vehicles/')


def vehicle_update(request):
    driver = fleet_models.Driver.objects.get(user_id=request.user.id)
    print('update_vehicle', driver.driver_id)
    driver_vehicle = fleet_models.DriverVehicle.objects.get(
        driver_id=driver.driver_id)
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


# delivery tasks ----------------------------------------------------------------------------------------------------------------------------


# Front end -------------------------------------------------------------------------------------------------------------------------------------------------

# driver profile -------------------------------------------------------------------------------------------------------------------------------------------------
def driver_profile(request, fleet_id):
    try:
        driver = fleet_models.Driver.objects.get(driver_id=fleet_id)

    except fleet_models.Driver.DoesNotExist:
        print('driver does not exist')
        return redirect('/fleet/')
    print('driver_profile', driver.driver_id)

    profile = core_models.Profile.objects.get(user_id=driver.user_id)
    print(driver)

    driver_vehicle = driver.driver_vehicle.all()
    print('vehicle id: ', driver_vehicle)
    driver_documents = driver.driver_document.all()
    print('driver_documents', driver_documents)

    context = {
        'profile': profile,
        'driver': driver,
        'driver_documents': driver_documents,
        'driver_vehicle': driver_vehicle,
    }
    return render(request, 'fleet/frontend/driver_profile.html', context)
