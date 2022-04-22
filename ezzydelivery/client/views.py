from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from client import models as client_models
from core import models as core_models

from client import forms as client_forms

# Create your views here.


def client_dashboard(request):

    return render(request, 'client/client_dashboard.html')

# dashboard---------------------------------------------------------------------------------------------------------------------


@login_required(login_url='account_login')
def client_dashboard(request):
    context = {}

    profile = core_models.Profile.objects.get(user_id=request.user.id)
    context['profile'] = profile
    client = client_models.Client.objects.get(user_id=request.user.id)
    context['client'] = client

    return render(request, 'client/client_dashboard.html', context)


# pickup location add------------------------------------------------------


def add_pickup_location(request):
    context = {}
    if request.method == 'POST':
        form = client_forms.PickupLocationsAddForm(request.POST)
        if form.is_valid():
            pickup_location = form.save(commit=False)
            pickup_location.client_id = client_models.Client.objects.get(
                user_id=request.user.id).id
            print(pickup_location.client)
            form.save()
            return redirect('/seller/')
    else:
        form = client_forms.PickupLocationsAddForm()
    context['form'] = form
    return render(request, 'client/add_pickup_location.html', context)
