from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from client import models as business_models
from core import models as core_models

from client import forms as business_forms

# Create your views here.


def business_dashboard(request):

    return render(request, 'client/business_dashboard.html')

# dashboard---------------------------------------------------------------------------------------------------------------------


@login_required(login_url='account_login')
def business_dashboard(request):
    try:
        business = business_models.Business.objects.get(user_id=request.user.id)
        profile = core_models.Profile.objects.get(user_id=business.user_id)
        location = business_models.PickupLocation.objects.filter(
            business_id=business.business_id).all()
        print(business)

        context = {
            'profile': profile,
            'business': business,
            'location': location,
        }
        return render(request, 'client/business_dashboard.html', context)
    except business_models.Business.DoesNotExist:
        return redirect('core:main_dashboard')

# Driver contact list of business---------------------------------------------------------------------------------------------------------------------


def regular_driver_contacts_list(request):
    if business_models.RegularDriverContacts.objects.filter(
            business_id=request.user.id).all().exists():
        regular_driver_contacts = business_models.RegularDriverContacts.objects.filter(
            business_id=request.user.id).all()
        if not regular_driver_contacts:
            return redirect('business:regular_driver_contacts_add')
        context = {
            'contacts': regular_driver_contacts,
        }
        return render(request, 'client/parts/regular_driver_contacts_list.html', context)
    else:

        return redirect('business:regular_driver_contacts_add')
        # return HttpResponse('No Drivers contacts yet ')


def regular_driver_contacts_add(request):
    print('regular_driver_contacts_add')

    form = business_forms.RegularDriverContactsAddForm(request.POST or None)
    if request.method == 'POST':
        print('regular_driver_contacts_add POST')
        if form.is_valid():
            print('regular_driver_contacts_add valid')
            f = form.save(commit=False)
            f.business = business_models.Business.objects.get(
                business_id=request.user.id)
            print(f.business)
            print('RegularDriverContactsAddForm submitted')
            form.save()
            messages.success(request, "Successful Submission")
            return redirect("business:regular_driver_contacts_list")
        else:
            print('regular_driver_contacts_add not valid')
            messages.error(request, "Error")
    context = {
        'form': form,
    }
    return render(request, 'client/parts/regular_driver_contacts_add.html', context)


def regular_driver_contacts_delete(request, contact_id):
    contact = business_models.RegularDriverContacts.objects.get(id=contact_id)
    contact.delete()
    return redirect("business:regular_driver_contacts_list")


# pickup location add------------------------------------------------------
def pickup_location_list(request):
    pickup_location = business_models.PickupLocation.objects.filter(
        business_id=request.user.id).all()
    if not pickup_location:
        return redirect('business:pickup_location_add')
    print('pickup_location', pickup_location)
    context = {
        'pickup_location': pickup_location,
    }
    return render(request, 'client/parts/pickup_location_list.html', context)


def pickup_location_add(request):
    print(request)
    form = business_forms.PickupLocationsAddForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pickup_location = form.save(commit=False)
            pickup_location.business_id = business_models.Business.objects.get(
                user_id=request.user.id).business_id
            print(pickup_location.business)
            form.save()
            messages.success(request, "Successful Submission")
            return redirect("business:pickup_location_list")

    context = {
        'form': form,
    }
    return render(request, 'client/parts/pickup_location_add.html', context)


def pickup_location_delete(request, pickup_location_id):
    pickup_location = business_models.PickupLocation.objects.get(
        id=pickup_location_id)
    pickup_location.delete()
    return redirect("business:pickup_location_list")


def pickup_location_update(request, pickup_location_id):
    id = pickup_location_id
    print(pickup_location_id)
    print('pickup_location_update')
    pickup_location = get_object_or_404(
        business_models.PickupLocation, id=pickup_location_id)
    print(pickup_location)
    print(pickup_location.pickup_zone_no)
    form = business_forms.PickupLocationsAddForm(
        request.POST or None, instance=pickup_location)
    if request.method == 'POST':
        if form.is_valid():
            print('pickup_location_update valid')
            form.save()
            return redirect("business:pickup_location_list")

    context = {
        'form': form,
        'id': id,

    }
    return render(request, 'client/parts/pickup_location_update.html', context)

# frontend ---------------------------------------------------------------------------------------------------------------------


def business_profile(request, business_id):
    try:
        business = business_models.Business.objects.get(business_id=business_id)
        profile = core_models.Profile.objects.get(user_id=business.user_id)
        location = business_models.PickupLocation.objects.filter(
            business_id=business.business_id).values_list('pickup_location_title', flat=True)
        print(business)
        print(profile)
        print(location)

        context = {
            'profile': profile,
            'business': business,
            'location': location,
        }
        return render(request, 'client/frontend/business_profile.html', context)
    except business_models.Business.DoesNotExist:

        return redirect("/join_us/")


def all_business(request):
    business = business_models.Business.objects.all()
    context = {
        'business': business,
    }
    return render(request, 'client/frontend/all_business.html', context)
