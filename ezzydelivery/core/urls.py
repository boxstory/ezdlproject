from django.urls import path
from core import views as core_views
from webpages import views as webpages_views
from delivery import views as delivery_views
from orders import views as orders_views

app_name = 'core'
urlpatterns = [
    path('profile/', core_views.profile_view, name='profile_view'),
    path('profile/<int:pk>/', core_views.profile, name='profile'),
    path('profile/<int:pk>/update/',
         core_views.profile_update, name='profile_update'),
    path('profile/add/',
         core_views.profile_add, name='profile_add'),
     path('dashboard/', core_views.main_dashboard, name='main_dashboard'),

    path('join_us/',
         core_views.join_us, name='join_us'),
    path('join_us/business/',
         core_views.join_business, name='join_business'),
    path('join_us/driver/',
         core_views.join_driver, name='join_driver'),
     path('join_us/business/update/',
         core_views.update_business, name='update_business'),
    path('join_us/driver/update/',
         core_views.update_driver, name='update_driver'),

    path('driverjobform/', core_views.driverjobform, name='driverjobform'),



]
