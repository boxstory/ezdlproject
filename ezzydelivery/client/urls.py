from django.urls import path
from webpages import views as webpages_views
from delivery import views as delivery_views
from orders import views as orders_views
from core import views as core_views
from fleet import views as fleet_views
from client import views as business_views

app_name = 'business'
urlpatterns = [
    # BUSINESS LINKS
    path('dashboard/', business_views.business_dashboard,
         name='business_dashboard'),

    # PICKUP LOCATIONS
    path('pickup_location/add/',
         business_views.pickup_location_add, name='pickup_location_add'),
    path('pickup_location/<int:pickup_location_id>/update/',
         business_views.pickup_location_update, name='pickup_location_update'),
    path('pickup_location/<int:pickup_location_id>/delete/',
         business_views.pickup_location_delete, name='pickup_location_delete'),
    path('pickup_locations/',
         business_views.pickup_location_list, name='pickup_location_list'),

    # frontend
    path('<int:business_id>/', business_views.profile_business,
         name='profile_business'),
    path('all', business_views.all_business, name='all_business'),

    # driver contacts list
    path('driver_contacts/', business_views.regular_driver_contacts_list,
         name='regular_driver_contacts_list'),
    path('driver_contacts/add/', business_views.regular_driver_contacts_add,
         name='regular_driver_contacts_add'),
    path('driver_contacts/<int:contact_id>/delete/',
         business_views.regular_driver_contacts_delete, name='regular_driver_contacts_delete'),

]
