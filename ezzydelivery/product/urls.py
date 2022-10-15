from django.urls import path
from webpages import views as webpages_views
from delivery import views as delivery_views
from orders import views as orders_views
from product import views as product_views

app_name = 'product'
urlpatterns = [
    # ITEMS
    path('all/',
         product_views.product_item_list, name='product_item_list'),
    path('<int:product_id>/add_item/',
         product_views.product_item_add, name='product_item_add'),
    path('<int:product_id>/delete_item/',
         product_views.product_item_delete, name='product_item_delete'),
    path('<int:product_id>/update_item/',
         product_views.product_item_update, name='product_item_update'),
    # SKUS
    path('skus/all/', product_views.product_sku_list,
         name='product_sku_list'),
    path('add_item_sku/',
         product_views.product_sku_add, name='product_sku_add'),
    path('update_item_sku/<int:sku_id>/',
         product_views.product_sku_update, name='product_sku_update'),
    path('delete_item_sku/<int:sku_id>/',
         product_views.product_sku_delete, name='product_sku_delete'),


]
