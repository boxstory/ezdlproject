from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from product import models as product_models
from client import models as business_models
from product import forms as product_forms
# Create your views here.


# ITEMS


@login_required(login_url='account_login')
def product_all_list(request):
    business=business_models.Business.objects.get(user_id=request.user.id)
    print(business)
    products = product_models.Product.objects.all()
    print(products)
    data = {
        'products': products
    }
    return render(request, 'product/product_all_list.html', data)


@login_required(login_url='account_login')
def product_all_list_card(request):
    business=business_models.Business.objects.get(user_id=request.user.id)
    print(business)
    products = product_models.Product.objects.all()
    print(products)
    data = {
        'products': products
    }
    return render(request, 'product/product_all_list_card.html', data)


@login_required(login_url='account_login')
def product_single_add(request):
    if request.method == 'POST':
        form = product_forms.AddItemsForm(request.POST)
        if form.is_valid():
            form.save()
            form = product_forms.AddItemsForm()
            #@todo: change redirection
            return redirect('/')
    else:
        form = product_forms.AddItemsForm()

    data = {
        'form': form,
    }
    return render(request, 'product/product_single_add.html', data)


@login_required(login_url='account_login')
def product_single_delete(request, product_id):

    data = {

    }
    return render(request, 'product/product_single_delete.html', data)


@login_required(login_url='account_login')
def product_single_update(request, product_id):
    product = product_models.Items.objects.get(id=product_id)
    data = {
        'product': product
    }
    return render(request, 'product/product_single_update.html', data)


def product_inventory(request):
    data = {

    }
    return render(request, 'product/product_inventory.html', data)



def product_categories(request):
    data = {

    }
    return render(request, 'product/product_categories.html', data)