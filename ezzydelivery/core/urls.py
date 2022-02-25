from django.urls import path
from core import views as core_views
from webpages import views as webpages_views
from delivery import views as delivery_views
from orders import views as orders_views

app_name = 'core'
urlpatterns = [
    path('profile/', core_views.profile, name='profile'),




]
