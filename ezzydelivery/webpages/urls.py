from django.urls import path
from webpages import views as webpages_views
<<<<<<< HEAD
=======
from delivery import views as delivery_views
from orders import views as orders_views
from core import views as core_views
>>>>>>> efb83dc66fb99846065e84f234c6600276aaf31b

app_name = 'webpages'
urlpatterns = [
    path('', webpages_views.index, name='index'),
    path('about/', webpages_views.about, name='about'),
    path('contact/', webpages_views.contact, name='contact'),
    path('services/', webpages_views.services, name='services'),
    path('join_driver/', webpages_views.join_driver, name='join_driver'),
    path('privacy/', webpages_views.privacy, name='privacy'),
    path('contactus/', webpages_views.contactus, name='contactus'),

    path('fullfillment/', webpages_views.fullfillment, name='fullfillment'),



    path('terms/', webpages_views.terms, name='terms'),
    path('test/', webpages_views.test, name='test'),




]
