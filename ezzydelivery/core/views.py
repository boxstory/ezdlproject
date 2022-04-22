
from unicodedata import name
from django.contrib.auth.models import User
from PIL import Image
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


from core import models as core_models
from fleet import models as fleet_models
from core import forms as core_forms
from webpages import forms as webpages_forms
from fleet import forms as fleet_forms
from client import forms as client_forms


# Create your views here.


# joins---------------------------------------------------------------------------------------------------------------------
def join_seller(request):
    clientresisterform = client_forms.ClinetRegisterForm()
    if request.method == 'POST':
        form = client_forms.ClinetRegisterForm(request.POST)
        if form.is_valid():
            print("ClientForm full  is valid")
            f = form.save(commit=False)
            f.save()
            return redirect('/')
    else:
        context = {
            'clientresisterform': clientresisterform,
        }
        return render(request, 'core/join_us_seller.html', context)


def join_driver(request):
    driverjoinform = fleet_forms.DriverJoinForm()
    try:
        driver = fleet_models.Driver.objects.get(user_id=request.user.id)
        print(driver)
        print(driver.id)
        print(driver.user_id)
        return redirect('core:profile', pk=request.user.id)
    except fleet_models.Driver.DoesNotExist:

        if request.method == 'POST':
            form = fleet_forms.DriverJoinForm(request.POST)
            if form.is_valid():
                print("DriverForm full  is valid")
                f = form.save(commit=False)
                f.driver_status = 'Aproval Pending'
                f.user_id = request.user.id
                f.driver_rating = 0
                f.driver_rating_count = 0
                f.driver_reviews = 0
                f.driver_reviews_count = 0

                f.save()
                return redirect('/')
        else:
            form = fleet_forms.DriverJoinForm()
            context = {
                'form': form,
                'driverjoinform': driverjoinform,
            }
            return render(request, 'core/join_us_driver.html', context)


def join_us(request):
    instance = get_object_or_404(core_models.Profile, user_id=request.user.id)
    joinusform = core_forms.JoinUsForm(request.POST or None, instance=instance)
    #instance_driver = get_object_or_404(Driver, user_id=request.user.id)
    driverjoinform = fleet_forms.DriverJoinForm()
    clientresisterform = client_forms.ClinetRegisterForm()

    if request.method == 'POST':
        print("join as driver")
        if driverjoinform.is_valid():
            print("driver join valid")
            form1 = joinusform.save(commit=False)
            user = User.objects.get(id=request.user.id)
            print(user)
            print(form1.user_id)
            form1.user = user
            form1.is_driver = True
            form1.is_seller = False
            form1.save()
            print(form1)
            form = driverjoinform.save(commit=False)
            print(form)
            form.user = user
            form.driver_id = request.user.id
            form.driver_status = "Active"
            print(form.driver_status)
            print(form)
            form.save()
            print(driverjoinform.cleaned_data)
            messages.success(
                request, f'Your Fleet account details has been added!')
        if clientresisterform.is_valid():
            print("join as Cleint")
            form = clientresisterform.save(commit=False)
            user = User.objects.get(id=request.user.id)
            print(user)

            # form.save()
            print(form)
            messages.success(
                request, f'Your account details has been added!')

        return redirect('core:profile', pk=request.user.id)
    else:
        print("load add form")
        context = {
            'joinusform': joinusform,
            'driverjoinform': driverjoinform,
            'clientresisterform': clientresisterform,
            'instance': instance
        }
    return render(request, 'core/join_us.html', context)


def seller_profile(request, pk):

    return render(request, 'core/seller_profile.html')


def main_dashboard(request):
    profile = get_object_or_404(core_models.Profile, user_id=request.user.id)
    if profile.is_seller:
        return redirect('client:client_dashboard')
    elif profile.is_driver:
        return redirect('fleet:fleet_dashboard')
    else:
        return redirect('core:join_us', pk=request.user.id)


# profile  pages---------------------------------------------------------------------------------------------------------------------
def profile_view(request):
    user_id = request.user.id
    if core_models.Profile.objects.filter(user_id=user_id).exists():
        #pk = request.user.id

        return redirect('core:profile', pk=user_id)
    else:
        return redirect('core:profile_add')


def profile(request, pk):
    profile = get_object_or_404(core_models.Profile, user_id=request.user.id)
    context = {}
    context["profile"] = core_models.Profile.objects.get(
        user_id=request.user.id)
    return render(request, 'core/profile.html', context)


def profile_add(request):
    profileaddform = core_forms.ProfileForm(request.POST, request.FILES)
    new_var = request.user.id
    print(new_var)
    if request.method == 'POST':
        if profileaddform.is_valid():
            print("valid")
            form = profileaddform.save(commit=False)
            form.user_id = request.user.id
            form.id = request.user.id
            print(form.user_id)
            form.save()
            messages.success(
                request, f'Your account details has been added!')
            return redirect('core:profile', pk=request.user.id)
    else:
        print("load add form")
        context = {
            'profileaddform': profileaddform,
        }
        return render(request, 'core/profile_add.html', context)


def profile_update(request, pk):
    context = {}
    instance = get_object_or_404(core_models.Profile, user_id=pk)
    form = core_forms.ProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        messages.success(
            request, f'Your account details has been Updated!')
        return redirect('core:profile', pk=pk)
    context = {
        'profileform': form,
        'instance': instance
    }
    return render(request, 'core/profile_update.html', context)


def profile_delete(request, pk):
    instance = get_object_or_404(core_models.Profile, user_id=pk)
    instance.delete()
    messages.success(
        request, f'Your account details has been Deleted!')
    return redirect('core:profile_update', pk=pk)


# driverjob ---------------------------------------------------------------------------------------------------------------------


@login_required(login_url='account_login')
def driverjobform(request):
    if request.method == 'POST':
        driverjobform = core_forms.DriverVacancyAplicationForm(
            request.POST or None)
        if driverjobform.is_valid():
            form = driverjobform.save(commit=False)
            form.user_id = request.user.id
            form.save()

            return redirect('/')

    else:
        driverjobform = core_forms.DriverVacancyAplicationForm()
    return render(request, 'core/driverjobform.html', {'driverjobform': driverjobform})
