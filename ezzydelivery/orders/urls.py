from django.urls import path
from webpages import views as webpages_views
from delivery import views as delivery_views
from orders import views as orders_views

app_name = 'orders'
urlpatterns = [
    path('', orders_views.orders_list, name='orders_list'),
    # ORDERS
    path('add_order/', orders_views.add_order, name='add_order'),
    path('update_order/<int:order_id>/',
         orders_views.update_order, name='update_order'),
    path('delete_order/<int:order_id>/',
         orders_views.delete_order, name='delete_order'),
    path('order_details/<int:order_id>/',
         orders_views.order_details, name='order_details'),

    # ITEMS
    path('order_details/<int:order_id>/add_item/',
         orders_views.order_add_item, name='order_add_item'),
    path('order_details/add_item/',
         orders_views.order_add_item, name='order_add_item'),
    path('order_details/<int:order_id>/delete_item/<int:item_pk>/',
         orders_views.order_delete_item, name='orders_delete_item'),
    path('order_details/<int:order_id>/update_item/<int:item_pk>/',
         orders_views.order_update_item, name='orders_update_item'),
    path('order_details/<int:order_id>/add_item_sku/',
         orders_views.order_add_item_sku, name='orders_add_item_sku'),
    path('order_details/<int:order_id>/delete_item_sku/<int:item_sku_pk>/',
         orders_views.order_delete_item_sku, name='orders_delete_item_sku'),
    path('order_details/<int:order_id>/update_item_sku/<int:item_sku_pk>/',
         orders_views.order_update_item_sku, name='orders_update_item_sku'),

    # SKUS




]
