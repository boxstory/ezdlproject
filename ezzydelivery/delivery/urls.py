from django.urls import path
from webpages import views as webpages_views
from delivery import views as delivery_views
from orders import views as orders_views

app_name = 'delivery'
urlpatterns = [

    # requst to user update address before delivery
    path('<str:dl_task_number>/<int:mobile_no>/',
         delivery_views.dl_address_update, name='dl_address'),

    path('ajax/get_zone_name/', delivery_views.get_zone_name, name='get_zone_name'),


    # business side delivery data
    #path('delivery_list/', delivery_views.delivery_list, name='delivery_list'),
    path('delivery_tasks/all/', delivery_views.all_delivery_tasks,
         name='all_delivery_tasks'),

    # asign driver to delivery task
    # path('assign_driver/<str:dl_task_number>/',
    #     delivery_views.assign_driver, name='assign_driver'),
]
