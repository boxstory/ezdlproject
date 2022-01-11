from django.urls import path
from webpages import views as webpages_views

app_name = 'webpages'
urlpatterns = [
    path('', webpages_views.index, name='index'),
    path('about/', webpages_views.about, name='about'),
    path('contactus/', webpages_views.contactus, name='contactus'),
    path('delivery_address_details/', webpages_views.delivery_address_details, name='delivery_address_details'),
    path('services/', webpages_views.services, name='services'),
    path('join_driver/', webpages_views.join_driver, name='join_driver'),
    path('privacy/', webpages_views.privacy, name='privacy'),


]
