from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

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
            print("POST form")
            form = orders_forms.AddOrderForm(request.POST)
            # form.fields['product_list'].queryset = orders_models.Items.objects.filter(
            #     business=request.user.business)
            if form.is_valid():
                print("valid form")
                order = form.save(commit=False)
                order.business = business_models.Business.objects.get(
                    business_id=request.user.id)
                print(order.business_id)
                form.save()
                form = orders_forms.AddOrderForm()
                return redirect('/orders/')
        else:
            print("load form")
            form = orders_forms.AddOrderForm()
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
def delete_order(request, order_id):
    order = orders_models.Order.objects.get(id=order_id).delete()
    return redirect('/business/dashboard/')


@login_required(login_url='account_login')
def order_details(request, order_id):
    order = orders_models.Order.objects.get(id=order_id)
    data = {
        'order': order
    }
    return render(request, 'orders/order_details.html', data)


# operation links

@require_POST
def update_order_status3(request):
    order_id = request.POST.get('order_id')
    new_status = request.POST.get('new_status')

    try:
        review = orders_models.Order.objects.get(id=order_id)
        review.order_status = new_status
        review.save()
        return JsonResponse({'success': True})
    except (orders_models.Order.DoesNotExist, Exception):
        return JsonResponse({'success': False})


def update_order_status(request):
    if request.method == 'POST' and request.is_ajax():
        # Assuming you have a model named "YourModel" with a "status" field
        order_id = request.POST.get('order_id')
        print(order_id)
        status=request.POST.get('status')
        order = orders_models.Order.objects.get(pk=order_id)
        order.order_status = status
        print(order.order_status)
        order.save()

        # Return a JSON response indicating success
        return JsonResponse({'status': 'success'})

    # Return a JSON response indicating failure
    return JsonResponse({'status': 'error'})
