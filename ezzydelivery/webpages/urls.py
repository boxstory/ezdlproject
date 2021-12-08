from django.urls import path
from webpages import views as webpages_views

app_name = 'webpages'
urlpatterns = [
    path('', webpages_views.index, name='index'),
    path('about/', webpages_views.about, name='about'),
    path('contact/', webpages_views.contact, name='contact'),
    path('services/', webpages_views.services, name='services'),
    path('privacy/', webpages_views.privacy, name='privacy'),


]
