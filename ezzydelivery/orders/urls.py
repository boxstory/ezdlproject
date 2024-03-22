from django.urls import path
from webpages import views as webpages_views
from delivery import views as delivery_views
from orders import views as orders_views

# /orders/
app_name = 'orders'
urlpatterns = [
    path('', orders_views.orders_list, name='orders_list'),
    path('partial/all', orders_views.orders_list, name='orders_list'),
    #path('partial/all', orders_views.orders_list_review, name='orders_list'),
    # ORDERS
    path('add_order/', orders_views.add_order, name='add_order'),
    path('update_order/<int:order_id>/',
         orders_views.update_order, name='update_order'),
    path('delete_order/<int:order_id>/',
         orders_views.delete_order, name='delete_order'),
    path('order_details/<int:order_id>/',
         orders_views.order_details, name='order_details'),
    # Products add to order list
    path('add_order_product/<int:order_id>/', 
         orders_views.add_order_product, name='add_order_product'),
    # operation links
    path('update_order_status/', 
         orders_views.update_order_status, name='update_order_status'),

]

