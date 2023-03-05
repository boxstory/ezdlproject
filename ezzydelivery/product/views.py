from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from product import models as product_models
from client import models as business_models
from product import forms as product_forms
# Create your views here.


# ITEMS


@login_required(login_url='account_login')
def product_item_list(request):
    products = product_models.Items.objects.filter(
        business_id=business_models.Business.objects.get(user_id=request.user.id).id)
    print(products)
    data = {
        'products': products
    }
    return render(request, 'product/product_item_list.html', data)


@login_required(login_url='account_login')
def product_item_add(request):
    form = product_forms.AddItemsForm()

    data = {
        'form': form,
    }
    return render(request, 'product/product_item_add.html', data)


@login_required(login_url='account_login')
def product_item_delete(request, product_id):
    data = {

    }
    return render(request, 'product/product_item_delete.html', data)


@login_required(login_url='account_login')
def product_item_update(request, product_id):
    product = product_models.Items.objects.get(id=product_id)
    data = {
        'product': product
    }
    return render(request, 'product/product_item_update.html', data)

# SKU


def product_sku_list(request):
    business_id = business_models.Business.objects.get(user_id=request.user.id).id
    skus = product_models.ItemSku.objects.filter(
        business_id=business_id)

    data = {
        'skus': skus
    }
    return render(request, 'product/product_sku_list.html', data)


def product_sku_add(request):
    if request.method == 'POST':
        form = product_forms.AddItemsSkuForm(request.POST)
        if form.is_valid():
            form.save()
            form = product_forms.AddItemsSkuForm()
            return redirect('/')
    else:
        form = product_forms.AddItemsSkuForm()

    data = {
        'form': form,
    }
    return render(request, 'product/product_sku_add.html', data)


def product_sku_update(request, sku_id):
    data = {

    }
    return render(request, 'product/product_sku_update.html', data)


def product_sku_delete(request, sku_id):
    data = {

    }
    return render(request, 'product/product_sku_delete.html', data)
