from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from core import models as core_models
from orders import models as orders_models
from client import models as business_models
from orders import forms as orders_forms
# Create your views here.


# orders---------------------------------------------------------------------------------------------------------------------


@login_required(login_url='account_login')
def orders_list(request):
    business = business_models.Business.objects.get(user_id=request.user.id)
    orders = orders_models.Order.objects.filter(
        business_id=business.business_id).order_by('-id')
    context = {
        'orders': orders
    }
    return render(request, 'orders/orders_list.html', context)


@login_required(login_url='account_login')
def add_order(request):
    if request.method == 'POST':
        form = orders_forms.AddOrderForm(request.POST)
        form.fields['product_list'].queryset = orders_models.Items.objects.filter(
            business=request.user.business)
        if form.is_valid():
            order = form.save(commit=False)
            order.business_id = business_models.Business.objects.get(
                user_id=request.user.id).id
            print(order.business)
            form.save()
            form = orders_forms.AddOrderForm()
            return redirect('/orders/')
    else:
        form = orders_forms.AddOrderForm()
    return render(request, 'orders/add_order.html', {'form': form})


@login_required(login_url='account_login')
def update_order(request, order_id):
    order = orders_models.Order.objects.get(id=order_id)
    if request.method == 'POST':
        form = orders_forms.UpdateOrderForm(request.POST, instance=order)
        print('form valid checking')
        if form.is_valid():
            print('form valid')
            form.save()
            return redirect('/business/dashboard/')
    else:
        form = orders_forms.UpdateOrderForm(instance=order)

    context = {
        'form': form,
        'order': order,
        'order_id': order_id
    }
    return render(request, 'orders/update_order.html', context)


@login_required(login_url='account_login')
def delete_order(request):
    data = {

    }
    return render(request, 'orders/delete_order.html', data)


@login_required(login_url='account_login')
def order_details(request, order_id):
    order = orders_models.Order.objects.get(id=order_id)
    data = {
        'order': order
    }
    return render(request, 'orders/order_details.html', data)
