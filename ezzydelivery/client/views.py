from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from client import models as client_models
from core import models as core_models

from client import forms as client_forms

# Create your views here.


def client_dashboard(request):

    return render(request, 'client/client_dashboard.html')

# dashboard---------------------------------------------------------------------------------------------------------------------


@login_required(login_url='account_login')
def client_dashboard(request):
    try:
        client = client_models.Client.objects.get(user_id=request.user.id)
        profile = core_models.Profile.objects.get(user_id=client.user_id)
        location = client_models.PickupLocation.objects.filter(
            client_id=client.client_id).all()
        print(client)

        context = {
            'profile': profile,
            'client': client,
            'location': location,
        }
        return render(request, 'client/client_dashboard.html', context)
    except client_models.Client.DoesNotExist:
        return redirect('core:main_dashboard')

# Driver contact list of clients---------------------------------------------------------------------------------------------------------------------


def regular_driver_contacts_list(request):
    if client_models.RegularDriverContacts.objects.filter(
            client_id=request.user.id).all().exists():
        regular_driver_contacts = client_models.RegularDriverContacts.objects.filter(
            client_id=request.user.id).all()
        if not regular_driver_contacts:
            return redirect('client:regular_driver_contacts_add')
        context = {
            'contacts': regular_driver_contacts,
        }
        return render(request, 'client/parts/regular_driver_contacts_list.html', context)
    else:

        return redirect('client:regular_driver_contacts_add')
        # return HttpResponse('No Drivers contacts yet ')


def regular_driver_contacts_add(request):
    print('regular_driver_contacts_add')

    form = client_forms.RegularDriverContactsAddForm(request.POST or None)
    if request.method == 'POST':
        print('regular_driver_contacts_add POST')
        if form.is_valid():
            print('regular_driver_contacts_add valid')
            f = form.save(commit=False)
            f.client = client_models.Client.objects.get(
                client_id=request.user.id)
            print(f.client)
            print('RegularDriverContactsAddForm submitted')
            form.save()
            messages.success(request, "Successful Submission")
            return redirect("client:regular_driver_contacts_list")
        else:
            print('regular_driver_contacts_add not valid')
            messages.error(request, "Error")
    context = {
        'form': form,
    }
    return render(request, 'client/parts/regular_driver_contacts_add.html', context)


def regular_driver_contacts_delete(request, contact_id):
    contact = client_models.RegularDriverContacts.objects.get(id=contact_id)
    contact.delete()
    return redirect("client:regular_driver_contacts_list")


# pickup location add------------------------------------------------------
def pickup_location_list(request):
    pickup_location = client_models.PickupLocation.objects.filter(
        client_id=request.user.id).all()
    if not pickup_location:
        return redirect('client:pickup_location_add')
    print('pickup_location', pickup_location)
    context = {
        'pickup_location': pickup_location,
    }
    return render(request, 'client/parts/pickup_location_list.html', context)


def pickup_location_add(request):
    print(request)
    form = client_forms.PickupLocationsAddForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pickup_location = form.save(commit=False)
            pickup_location.client_id = client_models.Client.objects.get(
                user_id=request.user.id).client_id
            print(pickup_location.client)
            form.save()
            messages.success(request, "Successful Submission")
            return redirect("client:pickup_location_list")

    context = {
        'form': form,
    }
    return render(request, 'client/parts/pickup_location_add.html', context)


def pickup_location_delete(request, pickup_location_id):
    pickup_location = client_models.PickupLocation.objects.get(
        id=pickup_location_id)
    pickup_location.delete()
    return redirect("client:pickup_location_list")


def pickup_location_update(request, pickup_location_id):
    id = pickup_location_id
    print(pickup_location_id)
    print('pickup_location_update')
    pickup_location = get_object_or_404(
        client_models.PickupLocation, id=pickup_location_id)
    print(pickup_location)
    print(pickup_location.pickup_zone_no)
    form = client_forms.PickupLocationsAddForm(
        request.POST or None, instance=pickup_location)
    if request.method == 'POST':
        if form.is_valid():
            print('pickup_location_update valid')
            form.save()
            return redirect("client:pickup_location_list")

    context = {
        'form': form,
        'id': id,

    }
    return render(request, 'client/parts/pickup_location_update.html', context)

# frontend ---------------------------------------------------------------------------------------------------------------------


def client_profile(request, client_id):
    try:
        client = client_models.Client.objects.get(client_id=client_id)
        profile = core_models.Profile.objects.get(user_id=client.user_id)
        location = client_models.PickupLocation.objects.filter(
            client_id=client.client_id).values_list('pickup_location_title', flat=True)
        print(client)
        print(profile)
        print(location)

        context = {
            'profile': profile,
            'client': client,
            'location': location,
        }
        return render(request, 'client/frontend/client_profile.html', context)
    except client_models.Client.DoesNotExist:

        return redirect("/join_us/")


def all_clients(request):
    clients = client_models.Client.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'client/frontend/all_clients.html', context)
