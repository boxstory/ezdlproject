from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='account_login')
def orders_list(request):
    data = {

    }
    return render(request, 'orders/orders_list.html', data)


@login_required(login_url='account_login')
def add_order(request):
    data = {

    }
    return render(request, 'orders/add_order.html', data)
