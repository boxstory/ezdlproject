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
    path('pickup_location/add/',
         client_views.pickup_location_add, name='pickup_location_add'),
    path('pickup_location/<int:pickup_location_id>/update/',
         client_views.pickup_location_update, name='pickup_location_update'),
    path('pickup_location/<int:pickup_location_id>/delete/',
         client_views.pickup_location_delete, name='pickup_location_delete'),
    path('pickup_locations/',
         client_views.pickup_location_list, name='pickup_location_list'),

    # frontend
    path('<int:client_id>/', client_views.client_profile, name='client_profile'),
    path('all', client_views.all_clients, name='all_clients'),

    # driver contacts list
    path('driver_contacts/', client_views.regular_driver_contacts_list,
         name='regular_driver_contacts_list'),
    path('driver_contacts/add/', client_views.regular_driver_contacts_add,
         name='regular_driver_contacts_add'),
    path('driver_contacts/<int:contact_id>/delete/',
         client_views.regular_driver_contacts_delete, name='regular_driver_contacts_delete'),

]
