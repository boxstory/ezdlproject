from django.urls import path
from webpages import views as webpages_views
from delivery import views as delivery_views
from orders import views as orders_views
from core import views as core_views
from fleet import views as fleet_views
from client import views as client_views

app_name = 'fleet'
urlpatterns = [
    path('', fleet_views.fleets, name='fleets'),
    path('dashboard/', fleet_views.fleet_dashboard, name='fleet_dashboard'),
    path('update_vehicle/',
         fleet_views.update_vehicle, name='update_vehicle'),
    path('documents/', fleet_views.driver_documents, name='driver_documents'),
    path('documents/upload/', fleet_views.driver_documents_upload,
         name='driver_documents_upload'),


    path('delivery_tasks/all/', fleet_views.all_delivery_tasks,
         name='all_delivery_tasks'),
    #     path('delivery_tasks/<int:dl_id>/',
    #          fleet_views.single_delivery_task, name='single_delivery_task'),
    #     path('delivery_address_details/',
    #          delivery_views.delivery_address_details, name='delivery_address_details'),

]
