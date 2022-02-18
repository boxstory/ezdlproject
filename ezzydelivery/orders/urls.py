from django.urls import path
from webpages import views as webpages_views
from delivery import views as delivery_views
from orders import views as orders_views

app_name = 'orders'
urlpatterns = [
    path('', orders_views.orders_list, name='orders_list'),
    path('add_order/', orders_views.add_order, name='add_order'),

]
