from django.urls import path
from webpages import views as webpages_views
from delivery import views as delivery_views
from orders import views as orders_views

app_name = 'delivery'
urlpatterns = [

    #path('jobs/', delivery_views.delivery_jobs, name='delivery_jobs'),
    path('delivery_address_details/', delivery_views.delivery_address_details,
         name='delivery_address_details'),
    path('<int:dl_id>/<int:mobile_no>/',
         delivery_views.dl_address, name='dl_address'),

    path('ajax/get_zone_name/', delivery_views.get_zone_name, name='get_zone_name'),


    # client side delivery data
    path('delivery_list/', delivery_views.delivery_list, name='delivery_list'),


]
