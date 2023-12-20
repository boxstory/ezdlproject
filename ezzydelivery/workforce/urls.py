from django.urls import path
from webpages import views as webpages_views
from workforce import views as workforce_views
from delivery import views as delivery_views
from orders import views as orders_views
from core import views as core_views

app_name = 'workforce'
urlpatterns = [
    path('', workforce_views.index, name='index'),
    path('dashboard/', workforce_views.wf_dashboard, name='wf_dashboard'),
    




]
