from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from client import models as business_models
from core import models as core_models
from orders import models as orders_models

from client import forms as business_forms



def index(request):
    data = {}

    return render(request, 'workforce/index.html', data)


@login_required(login_url='/accounts/login/')
def wf_dashboard(request):
    profile = core_models.Profile.objects.get(user_id=request.user.id)
    data = {
        'profile': profile,

    }

    return render(request, 'workforce/wf_base_dashboard.html', data)