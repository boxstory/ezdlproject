from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from core import models as core_models
from orders import models as orders_models
from client import models as client_models
from orders import forms as orders_forms
# Create your views here.


# orders---------------------------------------------------------------------------------------------------------------------


@login_required(login_url='account_login')
def orders_list(request):
    client_id = client_models.Client.objects.get(user_id=request.user.id)
    orders = orders_models.Order.objects.filter(
        client_id=client_id.id).order_by('-id')
    context = {
        'orders': orders
    }
    return render(request, 'orders/orders_list.html', context)


@login_required(login_url='account_login')
def add_order(request):
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.client_id = client_models.Client.objects.get(
                user_id=request.user.id).id
            print(order.client)
            form.save()
            form = AddOrderForm()
            return redirect('/orders/')
    else:
        form = AddOrderForm()
    return render(request, 'orders/add_order.html', {'form': form})


@login_required(login_url='account_login')
def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        form = UpdateOrderForm(request.POST, instance=order)
        print('form valid checking')
        if form.is_valid():
            print('form valid')
            form.save()
            return redirect('/orders/')
    else:
        form = UpdateOrderForm(instance=order)

    context = {
        'form': form,
        'order': order,
        'order_id': order_id
    }
    return render(request, 'orders/update_order.html', context)


@login_required(login_url='account_login')
def order_details(request, order_id):
    order = Order.objects.get(id=order_id)
    data = {
        'order': order
    }
    return render(request, 'orders/order_details.html', data)


@login_required(login_url='account_login')
def delete_order(request):
    data = {

    }
    return render(request, 'orders/delete_order.html', data)


@login_required(login_url='account_login')
def order_add_item(request):
    if request.method == 'POST':
        form = AddItemsForm(request.POST)
        if form.is_valid():
            form.save()
            form = AddItemsForm()
            return redirect('/')
    else:
        form = AddItemsForm()

    data = {
        'form': form,
    }
    return render(request, 'orders/add_product_items.html', data)


@login_required(login_url='account_login')
def order_delete_item(request):
    data = {

    }
    return render(request, 'orders/delete_product_item.html', data)


@login_required(login_url='account_login')
def order_update_item(request):
    data = {

    }
    return render(request, 'orders/update_product_item.html', data)


#path('order_details/<int:pk>/add_item_sku/', orders_views.orders_dadd_item_sku, name='orders_dadd_item_sku'),
@login_required(login_url='account_login')
def order_add_item_sku(request):
    data = {

    }
    return render(request, 'orders/add_product_item_sku.html', data)


#path('order_details/<int:pk>/delete_item_sku/<int:item_sku_pk>/', orders_views.orders_delete_item_sku, name='orders_ddelete_item_sku'),
@login_required(login_url='account_login')
def order_delete_item_sku(request):
    data = {

    }
    return render(request, 'orders/delete_product_item_sku.html', data)

#path('order_details/<int:pk>/update_item_sku/<int:item_sku_pk>/', orders_views.orders_update_item_sku, name='orders_dupdate_item_sku'),


@login_required(login_url='account_login')
def order_update_item_sku(request):
    data = {

    }
    return render(request, 'orders/update_product_item_sku.html', data)
