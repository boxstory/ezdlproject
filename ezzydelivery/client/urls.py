from django.urls import path
from webpages import views as webpages_views
from delivery import views as delivery_views
from orders import views as orders_views
from core import views as core_views
from fleet import views as fleet_views
from client import views as client_views

app_name = 'client'
urlpatterns = [

    path('dashboard/', client_views.client_dashboard, name='client_dashboard'),

    # PICKUP LOCATIONS
    path('add_pickup_location/',
         client_views.add_pickup_location, name='add_pickup_location'),

]
