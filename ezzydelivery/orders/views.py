from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone

from core import models as core_models
from orders import models as orders_models
from client import models as business_models
from orders import forms as orders_forms
# Create your views here.


# orders---------------------------------------------------------------------------------------------------------------------


@login_required(login_url='account_login')
def orders_list(request):
    business = business_models.Business.objects.get(user_id=request.user.id)

    print(business, "business order list")
    orders = orders_models.Order.objects.filter(
        business=business.business_id).order_by('-id')
    print(orders)
    context = {
        'orders': orders,
        'business': business,
    }
    return render(request, 'orders/orders_list.html', context)


@login_required(login_url='account_login')
def business_orders_list(request):
    business = business_models.Business.objects.get(user_id=request.user.id)

    print(business, "business order list")
    orders = orders_models.Order.objects.filter(
        business=business.business_id).order_by('-id')
    print(orders)
    context = {
        'orders': orders,
        'business': business,
    }
    return render(request, 'orders/orders_list.html', context)


@login_required(login_url='account_login')
def latest_orders_list(request):
    business = business_models.Business.objects.get(user_id=request.user.id)

    print(business, "latest 10 order list")
    orders = orders_models.Order.objects.filter(
        business=business.business_id).order_by('-id')
    print(orders)
    context = {
        'orders': orders,
        'business': business,
    }
    return render(request, 'orders/orders_list.html', context)


@login_required(login_url='account_login')
def add_order(request):
    business = business_models.Business.objects.get(
        user_id=request.user.id)
    pickup_locations = business_models.PickupLocation.objects.filter(
        business_id=request.user.id).all()

    print('pickup_locations : ', pickup_locations)
    if not pickup_locations:
        print("pickup_locations is None")
        return redirect('/business/pickup_location/add/')
    else:
        if request.method == 'POST':
            print("POST form in views")
            form = orders_forms.AddOrderForm(request.POST)
            print(form)

            # @todo
            # form.fields['product_list'].queryset = orders_models.Items.objects.filter(
            #     business=request.user.business)
            if form.is_valid():
                print("valid form")
                order = form.save(commit=False)
                order.business = business_models.Business.objects.get(
                    business_id=request.user.id)

                print(order.business_id)
                order = form.save()
                print('order.id')
                print(order.id)
                
                return  redirect('orders:add_order_product', order_id=order.id)
        else:
            print("load form")
            form = orders_forms.AddOrderForm(business_id=business.business_id)
    return render(request, 'orders/add_order.html', {'form': form, 'business': business, })


@login_required(login_url='account_login')
def update_order(request, order_id):
    order = orders_models.Order.objects.get(id=order_id)
    if request.method == 'POST':
        form = orders_forms.UpdateOrderForm(request.POST, instance=order)
        print('form valid checking')
        if form.is_valid():
            print('form valid')
            form.save()
            return redirect('/orders/')
    else:
        form = orders_forms.UpdateOrderForm(instance=order)

    context = {
        'form': form,
        'order': order,
        'order_id': order_id
    }
    return render(request, 'orders/update_order.html', context)


@login_required(login_url='account_login')
def delete_order(request, order_id):
    order = orders_models.Order.objects.get(id=order_id)
    print(order.business.user_id)
    if request.user.id == order.business.user_id:
        print("true")
        order.delete
    # order.delete()
    return redirect('/orders/')


@login_required(login_url='account_login')
def order_details(request, order_id):
    order = orders_models.Order.objects.get(id=order_id)
    data = {
        'order': order
    }
    return render(request, 'orders/order_details.html', data)


# add products to order
@login_required(login_url='account_login')
def add_order_product(request, order_id):
    order = orders_models.Order.objects.get(id=order_id)
    try:
        order_product_list = orders_models.OrderProductList.objects.get(order_id=order_id)
    except:
        order_product_list = orders_models.OrderProductList.objects.create(order_id=order_id)
    if request.method == 'POST':
            print("POST form in views")
            form = orders_forms.AddOrderProductsForm(request.POST, instance=order_product_list)
            print(form)
            if form.is_valid():
                print("valid form")
                form.save()
                return redirect('/orders/')
    else:
        form = orders_forms.AddOrderProductsForm(instance=order_product_list)
        print('else form')
    data = {
        'order': order,
        'form': form
    }
    return render(request, 'orders/add_order_product.html', data)



# operation links

@require_POST
def update_order_status(request):
    if request.method == 'POST' and request.is_ajax():
        # Assuming you have a model named "YourModel" with a "status" field
        order_id = request.POST.get('order_id')
        print('update_order_status - view', order_id)
        status = request.POST.get('status')
        print(status)
        order = orders_models.Order.objects.get(pk=order_id)
        order.order_status = status
        print(order.order_status)
        order.save()

        # Return a JSON response indicating success
        return JsonResponse({'status': 'success'})

    # Return a JSON response indicating failure
    return JsonResponse({'status': 'error'})
